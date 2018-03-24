#
# Python Dockerfile
#
# https://github.com/dockerfile/python
#

# Pull base image.
#FROM dockerfile/ubuntu
FROM python:3

ADD . /

# Install Python.
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  pip install -r /data/requirements.txt && \

# Define default command.
CMD ["python","bot.py"]
