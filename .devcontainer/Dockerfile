FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

USER root

RUN rm -f /etc/apt/sources.list.d/yarn.list /etc/apt/sources.list.d/yarn.list.save \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        gh \
        wget \
    && rm -rf /var/lib/apt/lists/*

USER vscode

ENV HOME=/home/vscode
ENV PATH="${HOME}/.local/bin:${HOME}/go/bin:${PATH}"

RUN curl -sS https://webi.sh/golang | sh
RUN /bin/bash -lc 'go install github.com/bootdotdev/bootdev@latest'
