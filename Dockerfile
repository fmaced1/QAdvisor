FROM python:3.12-slim AS builder

WORKDIR /app

COPY ./app/requirements.txt ./requirements.txt
RUN pip install virtualenv && \
    virtualenv venv && \
    . /app/venv/bin/activate && \
    pip install -r ./requirements.txt

FROM python:3.12-slim AS runner

WORKDIR /app
COPY --from=builder /app/venv /app/venv
COPY ./app /app

ENV REDIS_HOST="redis" \
    REDIS_PORT="6379" \
    PATH="/app/venv/bin:$PATH"

EXPOSE 8501 6379

ENTRYPOINT ["bash", "entrypoint.sh"]
CMD ["streamlit", "run", "app.py"]