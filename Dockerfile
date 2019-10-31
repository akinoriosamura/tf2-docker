FROM tensorflow/tensorflow:latest-gpu-py3

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    wget build-essential gcc zlib1g-dev git default-mysql-client default-libmysqlclient-dev \
    vim \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip3 install -U pip
RUN pip install pipenv
