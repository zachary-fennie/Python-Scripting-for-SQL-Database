[![CI/CD](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/CI_CD.yml/badge.svg)](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/CI_CD.yml) [![Install](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/install.yml/badge.svg)](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/install.yml) [![Format](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/format.yml/badge.svg)](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/format.yml) [![Lint](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/lint.yml/badge.svg)](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/lint.yml) [![Test](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/test.yml/badge.svg)](https://github.com/zfennie/Python-Scripting-for-SQL-Database/actions/workflows/test.yml)



# Fennie's Python Scripting for SQL Database
## A Python script for an ETL pipeline to external data. The project will extract data from a url, make any necessary transformations, load the transformed data into a SQLite database, and perform CRUD queries to ananlyze and retrieve preliminary insights on the stored data.


This folder contains the data behind the story How One High-Risk Community In Rural South Carolina Is Bracing For COVID-19.

mmsa-icu-beds.csv combines data from the Centers for Disease Control and Prevention’s Behavioral Risk Factor Surveillance System (BRFSS), a collection of health-related surveys conducted each year of more than 400,000 Americans, and the Kaiser Family Foundation to show the number of people who are at high risk of becoming seriously ill from COVID-19 per ICU bed in each metropolitan area, micropolitan area or metropolitan division for which we have data.

Being high risk is defined by a number of health conditions and behaviors. Based on the CDC’s list of the relevant underlying conditions that put people at higher risk of serious illness from COVID-19, plus the advice of experts from the Cleveland Clinic, the American Lung Association and the American Heart Association, we counted people as at risk if they’re 65 or older; if they have ever been told they have hypertension, coronary heart disease, a myocardial infarction, angina, a stroke, chronic kidney disease, chronic obstructive pulmonary disease, emphysema, chronic bronchitis or diabetes; if they currently have asthma or a BMI over 40; if they smoke cigarettes every day or some days or use e-cigarettes or vaping products every day or some days; or if they’re currently pregnant. We included every individual who meets at least one of these conditions but counted them only once each, so anyone with multiple conditions doesn’t get counted multiple times. We were not able to include a number of conditions for which we did not have location-based data from the BRFSS, such as liver disease, having smoked, vaped or dabbed marijuana in the last 30 days, and getting cancer treatment or being on immunosuppression medications.

combines data from the Centers for Disease Control and Prevention’s Behavioral Risk Factor Surveillance System (BRFSS), a collection of health-related surveys conducted each year of more than 400,000 Americans, and the Kaiser Family Foundation to show the number of people who are at high risk of becoming seriously ill from COVID-19 per ICU bed in each metropolitan area, micropolitan area or metropolitan division for which we have data.

FiveThirtyEight's MMS ICU Beds Dataset\
This dataset combines data from the Centers for Disease Control and Prevention's Behavioral Risk Factor Surveillance System (BRFSS) and the Kaiser Family Foundation to illustrate the number of people who were at high risk for hospitalization from the novel coronavirus COVID-19 in 2020.\
URL: https://github.com/fivethirtyeight/data/blob/e6bbbb2d35310b5c63c2995a0d03d582d0c7b2e6/covid-geography/mmsa-icu-beds.csv

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