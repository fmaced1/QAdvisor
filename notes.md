FROM ubuntu

USER root

RUN apt update -y \
    && apt install python3.8 python3-pip -y \
    && mkdir /app/

COPY ./meu_venv ./requirements.txt /app/venv/

WORKDIR /app/venv/

RUN . /app/venv/bin/activate \
    && python3.8 -m pip install -r requirements.txt --find-links=Tarhouse \
    && pip3 freeze

virtualenv meu-virtual-env
cd meu-virtual-env

mkdir wheelhouse && cd wheelhouse (Windows)
mkdir tarhouse && cd tarhouse (Linux)

pip download virtualenv django numpy
pip freeze > requirements.txt
Leve os arquivos .whl / .tar baixados para uma estação offline