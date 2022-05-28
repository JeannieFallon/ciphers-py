FROM python:3.10.4-slim-bullseye

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive \
    apt install -y \
    binutils \
    make

COPY docker/requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip && \
    python -m pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

CMD ["/bin/bash"]
