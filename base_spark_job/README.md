# Spark Training Project

[[_TOC_]]

# Topics

### Architecture

* [ ] KISS
    * Keep It Stupid Simple
* [ ] Peer Review
* [ ] Documentation
    * [ ] Lucid Chart
    * [ ] Wiki

### PLANNING

* [ ] User Stories
* [ ] Tasks Have Time Estimates
* [ ] Peer Review
* [ ] ¹Delivery Date
    * ¹ (`estimated start date` + `total estimated task time`) * π

### IMPLEMENTATION

* [ ] Documentation
    * [ ] README.md
    * [ ] Docstrings
    * [ ] Code
    * [ ] Handlers
* [ ] No ide Warnings
* [ ] No ide Errors
* [ ] ²No Job Warnings
    * ² except accepted standard warnings
    * ie: 'Setting default log level to \"WARN\".'
* [ ] No Job Errors
* [ ] Peer Review
* [ ] Audits
    * [ ] Minimum
    * [ ] Job Specific
* [ ] Logging
* [ ] Unit Tests
* [ ] Change Log
* [ ] Copyright

| → Architecture    | Planning                        | Implementation       |
|-------------------|---------------------------------|----------------------|
| [■] KISS          | [ ] User Storie(s)              | [■] Documentation    |
| [ ] Peer Review   | [ ] Task(s) Have Time Estimates | [ ] - README.md      |
| [ ] Documentation | [ ] Peer Review                 | [■] - Docstrings     |
| [ ] Lucid Chart   | [ ] ¹Delivery Date              | [■] - Code           |
| [ ] Wiki          | [ ] Test Plan                   | [■] - Handlers       |
|                   | [ ] Deploy Plan                 | [■] No IDE Warnings  |
|                   | [ ] Support Plan                | [■] No IDE Errors    |
|                   | [ ]                             | [■] ²No Job Warnings |
|                   | [ ]                             | [■] No Job Errors    |
|                   | [ ]                             | [ ] Peer Review      |
|                   | [ ]                             | [ ] Audits           |
|                   | [ ]                             | [ ] - Minimum        |
|                   | [ ]                             | [ ] - Job Specific   |
|                   | [ ]                             | [ ] Logging          |
|                   | [ ]                             | [ ] Unit Tests       |
|                   | [ ]                             | [ ] Change Log       |
|                   |                                 | [ ] Copyright        |
|                   |                                 | [ ] Black Formatter  |
¹ `estimated start date` + (`total estimated task time` * π) 

² except accepted standard warnings. (ie 'Setting default log level to "WARN".')

# Modules
## base_spark_job

## 

# Setup and Testing
Quick setup guide on how to execute the Job via Pycharm or through a Spark Submit
command.

## Pycharm Setup
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
   
# Related Docs
[Import DMS Document Data FSD](https://lucid.app/lucidchart/77185a06-1e34-4151-b490-b68678f3214e/edit?invitationId=inv_bded16c3-287c-4dbe-bf7d-597ab43e7bfa&page=0_0#) \
[Imports DMS Document Data Repo](https://dev.azure.com/berkadiadevops/Polaris/_git/data-pipeline-databridge-import-dms)