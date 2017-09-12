# platform-application

## Overview
This is a reference application for building [serverless](https://aws.amazon.com/serverless/) REST API backends using [flask-api](https://github.com/flask-api/flask-api) and [flask-restful](https://github.com/flask-restful/flask-restful), and deploying on [AWS Lambda](https://aws.amazon.com/lambda/) and [Amazon API Gateway](https://aws.amazon.com/api-gateway/).

## Prerequisites
- [Python Virtual Environment](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

## Getting Started

[Fork](https://help.github.com/articles/fork-a-repo/) this repo and clone your project *(replace the clone URL below with your fork's clone URL)*

	$ cd ~/Projects
	$ git clone https://github.com/excessivedemon/platform-application.git
	$ cd platform-application

Create your virtual environment

	$ virtualenv ~/platform-application

Activate your virtual environment

	$ source ~/platform-application/bin/activate

Install required packages

	$ pip install -r requirements.txt

Run the project

	$ python app.py

Access endpoints

	$ curl http://localhost:5000/
	{
		"message": "Hello World"
	}

Run tests

	$ python app_tests.py

## Endpoints
The following endpoints are provided:

<dl>
  <dt>/</dt>
  <dd>returns <code>{"message": "Hello World"}</code></dd>
  <dt>/root</dt>
  <dd>same as above</dd>
  <dt>/metadata</dt>
  <dd>returns the deployed application's git commit hash <em>(lastcommitsha)</em> and tag <em>(version)</em>. If the commit has not been tagged, the version returned is <code>null</code>. If the application has not been deployed in <a href="https://aws.amazon.com/lambda/">AWS Lambda</a> and <a href="https://aws.amazon.com/api-gateway/">Amazon API Gateway</a> using the <a href="https://github.com/excessivedemon/platform-infrastructure">platform-infrastructure</a> deploy project, returned values for both <code>lastcommitsha</code> and <code>version</code> are <code>null</code>. An example of returned JSON is: <code>{"lastcommitsha": "9ceda4e5f560f3e9758520e21a0b94bfed3dae67", "version": "7.0"}</code></dd>
  <dt>/health</dt>
  <dd>returns HTTP status code <em>(status_code)</em> received from calling the <code>/root</code> endpoint. The response time in seconds <em>(response_time)</em> is also returned. If the application has not been deployed in <a href="https://aws.amazon.com/lambda/">AWS Lambda</a> and <a href="https://aws.amazon.com/api-gateway/">Amazon API Gateway</a> using the <a href="https://github.com/excessivedemon/platform-infrastructure">platform-infrastructure</a> deploy project, returned value for both <code>status_code</code> and <code>response_time</code> is <code>null</code>. An example of returned JSON is: <code>{"status_code": 200, "response_time": 0.81}</code></dd>
</dl>

## Deploying
A separate [platform-infrastructure](https://github.com/excessivedemon/platform-infrastructure) project has been created to automate the creation of a CI/CD Pipeline for deploying this project in [AWS Lambda](https://aws.amazon.com/lambda/) and [Amazon API Gateway](https://aws.amazon.com/api-gateway/). Please refer to the [platform-infrastructure](https://github.com/excessivedemon/platform-infrastructure) project's documentation.
