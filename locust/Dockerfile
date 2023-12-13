FROM python:3

RUN pip3 install locust

WORKDIR /locust
COPY . /locust/

RUN ["./run.sh"]
