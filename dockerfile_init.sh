#!/usr/bin/env bash

# ---
# - creates a role in AWS which has the right to execute lambda functions and save
# the results of the execution to s3
# - deploys the function to AWS Lambda
# ---

aws iam create-role --role-name nba --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'

aws iam attach-role-policy --role-name nba --policy-arn arn:aws:iam::aws:policy/AWSLambda_FullAccess
# TODO restrict access to one bucket only. This can be set up by serverless 
# framework and is beyond the scope of this project

# reuired to write files to s3 bucket
aws iam attach-role-policy --role-name nba --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

serverless deploy