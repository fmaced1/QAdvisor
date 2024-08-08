#!/bin/bash

mkdir /src/charts/html/ /src/charts/jpeg/ -p

source /src/venv/bin/activate

exec "$@"