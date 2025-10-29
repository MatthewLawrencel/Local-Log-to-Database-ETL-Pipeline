# Local-Log-to-Database-ETL-Pipeline

A beginner-friendly **Data Engineering project** built with **Python and SQLite** to simulate an ETL (Extract, Transform, Load) workflow using local log files.

---

## 🚀 Project Overview

This pipeline demonstrates how to:
- **Extract** data from local `.log` files
- **Transform** and clean log messages
- **Load** structured data into a database
- **Analyze** the results using SQL

---

## 🧩 Tech Stack

- **Python 3.13**
- **SQLite3**
- **pandas** (optional)
- **os**, **argparse**, **datetime** modules

---

## ⚙️ How It Works

### 1️⃣ Extract
Reads all `.log` files from the `logs/` directory.

### 2️⃣ Transform
Cleans and structures each log entry into a format.

### 3️⃣ Load
Creates a SQLite database `logs.db` and inserts data into a table named `logs`.

### 4️⃣ Analyze
Aggregates and summarizes log data (e.g., how many `INFO`, `ERROR`, or `WARNING` entries exist).

---

## Run the Pipeline

```bash
# Activate your virtual environment first
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the ETL pipeline
python -m src.main --log_dir logs

# Analyze results
python -m src.analyze

```

### Example Output

Extracting logs...

Transforming logs...


Loading into database...


✅ Data successfully loaded into logs.db


🎯 Pipeline completed successfully!

📦 Total log entries: 5

📊 Log Level Summary:
   
     INFO: 2
     
     WARNING: 1
     
     ERROR: 2
``


### Author 
# Matthew Lawrence L
Bengaluru, Karnataka

lawrence82773824@gmail.com
