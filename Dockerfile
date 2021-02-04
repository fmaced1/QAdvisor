FROM python:3.8-slim-buster as base

FROM base as builder
ENV PY_LIBS="/libs"
RUN mkdir $PY_LIBS
WORKDIR $PY_LIBS
COPY requirements.txt $PY_LIBS
RUN pip install --prefix=$PY_LIBS --no-warn-script-location -r requirements.txt

FROM base
ENV APP="/app"
COPY --from=builder $PY_LIBS /usr/local/bin/
COPY src $APP
WORKDIR $APP