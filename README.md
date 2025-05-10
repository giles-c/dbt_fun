# DBT Fun

## Introduction

This exercise is designed to enable a team to demonstrate their knowledge of good software and data engineering practices. 

It should take around half a day to complete.

Please use the Python script to generate the required sample data instructions can be found in the README.md under data_generator.

### Instructions
The purpose of this exercise is to complete a small data pipeline that aggregates and transforms input data according to requirements driven by our engagement team. The details of this are given later in this document.

Please build out your solution and submit a PR once complete

You will be required to have an AWS account. 

You will also need a trial Snowflake account to complete the task.

The aim of this exercise is to write code that processes existing data sources so that it meets requirements. 
As part of solving this, we are looking to assess:

* Your problem-solving approach.
* Your ability to turn your solution into working code and choose appropriate technology.

## Task 

    The task involves developing a data pipeline 
    using synthetic sample data.

    Our engagement team has reached out to your 
    data engineering team requesting we create a data
    mart to enable self service reporting

The input data sources are comprised of insureds (in CSV format), reinsurance treaties (CSV), speciality lines (CSV),
policies (in JSON Lines format) and claims (JSONL). Their details are presented below:

### Acceptance Criteria

Create a warehouse (facts and dimensions) that will support the self service capability.

To arrive at this the following steps will need to be completed:

* Create a secure S3 bucket
* Upload data to bucket
* Ingest data from bucket to Snowflake
* Create models in DBT


### Further Implementation Details
The repo contains a starter project that includes the input data sources, a virtual environment with some dependencies you may find useful and some basic tests to ensure the environment is ready - but only for Python.

It is preferred to use Infrastructure-as-Code (Terraform) for completing the above tasks. Areas of automation and improvements can be highlighted in the code. 

The code and design should meet the above requirements, and should consider future extension or maintenance by different members of the team.
