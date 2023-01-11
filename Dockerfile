# Copyright Christopher Hock (c) 2023 ByteOtter

ARG APP_IMAGE=python:3.10.9

FROM $APP_IMAGE AS base

FROM base as builder

RUN mkdir /install

WORKDIR /install

COPY requirements.txt /requirements.txt

# TODO: this pip command seems to be deprecated
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

ENV FLASK_APP /OtterDen/main.py

WORKDIR /project

COPY --from=builder /install /usr/local

ADD . /project

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
