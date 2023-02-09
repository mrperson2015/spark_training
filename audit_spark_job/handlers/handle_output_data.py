"""
    This module handles the output for this training spark job.
"""

# Standard Library Imports <- This is not required but useful to separate out imports
from helper_printer import print_header
from pyspark.sql import DataFrame


def job_load_phase(dataframe: DataFrame, output_path: str) -> None:
    """
    Writes the data for this training job to the final destination.

    Examples:
        job_load_phase(dataframe=process_df, output_path="tests/output/data/audit_spark_job")

    Args:
        dataframe (DataFrame): Input DataFrame to write
        output_path (str): Where to write to

    Returns:
        Void
    """
    print_header("LOAD 1 of 1\n"
                 "\n"
                 "Write Data\n"
                 " ╚ Writes the completed dataframe to the final destination")
    dataframe \
        .write \
        .mode("overwrite") \
        .parquet(output_path)
