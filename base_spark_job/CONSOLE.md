```shell
project root
├── base_spark_job
│   ├── CONSOLE.md ◄
│   └── MISTAKES.md
├── audit_spark_job
├── logging_spark_job
├── unit_test_spark_job
├── self_heal_spark_job
└── single_execution_spark_job
```

### Console Output

```shell
C:\Source\spark_training\venv\Scripts\python.exe C:/Source/spark_training/base_spark_job/main.py 
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ ├ Topics                            ├ Code Complete Criteria                                                 ║
║ ┼───────────────────────────────────┼───────────────────────────────────                                     ║
║ │[ ] Audits                         │[■] Documentation                                                       ║
║ │    [ ] Minimum                    │    [ ] README.md                                                       ║
║ │    [ ] Job Specific               │    [■] Docstrings                                                      ║
║ │[ ] Logging                        │    [■] Code                                                            ║
║ │[ ] Unit Tests                     │    [■] Handlers                                                        ║
║ │[ ] Self-Healing                   │[■] No ide Warnings                                                     ║
║ │[ ] Single Execution               │[■] No ide Errors                                                       ║
║ │                                   │[■] ¹No Job Warnings                                                    ║
║ │                                   │[■] No Job Errors                                                       ║
║ ¹ except accepted standard warnings. ie 'Setting default log level to "WARN".'                               ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
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
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ Pre Job Execution Info:                                                                                      ║
║                                                                                                              ║
║                Start Time ► 2022-10-26 10:22:50.127811                                                       ║
║ Time To Get Spark Context ► 0:00:16.814267                                                                   ║
║      Spark Application ID ► local-1666801382144                                                              ║
║            Spark App Name ► base_spark_job                                                                   ║
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

+---+--------------+--------+------+
|id |username      |currency|amount|
+---+--------------+--------+------+
|0  |batesalexis   |EUR     |188256|
|1  |stevenbuchanan|GBP     |49163 |
|2  |padillaalicia |USD     |47668 |
|3  |holdentyler   |GBP     |70041 |
|4  |annahoward    |EUR     |63915 |
|5  |stephanie46   |USD     |54800 |
|6  |johnsonzachary|USD     |181538|
|7  |joshuabaker   |USD     |188690|
|8  |steven58      |USD     |23052 |
|9  |austin36      |EUR     |80461 |
|10 |brianwilson   |EUR     |8773  |
|11 |osbornjamie   |USD     |6669  |
|12 |xjackson      |USD     |101514|
|13 |kimberlynorris|USD     |148985|
|14 |dsteele       |EUR     |24612 |
|15 |bcruz         |GBP     |176736|
|16 |stevendoyle   |USD     |36209 |
|17 |kjackson      |GBP     |97529 |
|18 |melissa52     |GBP     |192096|
|19 |shill         |GBP     |168052|
+---+--------------+--------+------+

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
+---+--------------+--------+------+------------------+
|id |username      |currency|amount|random_change_type|
+---+--------------+--------+------+------------------+
|0  |batesalexis   |EUR     |188256|update            |
|1  |stevenbuchanan|GBP     |49163 |no_change         |
|2  |padillaalicia |USD     |47668 |no_change         |
|3  |holdentyler   |GBP     |70041 |no_change         |
|4  |annahoward    |EUR     |63915 |update            |
|5  |stephanie46   |USD     |54800 |update            |
|6  |johnsonzachary|USD     |181538|insert            |
|7  |joshuabaker   |USD     |188690|update            |
|8  |steven58      |USD     |23052 |nochange          |
|9  |austin36      |EUR     |80461 |insert            |
|10 |brianwilson   |EUR     |8773  |nochange          |
|11 |osbornjamie   |USD     |6669  |nochange          |
|12 |xjackson      |USD     |101514|update            |
|13 |kimberlynorris|USD     |148985|no_change         |
|14 |dsteele       |EUR     |24612 |insert            |
|15 |bcruz         |GBP     |176736|no_change         |
|16 |stevendoyle   |USD     |36209 |insert            |
|17 |kjackson      |GBP     |97529 |update            |
|18 |melissa52     |GBP     |192096|delete            |
|19 |shill         |GBP     |168052|insert            |
+---+--------------+--------+------+------------------+

╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ TRANSFORM 2 of 3                                                                                             ║
║                                                                                                              ║
║ Calculate Grant Total For Amount                                                                             ║
║  ╠ Added a new column that uses a window function to add the                                                 ║
║  ╚ Grand Total for Amount for new, update and delete.                                                        ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
+---+--------------+--------+------+------------------+------------------+
|id |username      |currency|amount|random_change_type|amount_grand_total|
+---+--------------+--------+------+------------------+------------------+
|0  |batesalexis   |EUR     |188256|update            |1416166           |
|4  |annahoward    |EUR     |63915 |update            |1416166           |
|5  |stephanie46   |USD     |54800 |update            |1416166           |
|6  |johnsonzachary|USD     |181538|insert            |1416166           |
|7  |joshuabaker   |USD     |188690|update            |1416166           |
|8  |steven58      |USD     |23052 |nochange          |1416166           |
|9  |austin36      |EUR     |80461 |insert            |1416166           |
|10 |brianwilson   |EUR     |8773  |nochange          |1416166           |
|11 |osbornjamie   |USD     |6669  |nochange          |1416166           |
|12 |xjackson      |USD     |101514|update            |1416166           |
|14 |dsteele       |EUR     |24612 |insert            |1416166           |
|16 |stevendoyle   |USD     |36209 |insert            |1416166           |
|17 |kjackson      |GBP     |97529 |update            |1416166           |
|18 |melissa52     |GBP     |192096|delete            |1416166           |
|19 |shill         |GBP     |168052|insert            |1416166           |
+---+--------------+--------+------+------------------+------------------+

╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ TRANSFORM 3 of 3                                                                                             ║
║                                                                                                              ║
║ Process Data Based On Change Type & Calculate Percent Of Total                                               ║
║  ╠ Updated (actually a new column of the same name) all column datatypes of string                           ║
║  ╠ to uppercase when the change type is `update`.                                                            ║
║  ╚ Added a new column that calculates the percent of total for amount                                        ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
+---+--------------+--------+------+------------------+-----------------------+
|id |username      |currency|amount|random_change_type|amount_percent_of_total|
+---+--------------+--------+------+------------------+-----------------------+
|0  |BATESALEXIS   |EUR     |188256|UPDATE            |0.13                   |
|4  |ANNAHOWARD    |EUR     |63915 |UPDATE            |0.05                   |
|5  |STEPHANIE46   |USD     |54800 |UPDATE            |0.04                   |
|6  |johnsonzachary|USD     |181538|insert            |0.13                   |
|7  |JOSHUABAKER   |USD     |188690|UPDATE            |0.13                   |
|8  |steven58      |USD     |23052 |nochange          |0.02                   |
|9  |austin36      |EUR     |80461 |insert            |0.06                   |
|10 |brianwilson   |EUR     |8773  |nochange          |0.01                   |
|11 |osbornjamie   |USD     |6669  |nochange          |0.0                    |
|12 |XJACKSON      |USD     |101514|UPDATE            |0.07                   |
|14 |dsteele       |EUR     |24612 |insert            |0.02                   |
|16 |stevendoyle   |USD     |36209 |insert            |0.03                   |
|17 |KJACKSON      |GBP     |97529 |UPDATE            |0.07                   |
|18 |melissa52     |GBP     |192096|delete            |0.14                   |
|19 |shill         |GBP     |168052|insert            |0.12                   |
+---+--------------+--------+------+------------------+-----------------------+

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
║ Post Job Execution Info:                                                                                     ║
║                                                                                                              ║
║                Start Time ► 2022-10-26 10:22:50.127811                                                       ║
║              Job Duration ► 0:00:38.837322                                                                   ║
║                  End Time ► 2022-10-26 10:23:28.965133                                                       ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

Process finished with exit code 0
```