FROM    python:3.10.1-buster
ENV     pythonbuffered 1
WORKDIR /workspaces
RUN     apt update && apt install -y curl
RUN     curl -sSL https://install.python-poetry.org | python3 -
# RUN     apt install -y pre-commit

# Poetryのパスの設定
ENV PATH /root/.local/bin:$PATH

# Poetryが仮想環境を生成しないようにする
RUN poetry config virtualenvs.create false

WORKDIR /workspaces/django_turbo/sources/backend

# COPY ./../../../sources/backend .
# COPY . .
# RUN poetry install

WORKDIR /workspaces/django_turbo/sources/frontend

# COPY ././../../sources/frontend .

# https://qiita.com/teco_iida/items/0e73740d4a08bfcb58f5
RUN apt update && apt install -y graphviz
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
SHELL ["/bin/bash", "-c"]
RUN \
    source ~/.profile && \
    nvm install v20.9.0 && \
    npm install -g pnpm turbo

WORKDIR /workspaces/drf_turbo/sources