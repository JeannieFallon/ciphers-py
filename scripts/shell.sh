#!/bin/bash

exec docker run -it --rm \
    --name ciphers-py \
    --hostname debian \
    --workdir `pwd` \
    -v `pwd`:`pwd` \
    ciphers-py
