#!/usr/bin/env bash

pwd

REAL_PATH=$(dirname $(realpath ${0}))
echo ${REAL_PATH}

python3 ${REAL_PATH}/draw.py
python3 ${REAL_PATH}/transform.py
python3 ${REAL_PATH}/polygon.py
