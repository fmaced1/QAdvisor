#!/bin/bash

mkdir /app/charts/html/ /app/charts/jpeg/ -p
source /app/venv/bin/activate

exec "$@"