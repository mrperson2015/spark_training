"""
    This module builds on the base_spark_job module. The focus of this module is to show the pattern to add audits
    to spark jobs. This pattern actually applies to any data movement job. When done correctly, you can guarantee
    all files have been handled and no record has been lost. This doesn't typically guarantee the data quality is
    perfect.
"""

# Standard Library Imports <- This is not required but useful to separate out imports
import datetime
from helper_printer import print_header
from helper_spark import get_spark
from audit_spark_job.handlers.handle_job_info import job_diagram
from audit_spark_job.handlers.handle_run_info import job_pre_run_info, job_post_run_info
from audit_spark_job.handlers.handle_input_data import job_extract_phase
from audit_spark_job.handlers.handle_transform_data import job_transform_phase
from audit_spark_job.handlers.handle_audit_data import job_audit_phase
from audit_spark_job.handlers.handle_output_data import job_load_phase

if __name__ == '__main__':
    print_header(
        "├ Topics                            ├ Code Complete Criteria            \n"
        "┼───────────────────────────────────┼───────────────────────────────────\n"
        "│[■] Audits                         │[ ] Documentation                  \n"
        "│    [■] Minimum                    │    [ ] README.md                  \n"
        "│    [■] Job Specific               │    [ ] Docstrings                 \n"
        "│[ ] Logging                        │    [ ] Code                       \n"
        "│[ ] Unit Tests                     │    [ ] Handlers                   \n"
        "│[ ] Self-Healing                   │[ ] No ide Warnings                \n"
        "│[ ] Single Execution               │[ ] No ide Errors                  \n"
        "│                                   │[ ] ¹No Job Warnings               \n"
        "│                                   │[ ] No Job Errors                  \n"
        "¹ except accepted standard warnings. ie 'Setting default log level to \"WARN\".'"
    )

    job_start_time = datetime.datetime.now()
    job_diagram()

    # Get Spark Session
    spark = get_spark(application_name="audit_spark_job")

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
    job_load_phase(dataframe=process_df, output_path="tests/output/data/audit_spark_job")

    print_header("AUDIT PHASE")
    #  - Audit the data to verify the job is processing/handling all records correctly
    #  - Every record is accounted for
    #  - Amount is accounted for
    #  - Total Percent of Total is accurate
    audit_result = job_audit_phase(spark_session=spark,
                                   output_path="tests/output/data/audit_spark_job",
                                   audit_output_path="tests/output/log/audit/audit_spark_job")

    # Print Job Run Info
    job_post_run_info(start_time=job_start_time, audit_result=audit_result)
