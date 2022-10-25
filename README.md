# Spark Training Project

[[_TOC_]]

## Purpose

This is the top-level directory for PySpark training. This is to help onboard new hires on what we expect all PySpark
jobs to be written. This also help existing developers to learn the same. This project is intended to be a living
document. Any questions, comments, or concerns are expected to be raised to the team and or your manager. While every
effort has been made to make this project meet all development guidelines and be 100% accurate, I won't pretend it is
perfect.

While this project is specifically designed for PySpark jobs, many of these principals can be applied to any ETL job.

## Contact

If you have any questions, comments, concerns or suggestions, please contact the team or your manager. Any PySpark
developer should have the knowledge to help understand the content contained. This was originally written by 📷-Cameron
Larson and reviewed by 🍞-Brad Transtrum and 🧢-Bill Larkin.

## Topics Covered

### Audits

Audits run with every job to verify all data is accounted for with no record or
data loss. While audits cant guarantee that the job is bug free. It can show that no data loss has occured. These can be
categorized into two distinct buckets:

1. _Basic_: steps that can be applied to any job
2. _Specific_: steps that are designed specifically to the current job and its data

### Logging

### Unit Tests

### Self-healing / Restartable

read the records from the source that has changed since the last execution
clear out previous failed runs

### Single Execution

single execution framework

## Modules

This training project is designed with a base PySpark job. It is a simple job that meets very little requirements. It
runs and runs without any execution errors. The other modules use this base PySpark job with the specified topic added.

You will want to run and understand the base spark job code well before jumping into the other modules. This will help
you to understand the specific code and purpose of each topic.

Each module is meant to be run standalone in PyCharm. The dependencies for each module is contained within the module
itself and the training_utils project. The source data is randomly generated data. No data connections are needed to run
any module. The output _is_ written to disk but can be deleted after.

### base_spark_job

This module is the base code that the other modules build upon. This is quite a simple project. The requirements to the
job are:

1. Uppercase all values where the field type is string when the record is an update
2. Calculate each row to show the percent of total for field `amount`. Each job execution should total 100%.

### audits_job

### logging_job

### unit_tests_job

### self_healing_job

### single_execution_job

## Setup and Testing

Quick setup guide on how to execute the Job via Pycharm or through a Spark Submit
command.

### Pycharm Setup

Before continuing make sure you have set up Pycharm for Data Pipeline Development. Follow [this wiki
here](https://berkadiadevops.visualstudio.com/Polaris/_wiki/wikis/Polaris.wiki/6759/Setting-Up-Pycharm-for-Data-Pipeline-Development)
if you haven't \

1. Open your Run/Debug Configuration that you will be using
2. Set the value for Script Path to point to the main.py module, this is our entrypoint to the
   Job.  \
   `<path to project>/data-pipeline-databridge-import-dms/src/jobs/import_dms_document_data/main.py`
3. Set the value for Parameters, depending on what you are testing this value will vary. See
   [Parameter Arguments](#parameter-arguments) for options. For debugging my parameters will look
   something like \
   `--Env Dev --Local True` \
   This loads the local <ssm_param>.example.json which allows for quick cycles when making edits to an
   SSM Param. When testing the AWS SSM Param you would just change your parameters to look like \
   `--Env Dev -SSMParameterName <name of ssm parameter>`
4. Select your Python Interpreter from the dropdown
5. Set the value for Working directory, this is the root of your project and will look something
   similar to \
   `<path to project>/<data-pipeline-databridge-import-dms>`

## Related Docs

[Import DMS Document Data FSD](https://lucid.app/lucidchart/77185a06-1e34-4151-b490-b68678f3214e/edit?invitationId=inv_bded16c3-287c-4dbe-bf7d-597ab43e7bfa&page=0_0#) \
[Imports DMS Document Data Repo](https://dev.azure.com/berkadiadevops/Polaris/_git/data-pipeline-databridge-import-dms)