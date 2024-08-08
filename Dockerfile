FROM python:3.12-slim AS builder

WORKDIR /src

COPY ./src/requirements.txt ./requirements.txt
RUN pip install virtualenv && \
    virtualenv venv && \
    . /src/venv/bin/activate && \
    pip install -r ./requirements.txt

FROM python:3.12-slim AS runner

WORKDIR /src
COPY --from=builder /src/venv /src/venv
COPY ./src /src

ENV REDIS_HOST="redis" \
    REDIS_PORT="6379" \
    PATH="/src/venv/bin:$PATH"

EXPOSE 8501 6379

ENTRYPOINT ["bash", "entrypoint.sh"]
CMD ["streamlit", "run", "app.py"]