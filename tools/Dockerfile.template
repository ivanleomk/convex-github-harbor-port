FROM oven/bun:1.3.8

# Runtime tools used by Convex's official scorer and backend bundle.
RUN apt-get update \
  && apt-get install -y --no-install-recommends git ca-certificates curl unzip \
  && rm -rf /var/lib/apt/lists/*

# Pin and cache the same local Convex backend used by the native comparison.
# This Docker layer is shared across tasks and avoids 76 GitHub API/downloads.
ARG CONVEX_BACKEND_VERSION=precompiled-2026-07-10-f35f765
ARG CONVEX_BACKEND_ASSET=convex-local-backend-x86_64-unknown-linux-gnu.zip
RUN mkdir -p /root/.convex-evals/releases /tmp/convex-backend \
  && curl --fail --location --retry 3 \
    "https://github.com/get-convex/convex-backend/releases/download/${CONVEX_BACKEND_VERSION}/${CONVEX_BACKEND_ASSET}" \
    --output /tmp/convex-backend/backend.zip \
  && unzip /tmp/convex-backend/backend.zip -d /tmp/convex-backend \
  && install -m 0755 /tmp/convex-backend/convex-local-backend \
    "/root/.convex-evals/releases/convex-local-backend-${CONVEX_BACKEND_VERSION}" \
  && rm -rf /tmp/convex-backend

WORKDIR /app
