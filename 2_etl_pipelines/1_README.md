# ETL Pipelines

## Overview
This directory contains examples and projects for building **ETL (Extract, Transform, Load)** pipelines using Python and various ETL tools. These pipelines are essential in data engineering, responsible for collecting data from different sources, transforming it into a suitable format, and loading it into target databases or files.

By working through these examples, you will develop a solid understanding of ETL concepts, workflows, and best practices.

### Basic, Intermediate, and Advanced Projects

- **Basic**: Create a simple ETL pipeline that reads data from a CSV file, performs basic transformations (like cleaning and aggregation), and outputs the transformed data into a new CSV file.
  
- **Intermediate**: Extend the basic pipeline by integrating Airflow for orchestration. This includes scheduling the pipeline to run periodically, handling errors, and adding logging functionality.
  
- **Advanced**: Build a complete ETL pipeline that interacts with cloud storage (AWS S3 or GCP), integrates Airflow for orchestration, and uses tools like dbt for transforming data. You’ll also add data validation steps and error-handling mechanisms to ensure data quality.

---

## Project Structure

### 1. **Basic ETL Pipeline** (Using Python)

**Objective**: 
To create a simple ETL pipeline that extracts data from a CSV file, applies basic transformations, and loads the results into another CSV file.

**Project Files**:
- **2_python/etl_basic.py**: This Python script extracts data from the AmesHousing dataset, cleans it (e.g., handling missing values), and saves the transformed data into a new CSV file.
 
- **5_data/**: Contains the input and output data for the pipeline.

**Steps**:
 - Loads the dataset.
- Cleans it by handling missing values.
- Aggregate Final_Sale_Price by MS Zoning and calculate the average.
- Save the transformed dataset to a new CSV file.

---

### 2. **Intermediate ETL Pipeline** (Python + Airflow)

**Objective**:
To build an ETL pipeline using **Apache Airflow** to orchestrate and schedule tasks. This project adds error-handling, logging, and basic scheduling features.

**Project Files**:
- **3_airflow/etl_airflow.py**: Contains the DAG (Directed Acyclic Graph) for orchestrating the ETL tasks using Airflow.
- **2_python/**: Python scripts for extraction, transformation, and loading steps.
- **5_data/**: Data used in the ETL process.

**Steps**:
- Schedule and orchestrate the ETL process using Airflow.
- Automatically trigger the ETL pipeline every 24 hours.
- Add logging and error-handling steps to monitor pipeline failures.

---

### 3. **Advanced ETL Pipeline** (Python + Airflow + dbt + Cloud Integration)

**Objective**:
Build an advanced ETL pipeline that integrates with cloud services like **AWS S3** or **Google Cloud Storage**, orchestrates tasks using **Airflow**, and performs complex transformations using **dbt**.

**Project Files**:
- **4_tools/dbt_transformations.sql**: SQL scripts that perform transformations using dbt.
- **3_airflow/etl_cloud_dag.py**: Airflow DAG for orchestrating cloud-based ETL tasks.
- **2_python/etl_cloud.py**: Python scripts for extracting and loading data from/to cloud services (e.g., AWS S3).
- **5_data/**: Example datasets stored in cloud storage (or local for simplicity).

**Steps**:
- Extract data from cloud storage (e.g., AWS S3).
- Use dbt for complex transformations (e.g., joins, aggregations).
- Load the transformed data back into cloud storage or a data warehouse.
- Schedule and monitor the pipeline using Airflow.
- Implement data validation and error-handling to ensure data quality.

---

## Tools and Libraries Used
- **Python**: Core language used for scripting ETL tasks.
- **Pandas**: Used for data manipulation and transformation.
- **Airflow**: For orchestration and scheduling of ETL workflows.
- **dbt (Data Build Tool)**: For transforming data using SQL.
- **Cloud Services**: AWS S3, Google Cloud Storage for cloud-based ETL pipelines.
  
---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd data_engineering_fundamentals/02_etl_pipelines
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Basic ETL pipeline:
   ```bash
   python 2_python/etl_basic.py
   ```

4. (Optional) Setup Airflow for the intermediate and advanced pipelines:
   ```bash
   airflow db init
   airflow webserver --port 8080
   airflow scheduler
   ```

---

## Learning Objectives

By completing these projects, you will:
1. Understand the fundamentals of ETL workflows.
2. Gain hands-on experience building ETL pipelines using Python.
3. Learn to orchestrate tasks with Airflow and integrate dbt for transformation.
4. Work with cloud storage for advanced ETL tasks.
5. Implement error handling, logging, and scheduling in production-ready pipelines.

---