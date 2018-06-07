FROM python:3.6.5-slim

RUN mkdir /app
WORKDIR /app

COPY calculation.py test_calculation.py input.csv /app/
RUN chmod +x calculation.py test_calculation.py


LABEL maintainer="Nick Kou <nickkounz@gmail.com>" \
      version="1.0"