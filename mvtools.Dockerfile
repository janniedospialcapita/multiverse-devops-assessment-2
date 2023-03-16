
FROM python:3-slim

ADD python-survey-app /root/python-survey-app

WORKDIR /root/python-survey-app

RUN python -m pip install -r requirements.txt

#CMD [“python”, “app.py”]

RUN python app.py > result.txt
RUN pytest --cov=. | tee test.log
#CMD cat ./result.txt ./test.log

FROM amazon/aws-cli:latest

RUN yum update -y \
    && yum install -y yum-utils shadow-utils \
    && yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo \
    && yum install -y terraform

RUN mkdir ~/.aws && echo -e "[default]\nregion = eu-west-2\noutput = json" > /root/.aws/config
ADD aws-credentials /root/.aws/credentials

WORKDIR /root
ENTRYPOINT /bin/bash

