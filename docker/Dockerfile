FROM docker:latest

COPY requirements/requirements.txt /tmp/requirements.txt

RUN apk add py3-pip --no-cache && \
pip3 install --upgrade pip --no-cache-dir && \
pip3 install -r /tmp/requirements.txt --no-cache-dir

COPY pyplineCI.py /

RUN PPATH=$(LOC=$(python3 -c "import easy_install as _; print(_.__file__)"); dirname $LOC) && \
    mv /pyplineCI.py $PPATH
