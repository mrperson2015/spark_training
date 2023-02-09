"""
    Generates the data for this training job. Uses the training utils project.
"""

# Standard Library Imports <- This is not required but useful to separate out imports
from helper_audit import audit
from helper_printer import print_header
from helper_spark import *


def job_pre_run_info(start_time: datetime.datetime, spark_session: SparkSession) -> None:
    """
    Prints out helpful PySpark job info. This is intended for the start of your PySpark job.

    Examples:
        job_pre_run_info(spark_session=spark, start_time=job_start_time)

    Args:
        start_time (datetime): The start time of the job
        spark_session (SparkSession): The SparkSession to retrieve info from

    Returns:
        Void
    """
    print_header(f"Pre Job Execution Info:\n"
                 f"\n"
                 f"               Start Time ► {start_time}\n"
                 f"Time To Get Spark Context ► {datetime.datetime.now() - start_time}\n"
                 f"     Spark Application ID ► {spark_session.sparkContext.applicationId}\n"
                 f"           Spark App Name ► {spark_session.sparkContext.appName}\n"
                 f"            Spark Version ► {spark_session.version}\n"
                 f"               Spark User ► {spark_session.sparkContext.sparkUser()}")
    return None


def job_post_run_info(start_time: datetime.datetime, audit_result) -> None:
    """
    Prints out helpful PySpark job info. This is intended for the end of your PySpark job.

    Examples:
        job_post_run_info(start_time=job_start_time)

    Args:
        start_time (datetime): The start time of the job

    Returns:
        Void
    """
    print_header(f"Post Job Execution Info:\n"
                 f"\n"
                 f"               Start Time ► {start_time}\n"
                 f"             Job Duration ► {datetime.datetime.now() - start_time}\n"
                 f"                 End Time ► {datetime.datetime.now()}\n"
                 f"             Audit Result ► {audit.result.get_audit_outcome()}\n")
    return None


if __name__ == '__main__':
    import helper_spark

    job_start_time = datetime.datetime.now()

    spark = helper_spark.get_spark(application_name="handle_input_data")
    job_pre_run_info(spark_session=spark, start_time=job_start_time)
    job_post_run_info(start_time=job_start_time)
