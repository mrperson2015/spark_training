```shell
project root
├── base_spark_job
├── audit_spark_job ◄
├── logging_spark_job
├── unit_test_spark_job
├── self_heal_spark_job
└── single_execution_spark_job
```

# Audit Spark Job

[[_TOC_]]

## Purpose

---

## Job

### Requirements
* **Base Spark Job**
  1. Uppercase string values for updated records
  2. Calculate Percent of Total for each record where record change is new, update, or delete
  3. Exclude no_change record types from the output
* **Audit Spark Job**
  1. Base Spark Job Requirements Met
  2. Every record is accounted for
  3. Amount is accounted for
  4. Total Percent of Total is accurate

### Steps

### Data Flow Diagram

```shell
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  2 AUDIT JOB                                                                                                 ║
║                                                                                                              ║
║           ┌             ┌──────┐                                                                             ║
║           │             │source│                                                                             ║
║ EXTRACT───┤             └──╥───┘                                                                             ║
║           │            ╔═══╩════╗                                                                            ║
║           │            ║  READ  ║                                                                            ║
║           │            ╚═══╦════╝                     ┐─────────────┌                                        ║
║           │                ╠══════════════════════════╡ INPUT AUDIT │                                        ║
║           │                ║                          │    VALUES   │                                        ║
║           └                ║                          ┘────╥────────└                                        ║
║           ┌          ╔═════╩═══════╗                       ║                                                 ║
║           │          ║ CHANGE TYPE ║                       ║                                                 ║
║           │          ╚══════╦══════╝                  ┐────╨────────┌                                        ║
║           │                 ╠═════════════════════════╡ INPUT AUDIT │                                        ║
║           │     ╔══════╦════╩═══╦════════╗            │    VALUES   │                                        ║
║           │ ┌───╨──┐┌──╨───┐┌───╨──┐┌────╨────┐       ┘────╥────────└                                        ║
║           │ │delete││update││insert││no_change│            ║                                                 ║
║ TRANSFORM─┤ └───╥──┘└───╥──┘└───╥──┘└─────────┘            ║                                                 ║
║           │     ║ ╔═════╩═════╗ ║                          ║                                                 ║
║           │     ║ ║ UPPERCASE ║ ║                          ║                                                 ║
║           │     ║ ║  STRINGS  ║ ║                          ║                                                 ║
║           │     ║ ╚═════╦═════╝ ║                          ║                                                 ║
║           │     ╚═══════╩═══╦═══╝                          ║                                                 ║
║           │            ╔════╩═════╗                        ║                                                 ║
║           │            ║ PERCENT  ║                        ║                                                 ║
║           │            ║ OF TOTAL ║                        ║                                                 ║
║           └            ╚════╦═════╝                        ║                                                 ║
║           ┌             ╔═══╩═══╗                          ║                                                 ║
║           │             ║ WRITE ║                          ║                                                 ║
║ LOAD──────┤             ╚═══╦═══╝                          ║                                                 ║
║           │           ┌─────╨─────┐                        ║                                                 ║
║           │           │destination│                        ║                                                 ║
║           └           └─────╥─────┘                        ║                                                 ║
║           ┌             ╔═══╩════╗                         ║                                                 ║
║           │             ║  READ  ║                         ║                                                 ║
║           │             ╚═══╦════╝                         ║                                                 ║
║           │           ┐─────╨────────┌                     ║                                                 ║
║           │           │ OUTPUT AUDIT │                     ║                                                 ║
║           │           │    VALUES    │                     ║                                                 ║
║           │           ┘───────────╥──└   ╔═════════════════╝                                                 ║
║           │                     ┐─╨──────╨──┌                                                                ║
║           │                     │ RUN AUDIT │                                                                ║
║ AUDIT─────┤                     ┘─╥───────╥─└                                                                ║
║           │                   ╔═══╩═══╗╔══╩════╗                                                             ║
║           │                   ║ WRITE ║║ ALERT ║                                                             ║
║           │                   ╚═══╦═══╝╚═══════╝                                                             ║
║           │                 ┌─────╨─────┐                                                                    ║
║           │                 │destination│                                                                    ║
║           └                 └───────────┘                                                                    ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  LEGEND                                        DATA╗     ┌─────┐ ┐─────┌ ┼─────┼ ╔════════╗ ╗═════╔ ╬═════╬  ║
║                                                ╔═══╬══╦═ │state│ │AUDIT│ │     │ ║ ACTION ║ ║     ║ ║     ║  ║
║                                                    FLOW  └─────┘ ┘─────└ ┼─────┼ ╚════════╝ ╝═════╚ ╬═════╬  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
```

### Related Docs

[Console Job Output](CONSOLE.md)

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
