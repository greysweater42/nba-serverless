FROM node:lts

RUN apt-get update

RUN apt-get install python3-pip -y
RUN npm install -g serverless
RUN apt install awscli -y
RUN apt install less -y
# python packages must be installed inside of a virtualenv (node container requirement)
RUN apt install python3-venv -y
RUN apt install vim -y

WORKDIR /app

# install serverless plugin which enables adding python packages to lambda
COPY serverless.yml /app/
RUN sls plugin install -n serverless-python-requirements --config /app/serverless.yml

RUN python3 -m venv venv
COPY requirements.txt /app/
RUN /app/venv/bin/pip install -r requirements.txt
COPY handler.py serverless.yml app/
