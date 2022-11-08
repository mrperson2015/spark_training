# Tested Versions

| Key               | Value                             |
|-------------------|-----------------------------------|
| OS                | Win 10, Win 11, Ubuntu 20.04      |
| IDE               | PyCharm 2022.1, 2022.2            |
| Python            | 3.8, 3.10                         |
| JDK               | openJDK 1.8.0-262, Java 1.8.0_351 |
| PySpark           | 3.0.2, 3.0.3, 3.2.2               |
| randomCoordinates | 0.1.7                             |
| Faker             | 15.1.1, 15.1.2                    |

# Assumptions

It is assumed that the user of these instructions has some knowledge of Spark/PySpark, Python, Python Packages, Python
Interpreters, PyCharm, and Java. This setup guide is a summary of steps needed to be taken rather than a comprehensive
step-by-step guide.

# Install & Configure

These projects will largely run the same in Windows and Ubuntu once you have the OS dependencies installed and
configured. More system dependencies exist in the Windows OS making it longer to get up and running. These steps have
been included below.

The steps below were generated from new a new virtual machine for Windows 11 and Ubuntu 20 using VMware Workstation.
General steps follow this pattern:

1. Install OS ([Windows](#Windows), [Ubuntu](#Ubuntu))
2. Install [JetBrains PyCharm](https://www.jetbrains.com/pycharm/) - The IDE to run the code in
3. Install [Git](https://git-scm.com/) - The version control tool of choice
4. Install [Python](https://www.python.org/) 3 - The language the PySpark jobs are written in
5. Install [JDK](https://www.oracle.com/java/) - The engine that Spark runs in
6. Install OS specific items
7. Clone repositories for `training_utils` and `spark_training` - The two projects used in this PySpark training project
8. Open and configure `spark_training` job in PyCharm - Setup PyCharm with the required Python packages
9. Run [PySpark](https://spark.apache.org/) job

## Windows

<details><summary>Instructions for Windows</summary>

1. Install Windows
    - 11 Version
    - UEFI Secure Boot Firmware Type
    - 16 GB Memory
    - 2 Processor @ 4 Cores each (8 total processor cores)
    - 60 GB NVMe disk (split, unallocated)
    - NAT Network Adapter
    - Handle Trusted Platform Module (TPM) Requirement (pick one):
        - [Enable TPM in VMware](https://pureinfotech.com/enable-tpm-secure-boot-vmware-install-windows-11/)
        - [Disable TPM in Windows](https://www.tomshardware.com/how-to/bypass-windows-11-tpm-requirement)
2. Install [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/)
    1. Install [PyCharm](https://www.jetbrains.com/pycharm/) 2022.2 via toolbox<br>
       [<img src="./assets/setup/win/jetbrains_toolkit.png" width="300" />](./assets/setup/win/jetbrains_toolkit.png)
3. Install [Git](https://git-scm.com/)
    - [Git Downloads](https://git-scm.com/downloads)
4. Install [Python](https://www.python.org/)
    - 3.8 Version
    - [Python Downloads](https://www.python.org/downloads/release/python-380/)
    - Install to `C:\Python\Python38\ `
    - Add to `PATH`
5. Install [JDK](https://www.oracle.com/java/)
    - 8u351 Version
    - [OpenJDK 8](https://www.oracle.com/java/technologies/downloads/#java8-windows)
    - Install JDK to `C:\Java\jdk1.8.0_351\ `
    - Install JRE to `C:\Java\jre\ `
6. Install WinUtils
    - [WinUtils](https://github.com/cdarlint/winutils)
    - Save `winutils.exe` to `C:\hadoop\bin\ `
    - Add `HADOOP_HOME` environment variable with path `C:\hadoop\ `
    - Add `%HADOOP_HOME%\bin` to `PATH`
7. Install hadoop.dll
    - [WinUtils](https://github.com/cdarlint/winutils)
    - Copy `hadoop.dll`, from the same location as `winutils.exe`, to `C:\Windows\System32\ `
8. Install Visual C++
    - x86 & x64 [Microsoft Visual C++](https://www.microsoft.com/en-au/download/details.aspx?id=26999)
9. Clone `training_utils`
    - `git clone https://github.com/mrperson2015/training_utils.git`
10. Clone `spark_training`
    - `git clone https://github.com/mrperson2015/spark_training.git`
11. Open project `spark_training` in PyCharm<br>
    [<img src="./assets/setup/win/base_spark_job_main.png" width="300" />](./assets/setup/win/base_spark_job_main.png)
    1. Setup Interpreter
    2. Add user interpreter `training_utils`
       [training_utils](https://github.com/mrperson2015/training_utils)<br>
       [<img src="./assets/setup/win/setup_interpreter.png" width="300" />](./assets/setup/win/setup_interpreter.png)
    3. Install required packages<br>
       [<img src="./assets/setup/win/pycharm_packages.png" width="300" />](./assets/setup/win/pycharm_packages.png)
    4. Run `base_spark_job/main.py`<br>
       [<img src="./assets/setup/win/job_complete.png" width="300" />](./assets/setup/win/job_complete.png)

</details>

## Ubuntu

<details><summary>Instructions for Ubuntu</summary>

1. Install [Ubuntu](https://ubuntu.com/)
    - 20.04.3 LTS Version
    - 8 GB Memory
    - 2 Processor @ 4 Cores each (8 total processor cores)
    - 20 GB NVMe disk (split, unallocated)
    - NAT Network Adapter
2. Upgrade & Update Ubuntu
    - `sudo apt update`
    - `sudo apt upgrade`
3. Install [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/)
4. Install [PyCharm](https://www.jetbrains.com/pycharm/) via JetBrains Toolbox
    - 2022.2 Version
5. Install [Git](https://git-scm.com/)
    - `sudo apt install git`
6. Install [Pip](https://pip.pypa.io/en/stable/)
    - `sudo apt install python3-pip`
7. Install [JDK](https://www.oracle.com/java/)
    - `sudo apt install openjdk-8-jre-headless`
    - 1.8.0_351 Version
8. Clone `training_utils`
    - `git clone https://github.com/mrperson2015/training_utils.git`
9. Clone `spark_training`
    - `git clone https://github.com/mrperson2015/spark_training.git`
10. Open project `spark_training` in PyCharm<br>
    [<img src="./assets/setup/ubuntu/base_spark_job_main.png" width="300" />](./assets/setup/ubuntu/base_spark_job_main.png)
    1. Setup interpreter
    2. Add user interpreter to `training_utils`<br>
       [<img src="./assets/setup/ubuntu/setup_interpreter.png" width="300" />](./assets/setup/ubuntu/setup_interpreter.png)
    3. Install required packages<br>
       [<img src="./assets/setup/ubuntu/package_requirements.png" width="300" />](./assets/setup/ubuntu/package_requirements.png)
    4. Run `base_spark_job/main.py`<br>
       [<img src="./assets/setup/ubuntu/job_complete.png" width="300" />](./assets/setup/ubuntu/job_complete.png)

</details>