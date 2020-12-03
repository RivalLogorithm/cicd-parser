FROM python:3.8
RUN pip3 install --user pipenv
FROM alpine:3.12.1
RUN apk add --update --no-cache curl jq python3 py3-pip \
        python3-dev g++ gcc libxml2 libxml2-dev libxslt-dev 
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
COPY project /src/project
CMD ["python3", "/src/project/parser_app.py"]