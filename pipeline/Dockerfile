# start with slim python 3.13 image
FROM python:3.13.10-slim

# copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# set working directory
WORKDIR /app

# add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"

# copy dependency files first (better layer caching)
COPY "pyproject.toml" "uv.lock" ".python-version" ./

# install dependencies from lock file (ensures reproducible builds)
RUN uv sync --locked

# copy application code
COPY pipeline.py pipeline.py

# set entry point
ENTRYPOINT ["uv", "run", "python", "pipeline.py"]
