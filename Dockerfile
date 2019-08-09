FROM ubuntu:latest
FROM python:3

MAINTAINER Selvyn Wright "swright@celestial.co.uk"
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip 
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD [ "./helloworld.py" ]