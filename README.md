[![CircleCI](https://dl.circleci.com/status-badge/img/gh/ankur1230/Udacity-DevOps-Capstone/tree/main.svg?style=svg)](https://app.circleci.com/pipelines/github/buikhongminh/Capstone-Project)


# Capstone Project

This is my repository: https://github.com/buikhongminh/Capstone-Project

This is the capstone project for the Udacity Cloud DevOps Engineer Nanodegree program. The project involves building, linting, and deploying an application using various tools and technologies.
In this project I apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

- Working in AWS
- Circle CI to implement Continuous Integration and Continuous Deployment
- Building pipelines
- Working CloudFormation to deploy clusters
- Building Kubernetes clusters - Elastic Kubernetes Service
- Building Docker containers in pipelines

## Application

The Application is based on a python3 script using flask render_template to render a simple html in browser.

## Project Structure

The project repository has the following structure:
.
├── eks-cluster             # contain the Elastic Kubernetes Service file
│   └── cluster.yaml        # create the Elastic Kubernetes Service
|── templates               # contain the html file
│   └── index.html          # create the Elastic Kubernetes Service
|── app.py                  
├── deployment.yml          # deploy the application
├── Dockerfile              # builde the application Docker image
├── Makefile                
├── requirements.txt
└── README.md

## Access the Application

Public LB DNS: http://af0697559b2b34ed2a8306cfb13ac6dc-783596888.us-east-1.elb.amazonaws.com/

![Access LB DNS](./submission/screenshots/Web_after_deployment.png)