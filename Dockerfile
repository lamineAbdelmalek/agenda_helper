FROM python:3.10-slim

WORKDIR /agenda_helper
COPY . .
RUN set -ex \
    \
    && pip install ./ \
    && rm -rf ~/.cache/pip pyproject.toml poetry.lock README.md

ENV GUNICORN_CMD_ARGS "--bind=0.0.0.0:80  --worker-class uvicorn.workers.UvicornWorker"
EXPOSE 80
CMD ["gunicorn", "agenda_helper.fastapi_views:app"]

