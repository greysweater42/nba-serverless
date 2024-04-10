from node:lts

RUN apt-get update

RUN apt-get install python3-pip -y
RUN npm install -g serverless
RUN apt install awscli -y
RUN apt install less -y
# python packages must be installed inside of a virtualenv (node container requirement)
RUN apt install python3-venv -y
RUN apt install vim -y

WORKDIR /app
COPY dockerfile_init.sh serverless.yml requirements.txt /app/
RUN sls plugin install -n serverless-python-requirements --config /app/serverless.yml
RUN bash /app/dockerfile_init.sh
