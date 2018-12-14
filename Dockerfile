FROM docker:latest

COPY requirements.txt /tmp/requirements.txt

RUN apk -U add python py-pip --no-cache && \
pip install --upgrade pip --no-cache-dir && \
pip install -r /tmp/requirements.txt --no-cache-dir

COPY pyplineCI.py /usr/lib/python2.7/
