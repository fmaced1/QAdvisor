FROM python:3.8-slim-buster

COPY ./src/requirements.txt /src/
WORKDIR /src/
RUN pip install -r requirements.txt
EXPOSE 8501 6379

COPY ./src/ /src

ENV REDIS_HOST="redis" REDIS_PORT="6379"

ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]