"""Harbor agent preserving the Convex benchmark's single-response semantics."""

from __future__ import annotations

import asyncio
import json
import os
import re
import shlex
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Literal, override

import httpx

from harbor.agents.base import BaseAgent
from harbor.environments.base import BaseEnvironment
from harbor.models.agent.context import AgentContext


FENCE = chr(96) * 3
SYSTEM_PROMPT = (
    "You are convexbot, a highly advanced software engineer specialized in "
    "creating applications using Convex and TypeScript."
)


ApiName = Literal["auto", "openai", "gemini"]


@dataclass(frozen=True)
class GenerationResult:
    text: str
    input_tokens: int | None
    output_tokens: int | None
    cached_tokens: int | None
    finish_reason: str | None
    api: str
    model: str


class ConvexSingleShotAgent(BaseAgent):
    """Make one model call, parse Convex markdown, and upload the files."""

    def __init__(
        self,
        api: ApiName = "auto",
        reasoning_effort: str = "medium",
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        if api not in {"auto", "openai", "gemini"}:
            raise ValueError("api must be one of: auto, openai, gemini")
        self._api: ApiName = api
        self._reasoning_effort = reasoning_effort

    @staticmethod
    @override
    def name() -> str:
        return "convex-single-shot"

    @override
    def version(self) -> str:
        return "0.2.0"

    @override
    async def setup(self, environment: BaseEnvironment) -> None:
        return None

    @override
    async def run(
        self,
        instruction: str,
        environment: BaseEnvironment,
        context: AgentContext,
    ) -> None:
        model = self.model_name or "gemini/gemini-3.5-flash"
        generated = await self._generate(instruction, model)
        parsed = self._parse_files(generated.text)
        if not parsed:
            raise RuntimeError("Model response contained no parseable files")

        self.logs_dir.mkdir(parents=True, exist_ok=True)
        (self.logs_dir / "model-response.md").write_text(generated.text)
        (self.logs_dir / "parsed-files.json").write_text(
            json.dumps(sorted(parsed), indent=2)
        )

        with tempfile.TemporaryDirectory(prefix="convex-single-shot-") as temp:
            temp_root = Path(temp)
            for relative_path, content in parsed.items():
                local_path = temp_root / relative_path
                local_path.parent.mkdir(parents=True, exist_ok=True)
                local_path.write_text(content)
                target = "/app/" + relative_path
                parent = str(PurePosixPath(target).parent)
                result = await environment.exec(
                    "mkdir -p " + shlex.quote(parent),
                    timeout_sec=30,
                )
                if result.return_code != 0:
                    raise RuntimeError("Could not create " + parent)
                await environment.upload_file(local_path, target)

        context.n_input_tokens = generated.input_tokens
        context.n_output_tokens = generated.output_tokens
        context.n_cache_tokens = generated.cached_tokens
        context.metadata = {
            "single_model_call": True,
            "api": generated.api,
            "api_override": self._api,
            "model": generated.model,
            "file_count": len(parsed),
            "finish_reason": generated.finish_reason,
        }

    async def _generate(self, prompt: str, model: str) -> GenerationResult:
        api = self._select_api(model)
        if api == "gemini":
            return await self._generate_gemini(prompt, model)
        return await self._generate_openai(prompt, model)

    def _select_api(self, model: str) -> Literal["openai", "gemini"]:
        if self._api != "auto":
            return self._api
        prefix = model.partition("/")[0].lower() if "/" in model else ""
        return "gemini" if prefix in {"gemini", "google"} else "openai"

    def _env(self, name: str) -> str | None:
        return self.extra_env.get(name) or os.environ.get(name)

    @staticmethod
    async def _post_with_retries(
        client: httpx.AsyncClient,
        url: str,
        *,
        headers: dict[str, str],
        payload: dict[str, Any],
    ) -> httpx.Response:
        """Match Convex's five retries for rate limits and transient 5xx errors."""
        for attempt in range(6):
            response = await client.post(url, headers=headers, json=payload)
            retryable = response.status_code == 429 or response.status_code >= 500
            if not retryable or attempt == 5:
                response.raise_for_status()
                return response
            await asyncio.sleep(min(2**attempt, 16))
        raise AssertionError("retry loop must return or raise")

    async def _generate_openai(
        self, prompt: str, model: str
    ) -> GenerationResult:
        api_key = self._env("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")
        base_url = (
            self._env("OPENAI_BASE_URL")
            or self._env("OPENAI_API_BASE")
            or "https://api.openai.com/v1"
        ).rstrip("/")
        url = (
            base_url
            if base_url.endswith("/chat/completions")
            else base_url + "/chat/completions"
        )
        if "generativelanguage.googleapis.com" in base_url and model.startswith("google/"):
            request_model = model.split("/", 1)[1]
        else:
            request_model = (
                model.split("/", 1)[1] if model.startswith("openai/") else model
            )
        payload = {
            "model": request_model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
        }
        token_parameter = (
            "max_completion_tokens"
            if "api.openai.com" in base_url
            else "max_tokens"
        )
        payload[token_parameter] = 16384
        if "openrouter.ai" in base_url:
            # Match Convex's OpenRouter request transformation exactly.
            payload["reasoning"] = {"effort": self._reasoning_effort}
        elif "generativelanguage.googleapis.com" in base_url:
            payload["reasoning_effort"] = self._reasoning_effort
        async with httpx.AsyncClient(timeout=900) as client:
            response = await self._post_with_retries(
                client,
                url,
                headers={
                    "Authorization": "Bearer " + api_key,
                    "Content-Type": "application/json",
                },
                payload=payload,
            )
            body = response.json()
        choices = body.get("choices") or []
        if not choices:
            raise RuntimeError("OpenAI-compatible API returned no choices")
        content = (choices[0].get("message") or {}).get("content") or ""
        if isinstance(content, list):
            content = "".join(
                part.get("text", "") for part in content if isinstance(part, dict)
            )
        usage = body.get("usage") or {}
        details = usage.get("prompt_tokens_details") or {}
        return GenerationResult(
            text=str(content),
            input_tokens=usage.get("prompt_tokens"),
            output_tokens=usage.get("completion_tokens"),
            cached_tokens=details.get("cached_tokens"),
            finish_reason=choices[0].get("finish_reason"),
            api="openai",
            model=request_model,
        )

    async def _generate_gemini(
        self, prompt: str, model: str
    ) -> GenerationResult:
        api_key = self._env("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set")
        request_model = model.split("/", 1)[1] if "/" in model else model
        base_url = (
            self._env("GEMINI_BASE_URL")
            or "https://generativelanguage.googleapis.com/v1"
        ).rstrip("/")
        url = (
            base_url
            if base_url.endswith("/interactions")
            else base_url + "/interactions"
        )
        payload = {
            "model": request_model,
            "input": prompt,
            "system_instruction": SYSTEM_PROMPT,
            "store": False,
            "generation_config": {"max_output_tokens": 16384},
        }
        async with httpx.AsyncClient(timeout=900) as client:
            response = await self._post_with_retries(
                client,
                url,
                headers={
                    "x-goog-api-key": api_key,
                    "Content-Type": "application/json",
                },
                payload=payload,
            )
            body = response.json()
        steps = body.get("steps") or []
        output_steps = [step for step in steps if step.get("type") == "model_output"]
        if not output_steps:
            raise RuntimeError("Gemini Interactions API returned no model output")
        text = "".join(
            item.get("text", "")
            for step in output_steps
            for item in (step.get("content") or [])
            if item.get("type") == "text"
        )
        usage = body.get("usage") or {}
        return GenerationResult(
            text=text,
            input_tokens=usage.get("total_input_tokens"),
            output_tokens=usage.get("total_output_tokens"),
            cached_tokens=usage.get("total_cached_tokens"),
            finish_reason=body.get("status"),
            api="gemini",
            model=request_model,
        )

    @staticmethod
    def _parse_files(response: str) -> dict[str, str]:
        files_heading = re.search(r"(?m)^# Files\s*$", response)
        if not files_heading:
            return {}
        section = response[files_heading.end() :]
        fence = re.escape(FENCE)
        pattern = re.compile(
            r"(?ms)^##[ \t]+([^\r\n]+?)\s*\r?\n"
            + fence
            + r"[^\r\n]*\r?\n(.*?)\r?\n"
            + fence
            + r"[ \t]*$"
        )
        files: dict[str, str] = {}
        for match in pattern.finditer(section):
            relative = match.group(1).strip()
            path = PurePosixPath(relative)
            if path.is_absolute() or ".." in path.parts or relative.startswith("."):
                raise ValueError("Unsafe generated path: " + relative)
            files[relative] = match.group(2).strip()
        return files


class ConvexReplayAgent(ConvexSingleShotAgent):
    """Replay saved single-shot responses to debug or rescore without API calls."""

    def __init__(self, replay_run: str, tasks_dir: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._responses: dict[str, tuple[str, dict[str, Any]]] = {}
        run_root = Path(replay_run)
        task_root = Path(tasks_dir)
        for result_path in run_root.glob("*/result.json"):
            result = json.loads(result_path.read_text())
            task_name = result.get("task_name", "").split("/")[-1]
            response_path = result_path.parent / "agent/model-response.md"
            instruction_path = task_root / task_name / "instruction.md"
            if response_path.exists() and instruction_path.exists():
                self._responses[instruction_path.read_text()] = (
                    response_path.read_text(),
                    result.get("agent_result") or {},
                )

    @staticmethod
    @override
    def name() -> str:
        return "convex-single-shot-replay"

    @override
    async def _generate(self, prompt: str, model: str) -> GenerationResult:
        if prompt not in self._responses:
            raise KeyError("No saved response matches this exact instruction")
        response, agent_result = self._responses[prompt]
        metadata = agent_result.get("metadata") or {}
        return GenerationResult(
            text=response,
            input_tokens=agent_result.get("n_input_tokens"),
            output_tokens=agent_result.get("n_output_tokens"),
            cached_tokens=agent_result.get("n_cache_tokens"),
            finish_reason=metadata.get("finish_reason") or "replayed",
            api="replay",
            model=metadata.get("model") or model,
        )
