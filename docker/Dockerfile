# Development image to build, format, and test project
FROM python:3.10.4-slim-bullseye

ARG USER=dev
ARG UID=1000
ARG GID=1000
ARG PW=dev

# Create non-root dev user
RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | \
    chpasswd

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive \
    apt install -y \
    binutils \
    make

COPY docker/requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip && \
    python -m pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# Run container with non-root dev user
USER ${UID}:${GID}
CMD ["/bin/bash"]
