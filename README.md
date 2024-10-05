[![CI/CD](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/CI_CD.yml/badge.svg)](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/CI_CD.yml) [![Install](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/install.yml/badge.svg)](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/install.yml) [![Format](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/format.yml/badge.svg)](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/format.yml) [![Lint](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/lint.yml/badge.svg)](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/lint.yml) [![Test](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/test.yml/badge.svg)](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/test.yml)



# Fennie's Python Scripting for SQL Database
## A Python script for an ETL pipeline to external data. The project will extract data from a url, make any necessary transformations, load the transformed data into a SQLite database, and perform CRUD queries to ananlyze and retrieve preliminary insights on the stored data.



Pandas Decriptive Report for Russian Equipment Losses (since the start of the war)\
Data Source - Kaggle: Russia Ukraine War 2022\
URL: https://www.kaggle.com/datasets/piterfm/2022-ukraine-russian-war?select=russia_losses_equipment.csv

Core Files are:
- Jupyter notebook
- library.py
- test_library.py & test_main.py
- requirements.txt
- CI/CD pipeline
- Makefile
- README.md

### Summary Statistics of the Russian Equipment Losses
![Alt Text](./summary_stats.png)

### Data Visualization of the Russian Equipment Losses
![Alt Text](./main_ground_losses.png)