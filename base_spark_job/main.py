"""
    This is the first module of many for PySpark training. The other training jobs will build upon this one.
"""

# Standard Library Imports <- This is not required but useful to separate out imports
import datetime
from helper_printer import print_header
from helper_spark import get_spark
from base_spark_job.handlers.handle_job_info import job_diagram
from base_spark_job.handlers.handle_run_info import job_pre_run_info, job_post_run_info
from base_spark_job.handlers.handle_input_data import job_extract_phase
from base_spark_job.handlers.handle_transaction_data import job_transform_phase
from base_spark_job.handlers.handle_output_data import job_load_phase

if __name__ == '__main__':
    print_header(
        "├ Topics                            ├ Code Complete Criteria            \n"
        "┼───────────────────────────────────┼───────────────────────────────────\n"
        "│[ ] Audits                         │[■] Documentation                  \n"
        "│    [ ] Minimum                    │    [ ] README.md                  \n"
        "│    [ ] Job Specific               │    [■] Docstrings                 \n"
        "│[ ] Logging                        │    [■] Code                       \n"
        "│[ ] Unit Tests                     │    [■] Handlers                   \n"
        "│                                   │[■] No ide Warnings                \n"
        "│                                   │[■] No ide Errors                  \n"
        "│                                   │[■] ¹No Job Warnings               \n"
        "│                                   │[■] No Job Errors                  \n"
        "¹ except accepted standard warnings. ie 'Setting default log level to \"WARN\".'"
    )

    # MISTAKES
    #  - Round percent_of_total makes the total potentially greater or lesser than 1 (ie 1.01)
    #  - Filtering out the no_change records causes the percent_of_total to be <= 1
    #  - Filtering doesn't handle the dirty record_change_type data of nochange and NULL
    #  - Unable to troubleshoot job execution for job failure or data quality issues

    job_start_time = datetime.datetime.now()
    job_diagram()

    # Get Spark Session
    spark = get_spark(application_name="base_spark_job")

    # Print Job Run Info
    job_pre_run_info(start_time=job_start_time, spark_session=spark)

    print_header("EXTRACT PHASE")
    #  - Extract/Read the data for this job from the source
    #  - Usually based on prior job run time (not covered in this training job)
    #  - Typically a direct read from the source w/ no transformations
    input_df = job_extract_phase(spark_session=spark, rows=20)

    print_header("TRANSFORM PHASE")
    #  - Transform the data as necessary for the job requirements
    #  - This job wants all records that have a datatype of 'string'
    #    to be transformed to uppercase where the change type is 'update'
    process_df = job_transform_phase(dataframe=input_df)

    print_header("LOAD PHASE")
    # Load Phase
    #  - Load/Write the data to the final destination
    job_load_phase(dataframe=process_df, output_path="output/base_spark_job")

    # Print Job Run Info
    job_post_run_info(start_time=job_start_time)
