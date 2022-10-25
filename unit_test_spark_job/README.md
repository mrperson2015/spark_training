`project root`<br>
`├── base_spark_job`<br>
`├── audit_spark_job`<br>
`├── logging_spark_job`<br>
`├── unit_test_spark_job ◄`<br>
`├── self_head_spark_job`<br>
`└── single_execution_spark_job`<br>

## Unit Tests

1. Check for dirty data in transform
    1. Test for edge cases (null, upper case, not in (delete, update, insert, no_change))
    2. Test result of strings are uppercase for strings