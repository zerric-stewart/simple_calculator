FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY . /app

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app"

RUN uv sync --all-groups && \
    uv pip install -e . && \
    pytest

CMD ["python", "src/calculator/calculator.py"]
