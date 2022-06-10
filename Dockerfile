FROM python:3.8

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

## Set the timezone.
#RUN echo "America/New_York" > /etc/timezone
#RUN dpkg-reconfigure -f noninteractive tzdata

#FROM alpine:latest
#FROM joyzoursky/python-chromedriver:3.7-alpine3.8-selenium
#FROM joyzoursky/python-chromedriver:latest
#FROM robcherry/docker-chromedriver:latest

#RUN apk add --update chromedriver gcc g++ make python3 py-pip python3-dev && rm -rf /var/cache/apk/*
#RUN apk add --update gcc g++ make && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

COPY *.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mintapi/mintapi mintapi
COPY *.py .

CMD [ "python3", "./basic.py" ]

