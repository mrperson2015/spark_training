```shell
project root
├── base_spark_job ◄
├── audit_spark_job
├── logging_spark_job
├── unit_test_spark_job
├── self_head_spark_job
└── single_execution_spark_job
```

# Base Spark Job

[[_TOC_]]

## Purpose

This job (base_spark_job) is the base code that all others start with. It is a simple job that meets very little
requirements. It runs and runs without any execution errors. The other jobs use this base PySpark job with the added
topic code added.

You will want to run and understand this base spark job code well before jumping into the other jobs. This will help
you to understand the specific code and purpose of each topic.

---

## Job

### Requirements

1. Uppercase string values for updated records
2. Calculate Percent of Total for each record where record change is new, update, or delete
3. Exclude no_change record types from the output

### Steps

- EXTRACT PHASE
    1. Read Data From Source
- TRANSFORM PHASE
    1. Determine Record Change Type
    2. Calculate Grant Total For Amount
    3. Process Data Based On Change Type & Calculate Percent Of Total
- LOAD PHASE
    1. Write Data

### Data Flow Diagram

```shell
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  1 BASIC JOB                                                                                                 ║
║                                                                                                              ║
║           ┌             ┌──────┐                                                                             ║
║           │             │source│                                                                             ║
║ EXTRACT───┤             └──╥───┘                                                                             ║
║           │            ╔═══╩════╗                                                                            ║
║           │            ║  READ  ║                                                                            ║
║           └            ╚═══╦════╝                                                                            ║
║           ┌          ╔═════╩═══════╗                                                                         ║
║           │          ║ CHANGE TYPE ║                                                                         ║
║           │          ╚══════╦══════╝                                                                         ║
║           │     ╔══════╦════╩═══╦════════╗                                                                   ║
║           │ ┌───╨──┐┌──╨───┐┌───╨──┐┌────╨────┐                                                              ║
║           │ │delete││update││insert││no_change│                                                              ║
║ TRANSFORM─┤ └───╥──┘└───╥──┘└───╥──┘└─────────┘                                                              ║
║           │     ║ ╔═════╩═════╗ ║                                                                            ║
║           │     ║ ║ UPPERCASE ║ ║                                                                            ║
║           │     ║ ║  STRINGS  ║ ║                                                                            ║
║           │     ║ ╚═════╦═════╝ ║                                                                            ║
║           │     ╚═══════╩═══╦═══╝                                                                            ║
║           │            ╔════╩═════╗                                                                          ║
║           │            ║ PERCENT  ║                                                                          ║
║           │            ║ OF TOTAL ║                                                                          ║
║           └            ╚════╦═════╝                                                                          ║
║           ┌             ╔═══╩═══╗                                                                            ║
║           │             ║ WRITE ║                                                                            ║
║ LOAD──────┤             ╚═══╦═══╝                                                                            ║
║           │           ┌─────╨─────┐                                                                          ║
║           │           │destination│                                                                          ║
║           └           └───────────┘                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  LEGEND                                        DATA╗     ┌─────┐ ┐─────┌ ┼─────┼ ╔════════╗ ╗═════╔ ╬═════╬  ║
║                                                ╔═══╬══╦═ │state│ │AUDIT│ │     │ ║ ACTION ║ ║     ║ ║     ║  ║
║                                                    FLOW  └─────┘ ┘─────└ ┼─────┼ ╚════════╝ ╝═════╚ ╬═════╬  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
```

### Related Docs

* [Console Job Output](CONSOLE.md)
* [Job Mistakes](MISTAKES.md)

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