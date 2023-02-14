```shell
project root
├── base_spark_job
│   ├── CONSOLE.md
│   └── MISTAKES.md ◄
├── audit_spark_job
├── logging_spark_job
├── unit_test_spark_job
├── self_heal_spark_job
└── single_execution_spark_job
```

# Base Spark Job Mistakes

A number of mistakes have been made in this job. If you cant tell, this is on purpose. This job, at face value, runs
correctly. While under the surface, mistakes abound. Some of these mistakes aren't visible on each execution. It is
based on the random data generated.

The topics covered in this training will show how each would have caught these mistakes before going to production...
or allow troubleshooting after deploy.

## Mistakes
1. Round percent_of_total makes the total potentially greater or lesser than 1 (ie 1.01)
2. Filtering out the no_change records causes the percent_of_total to be <= 1
3. Filtering doesn't handle the dirty record_change_type data of nochange and NULL
4. Excluded the no_change records too early
5. Unable to troubleshoot job execution for job failure or data quality issues
6. Using `print` statements instead of logging