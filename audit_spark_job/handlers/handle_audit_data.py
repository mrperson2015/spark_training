"""
    This module handles the audits for this training spark job.
"""

# Standard Library Imports <- This is not required but useful to separate out imports
from helper_audit import audit
from helper_printer import print_header
from pyspark.sql import SparkSession
import pyspark.sql.functions as F


def job_audit_phase(spark_session: SparkSession, output_path: str, audit_output_path: str):
    """
    Collects output audit values. Perform audits to verify the job is handling the data as required in the project
    requirements. Populates the audit result data. Writes the audit data for this training job to the final
    destination.

    Examples:
        job_audit_phase(spark_session=spark,
                         output_path="tests/output/data/audit_spark_job",
                         audit_output_path="tests/output/log/audit/audit_spark_job")

    Args:
        spark_session (SparkSession): Spark context to read the output with
        output_path (str): Where to the data for this job was written to in the load phase
        audit_output_path (str): Where to write the audit data to

    Returns:
        Void
    """
    print_header("AUDIT 1 of 1\n"
                 "\n"
                 "Audit Data\n"
                 " ╠  Audits the runtime values to verify the data is handled correctly\n"
                 " ╠  Sends any alerts if audits fail\n"
                 " ╚  If data is critical this handler will stop the job from running further")

    # READ WRITTEN DATA
    _output_df = spark_session \
        .read \
        .parquet(output_path)

    # COLLECT OUTPUT AUDIT VALUES
    audit_output_df = _output_df \
        .select(F.col("id"),
                F.col("amount"),
                F.col("random_change_type"),
                F.col("amount_percent_of_total"),
                F.when(F.lower(F.col("random_change_type")) == F.lit("delete"), F.lit(1))
                .otherwise(F.lit(0)).alias("delete"),
                F.when(F.col("random_change_type") == F.upper(F.lit("UPDATE")), F.lit(1))
                .otherwise(F.lit(0)).alias("update"),
                F.when(F.lower(F.col("random_change_type")) == F.lit("insert"), F.lit(1))
                .otherwise(F.lit(0)).alias("insert"),
                F.when(F.lower(F.col("random_change_type")) == F.lit("no_change"), F.lit(1))
                .otherwise(F.lit(0)).alias("no_change")) \
        .agg(F.count("id").alias("record_count"),
             F.sum("amount").alias("amount_sum"),
             F.countDistinct("id").alias("id_distinct"),
             F.sum("amount_percent_of_total").alias("amount_percent_of_total_sum"),
             F.sum(F.col("delete")).alias("delete_count"),
             F.sum(F.col("update")).alias("update_count"),
             F.sum(F.col("insert")).alias("insert_count"),
             F.sum(F.col("no_change")).alias("no_change_count"))
    audit.output.populate_from_df(audit_output_df)

    # PERFORM AUDITS
    # TODO: do we want to handle this here or add the functionality to helper_audit?
    _audits = {}
    # audit 1
    audit_input_record_count = audit.input.get_record_count_value() == (
            audit.input.get_delete_count_audit_value() +
            audit.input.get_update_count_audit_value() +
            audit.input.get_insert_count_audit_value() +
            audit.input.get_no_change_count_audit_value())
    _audits.update({"Check Input Record Counts": audit_input_record_count})
    # audit 2
    audit_output_record_count = audit.output.get_record_count_value() == (
            audit.output.get_delete_count_audit_value() +
            audit.output.get_update_count_audit_value() +
            audit.output.get_insert_count_audit_value() +
            audit.input.get_no_change_count_audit_value())
    _audits.update({"Check Output Record Counts Match `Input Record` Count": audit_output_record_count})
    # audit 3
    audit_output_pot = audit.output.get_audit_value(key="amount_percent_of_total_sum") == 1
    _audits.update({"Check Output Amount Percent Total Sum = 100%": audit_output_pot})
    # audit 4
    audit_output_no_change = audit.output.get_no_change_count_audit_value() == 0
    _audits.update({"Check Output Doesn't contain `No Change` Records": audit_output_no_change})
    # audit 5
    audit_updated_uppercase = audit.input.get_update_count_audit_value() == audit.output.get_update_count_audit_value()
    _audits.update({"Check Output Updated Records Are All Uppercase": audit_updated_uppercase})

    audit.result.set_audits_performed(audit_dict=_audits)

    audit.print()

    # WRITE AUDIT VALUES
    audit.get_dataframe() \
        .write \
        .mode("overwrite") \
        .parquet(audit_output_path)

    if audit.result.get_audit_passed():
        print_header(f"Audit Result: ☺☺{audit.result.get_audit_outcome()}☺☺")
    else:
        print_header(f"Audit Result: {audit.result.get_audit_outcome()}\n"
                     "‼SENDING ALERT‼")
