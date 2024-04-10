# Example of using `serverless framework` in Python

This simple project demonstrates how you can use [serverless framework](https://www.serverless.com/) to run a simple python function in AWS Lambda.

The function downloads the scores of the NBA games from yesterday and saves them to s3 bucket.

# Setup

1. make sure you store your AWS access key in `~/.aws/credentials`. You may also want to set 

```
[default]
region = eu-central-1
output = json
```

in `~/.aws/config`.

2. `docker-compose up --build` will:

    - create a nodejs-based docker container

    - install all relevant dependencies, including python and serverless framework

    - deploy this example python application to lambda. You'll be able to trigger the application by sending a GET request (using either curl or your browser) to the address provided at the end of the logs from docker-compose. The endpoint is set up by serverless at Amazon API Gateway.

# Resources

The code is based on this article: [https://www.freecodecamp.org/news/how-to-deploy-aws-lambda-with-serverless/](https://www.freecodecamp.org/news/how-to-deploy-aws-lambda-with-serverless/).

This piece of documentation helps to understand how to deal with python dependencies in your code: [https://www.serverless.com/plugins/serverless-python-requirements](https://www.serverless.com/plugins/serverless-python-requirements).
