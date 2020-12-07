FROM python:3.8-slim-buster as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /install/
RUN pip install --prefix=/install --no-warn-script-location -r requirements.txt

FROM base
COPY --from=builder /install /usr/local/bin/
COPY src /app
WORKDIR /app