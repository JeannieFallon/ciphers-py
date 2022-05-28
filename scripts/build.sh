#!/bin/bash

exec pyinstaller \
    --distpath bin \
    --specpath build \
    --onefile \
    src/ciphers.py
