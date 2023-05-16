FROM python:latest
WORKDIR /code
COPY ./requirements.txt /code
RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000