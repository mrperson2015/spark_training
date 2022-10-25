"""
    Generates the data for this training job. Uses the training utils project.
"""

# Standard Library Imports <- This is not required but useful to separate out imports
from helper_printer import print_header
from pyspark.sql import SparkSession, DataFrame
import helper_spark_data_generator as sdg


def job_extract_phase(spark_session: SparkSession, rows: int) -> DataFrame:
    """
    Generates the data for this training job. Uses the training utils project.

    Examples:
        job_extract_phase(spark_session=spark, rows=20)

    Args:
        spark_session (SparkSession): The SparkSession to use in reading the source data
        rows (int): The number of rows to generate for this job

    Returns:
        DataFrame
    """
    print_header("EXTRACT 1 of 1\n"
                 "\n"
                 "Read Data From Source\n"
                 " ╠ This uses a self generated sample dataset\n"
                 " ╠ The dataframe size or context makes no difference\n"
                 " ╚ except a column of string is needed to see the changes")
    _input_df = sdg.transaction_df(spark_session=spark_session, record_count=rows)
    _input_df.printSchema()
    _input_df.show(truncate=False)
    return _input_df


if __name__ == '__main__':
    import helper_spark

    spark = helper_spark.get_spark(application_name="handle_input_data")
    job_extract_phase(spark_session=spark, rows=20)
