`project root ◄`<br>
`├── base_spark_job`<br>
`├── audit_spark_job`<br>
`├── logging_spark_job`<br>
`├── unit_test_spark_job`<br>
`├── self_head_spark_job`<br>
`└── single_execution_spark_job`<br>

# Spark Training Project

[[_TOC_]]

## Purpose

This is the top-level directory for PySpark Training. This is to help new hires and current developers alike to
understand expectations for all PySpark jobs. This project is a living document and will continue to be supported
and enhanced.

While this project is specifically designed for PySpark jobs, many of these principals should be applied to any ETL job.

---

## How You Can Help

While every effort has been made to make this project meet all development guidelines and be 100% accurate, I won't
pretend it is perfect. Any questions, comments, or concerns are expected to be raised to the team and/or your manager.

---

## Contact

If you have any questions, comments, concerns or suggestions, please contact the team or your manager. Any PySpark
developer should have the knowledge to help understand the content contained here in. This was originally written
by 📷-Cameron Larson and reviewed by 🍞-Brad Transtrum and 🧢-Bill Larkin.

---

## Topics Covered

### Audits

[Audit Module Details](audit_spark_job/README.md)

Audits run with every job to verify all data is accounted for with no record or data loss. While audits can't guarantee
that the job is bug free; it can show that no data loss has occurred. These can be categorized into two
distinct buckets:

1. _Basic_: steps that can be applied to any job
2. _Specific_: steps that are designed specifically to the current job and its data

### Logging

[Logging Module Details](logging_spark_job/README.md)

Logging is a part of each job. Instead of using print statements, logging should be used. It also allows the messages
to be included in normal code reporting systems. eg. Kibana, Graphana, etc.

By using logging, you can troubleshoot the job execution in root cause analysis.

### Unit Tests

[Unit Tests Module Details](unit_test_spark_job/README.md)

Unit tests allows tests to be completed against specific snippets of code. Verifying that specific pieces of code
is behaving as intended. These run at development and during CI/CD activities.

Failed unit tests will block deployments to the different environments.

### Self-healing / Restartable

[Self Healing Module Details](self_heal_spark_job/README.md)

Self-healing or restart-ability is the idea that when a job failes, you are able to restart the job without manual
intervention. Subsequent jobs will handle the data or job artifacts left over from the previous execution. 

read the records from the source that has changed since the last execution
clear out previous failed runs

### Single Execution

[Single Execution Module Details](single_execution_spark_job/README.md)

Single execution framework manages subsequent jobs to be skipped or delayed if the job doesn't allow for multiple
instances ot overlap. Ideally, you would build your jobs in a way that allows for multiple executions as this is easier
to code.

---

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

[Audit Module Details](audit_spark_job/README.md)

### logging_job

[Logging Module Details](logging_spark_job/README.md)

### unit_tests_job

[Unit Tests Module Details](unit_test_spark_job/README.md)

### self_healing_job

[Self Healing Module Details](self_heal_spark_job/README.md)

### single_execution_job

[Single Execution Module Details](single_execution_spark_job/README.md)

---

## Setup and Testing

### Pycharm Setup

---

## Related Docs
