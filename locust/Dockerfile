FROM python:3

RUN pip3 install locust

WORKDIR /locust
COPY . /locust/

CMD ["./run.sh"]
