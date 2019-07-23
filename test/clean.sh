#!/usr/bin/env bash

pwd

REAL_PATH=$(dirname $(realpath ${0}))
echo ${REAL_PATH}

rm -rf ${REAL_PATH}/data/output

