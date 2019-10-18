FROM python:3
# LABEL maintainer="timvanmourik@gmail.com" <-- replace

ENV PYTHONUNBUFFERED 1
RUN mkdir /code /code/requirements
WORKDIR /code

# Install Python dependencies
COPY requirements.txt /code/
COPY requirements/base.txt /code/requirements/
RUN pip install -r requirements.txt

EXPOSE 8000
