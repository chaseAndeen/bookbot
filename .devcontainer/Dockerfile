FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN rm -f /etc/apt/sources.list.d/yarn.list /etc/apt/sources.list.d/yarn.list.save \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        git \
        git-lfs \
        gh \
        python3-venv \
        wget \
    && rm -rf /var/lib/apt/lists/*

USER vscode

ENV HOME=/home/vscode
ENV PATH="${HOME}/.local/bin:${HOME}/go/bin:${PATH}"
ENV GOBIN="${HOME}/go/bin"

RUN mkdir -p "${HOME}/.local/bin" "${HOME}/go/bin" \
    && curl -sS https://webi.sh/golang | sh \
    && /bin/bash -lc 'go install github.com/bootdotdev/bootdev@latest'
