#!/bin/bash

# Run shell into development image with project dir mounted
exec docker run -it --rm \
    --volume `pwd`:`pwd` \
    --workdir `pwd` \
    --name ciphers-py \
    --hostname debian \
    ciphers-py
