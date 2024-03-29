# Copyright Christopher Hock (c) 2023 ByteOtter

FROM python:3.10.9

WORKDIR /otterdenimage

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
