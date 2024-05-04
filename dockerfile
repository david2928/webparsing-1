FROM python:3.11.9-slim

# create app folder
RUN mkdir /opt/app

# create output folder
RUN mkdir /tmp/browserdownload
RUN mkdir /tmp/browserscreenshots

ADD app /opt/app

WORKDIR /opt/app

RUN pip install -r requirenments.txt

RUN apt-get update && playwright install && playwright install-deps

ENTRYPOINT [ "python", "app.py"] 