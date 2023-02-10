```shell
project root
├── base_spark_job
├── audit_spark_job
│   └── CONSOLE.md ◄
├── logging_spark_job
├── unit_test_spark_job
├── self_head_spark_job
└── single_execution_spark_job
```

### Console Output

```shell
C:\Source\spark_training\venv\Scripts\python.exe C:/Source/spark_training/audit_spark_job/main.py 
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ ├ Topics                            ├ Code Complete Criteria                                                 ║
║ ┼───────────────────────────────────┼───────────────────────────────────                                     ║
║ │[■] Audits                         │[ ] Documentation                                                       ║
║ │    [■] Minimum                    │    [ ] README.md                                                       ║
║ │    [■] Job Specific               │    [ ] Docstrings                                                      ║
║ │[ ] Logging                        │    [ ] Code                                                            ║
║ │[ ] Unit Tests                     │    [ ] Handlers                                                        ║
║ │[ ] Self-Healing                   │[ ] No ide Warnings                                                     ║
║ │[ ] Single Execution               │[ ] No ide Errors                                                       ║
║ │                                   │[ ] ¹No Job Warnings                                                    ║
║ │                                   │[ ] No Job Errors                                                       ║
║ ¹ except accepted standard warnings. ie 'Setting default log level to "WARN".'                               ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
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
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ Pre Job Execution Info:                                                                                      ║
║                                                                                                              ║
║                Start Time ► 2023-02-09 15:12:03.871362                                                       ║
║ Time To Get Spark Context ► 0:00:14.398188                                                                   ║
║      Spark Application ID ► local-1675980736447                                                              ║
║            Spark App Name ► audit_spark_job                                                                  ║
║             Spark Version ► 3.2.2                                                                            ║
║                Spark User ► clarson                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ EXTRACT PHASE                                                                                                ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ EXTRACT 1 of 1                                                                                               ║
║                                                                                                              ║
║ Read Data From Source                                                                                        ║
║  ╠ This uses a self generated sample dataset                                                                 ║
║  ╠ The dataframe size or context makes no difference                                                         ║
║  ╚ except a column of string is needed to see the changes                                                    ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
root
 |-- id: integer (nullable = false)
 |-- username: string (nullable = false)
 |-- currency: string (nullable = false)
 |-- amount: integer (nullable = false)

+---+---------------+--------+------+
|id |username       |currency|amount|
+---+---------------+--------+------+
|0  |adennis        |GBP     |94198 |
|1  |zlandry        |GBP     |82473 |
|2  |danielolsen    |EUR     |4216  |
|3  |gdelacruz      |USD     |190580|
|4  |scottfranco    |EUR     |55074 |
|5  |dthomas        |USD     |178561|
|6  |dmorris        |GBP     |195913|
|7  |slane          |EUR     |8304  |
|8  |igreen         |USD     |179815|
|9  |jason43        |GBP     |23134 |
|10 |uhicks         |USD     |152513|
|11 |allenjuan      |GBP     |32733 |
|12 |fraziersarah   |USD     |49802 |
|13 |sandersadrian  |USD     |189603|
|14 |vcline         |EUR     |66733 |
|15 |bhall          |GBP     |105686|
|16 |stacy04        |GBP     |97489 |
|17 |amanda65       |EUR     |193042|
|18 |krobinson      |EUR     |189091|
|19 |vanessamcdowell|GBP     |165827|
+---+---------------+--------+------+

{
  "record_count": 20,
  "insert_count": null,
  "update_count": null,
  "delete_count": null,
  "no_change_count": null,
  "amount_sum": 2254787,
  "id_distinct": 20
}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ TRANSFORM PHASE                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ TRANSFORM 1 of 3                                                                                             ║
║                                                                                                              ║
║ Determine Record Change Type                                                                                 ║
║  ╠ Added a new column named `random_change_type` that is randomly                                            ║
║  ╚ generated by a UDF and is one of: new, update, delete, no_change.                                         ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
+---+---------------+--------+------+------------------+
|id |username       |currency|amount|random_change_type|
+---+---------------+--------+------+------------------+
|0  |adennis        |GBP     |94198 |null              |
|1  |zlandry        |GBP     |82473 |insert            |
|2  |danielolsen    |EUR     |4216  |null              |
|3  |gdelacruz      |USD     |190580|delete            |
|4  |scottfranco    |EUR     |55074 |nochange          |
|5  |dthomas        |USD     |178561|insert            |
|6  |dmorris        |GBP     |195913|no_change         |
|7  |slane          |EUR     |8304  |delete            |
|8  |igreen         |USD     |179815|no_change         |
|9  |jason43        |GBP     |23134 |no_change         |
|10 |uhicks         |USD     |152513|insert            |
|11 |allenjuan      |GBP     |32733 |nochange          |
|12 |fraziersarah   |USD     |49802 |no_change         |
|13 |sandersadrian  |USD     |189603|no_change         |
|14 |vcline         |EUR     |66733 |nochange          |
|15 |bhall          |GBP     |105686|insert            |
|16 |stacy04        |GBP     |97489 |delete            |
|17 |amanda65       |EUR     |193042|insert            |
|18 |krobinson      |EUR     |189091|insert            |
|19 |vanessamcdowell|GBP     |165827|no_change         |
+---+---------------+--------+------+------------------+

Input
{
  "record_count": 20,
  "insert_count": 6,
  "update_count": 0,
  "delete_count": 3,
  "no_change_count": 6,
  "amount_sum": 2254787,
  "id_distinct": 20
}
Output
{
  "record_count": null,
  "insert_count": null,
  "update_count": null,
  "delete_count": null,
  "no_change_count": null,
  "amount_sum": null,
  "id_distinct": null
}
Result
{
  "audit_passed": false,
  "audit_outcome": "Audit Failed Num Was Not Set",
  "num_audits_passed": 0,
  "num_audits_failed": 0,
  "audits_performed": {}
}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ TRANSFORM 2 of 3                                                                                             ║
║                                                                                                              ║
║ Calculate Grant Total For Amount                                                                             ║
║  ╠ Added a new column that uses a window function to add the                                                 ║
║  ╚ Grand Total for Amount for new, update and delete.                                                        ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
+---+-----------+--------+------+------------------+------------------+
|id |username   |currency|amount|random_change_type|amount_grand_total|
+---+-----------+--------+------+------------------+------------------+
|1  |zlandry    |GBP     |82473 |insert            |1352279           |
|3  |gdelacruz  |USD     |190580|delete            |1352279           |
|4  |scottfranco|EUR     |55074 |nochange          |1352279           |
|5  |dthomas    |USD     |178561|insert            |1352279           |
|7  |slane      |EUR     |8304  |delete            |1352279           |
|10 |uhicks     |USD     |152513|insert            |1352279           |
|11 |allenjuan  |GBP     |32733 |nochange          |1352279           |
|14 |vcline     |EUR     |66733 |nochange          |1352279           |
|15 |bhall      |GBP     |105686|insert            |1352279           |
|16 |stacy04    |GBP     |97489 |delete            |1352279           |
|17 |amanda65   |EUR     |193042|insert            |1352279           |
|18 |krobinson  |EUR     |189091|insert            |1352279           |
+---+-----------+--------+------+------------------+------------------+

╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ TRANSFORM 3 of 3                                                                                             ║
║                                                                                                              ║
║ Process Data Based On Change Type & Calculate Percent Of Total                                               ║
║  ╠ Updated (actually a new column of the same name) all column datatypes of string                           ║
║  ╠ to uppercase when the change type is `update`.                                                            ║
║  ╚ Added a new column that calculates the percent of total for amount                                        ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
+---+-----------+--------+------+------------------+-----------------------+
|id |username   |currency|amount|random_change_type|amount_percent_of_total|
+---+-----------+--------+------+------------------+-----------------------+
|1  |zlandry    |GBP     |82473 |insert            |0.06                   |
|3  |gdelacruz  |USD     |190580|delete            |0.14                   |
|4  |scottfranco|EUR     |55074 |nochange          |0.04                   |
|5  |dthomas    |USD     |178561|insert            |0.13                   |
|7  |slane      |EUR     |8304  |delete            |0.01                   |
|10 |uhicks     |USD     |152513|insert            |0.11                   |
|11 |allenjuan  |GBP     |32733 |nochange          |0.02                   |
|14 |vcline     |EUR     |66733 |nochange          |0.05                   |
|15 |bhall      |GBP     |105686|insert            |0.08                   |
|16 |stacy04    |GBP     |97489 |delete            |0.07                   |
|17 |amanda65   |EUR     |193042|insert            |0.14                   |
|18 |krobinson  |EUR     |189091|insert            |0.14                   |
+---+-----------+--------+------+------------------+-----------------------+

╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ LOAD PHASE                                                                                                   ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ LOAD 1 of 1                                                                                                  ║
║                                                                                                              ║
║ Write Data                                                                                                   ║
║  ╚ Writes the completed dataframe to the final destination                                                   ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ AUDIT PHASE                                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ AUDIT 1 of 1                                                                                                 ║
║                                                                                                              ║
║ Audit Data                                                                                                   ║
║  ╠  Audits the runtime values to verify the data is handled correctly                                        ║
║  ╠  Sends any alerts if audits fail                                                                          ║
║  ╚  If data is critical this handler will stop the job from running further                                  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
Input
{
  "record_count": 20,
  "insert_count": 6,
  "update_count": 0,
  "delete_count": 3,
  "no_change_count": 6,
  "amount_sum": 2254787,
  "id_distinct": 20
}
Output
{
  "record_count": 12,
  "insert_count": 6,
  "update_count": 0,
  "delete_count": 3,
  "no_change_count": 0,
  "amount_sum": 1352279,
  "id_distinct": 12,
  "amount_percent_of_total_sum": 0.9900000000000001
}
Result
{
  "audit_passed": false,
  "audit_outcome": "Audit(s) Failed",
  "num_audits_passed": 2,
  "num_audits_failed": 3,
  "audits_performed": {
    "Check Input Record Counts": false,
    "Check Output Record Counts Match Input Record Count": false,
    "Check Output Amount Percent Total Sum = 100%": false,
    "Check Output Has No Change Records": true,
    "Check Output Updated Records Are All Uppercase": true
  }
}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ Audit Result: Audit(s) Failed                                                                                ║
║ ‼SENDING ALERT‼                                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ Post Job Execution Info:                                                                                     ║
║                                                                                                              ║
║                Start Time ► 2023-02-09 15:12:03.871362                                                       ║
║              Job Duration ► 0:01:00.908579                                                                   ║
║                  End Time ► 2023-02-09 15:13:04.779941                                                       ║
║              Audit Result ► Audit(s) Failed                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

Process finished with exit code 0

```