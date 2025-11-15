# Local-Log-to-Database ETL Pipeline

A complete ETL (Extract–Transform–Load) project that reads local log files, processes them, and stores structured log data into a SQLite database for analysis.

---

##  Project Overview

This project demonstrates how to:

- Extract log data from `.log` files stored locally  
- Transform and clean the logs into structured records  
- Load processed logs into a SQLite database  
- Analyze log patterns and generate summaries  

---

##  Tech Stack

- **Python**
- **SQLite** — Local database storage  
- **os** — File extraction  
- **sqlite3** — Database operations  

---

## Process

### **Extract**
Reads raw log files from the `logs/` directory.

**Example raw log format:**
```bash
2025-01-12 10:02:01, INFO, Server started
2025-01-12 10:05:23, ERROR, Failed to connect to DB
```


---

### ** Transform**
Cleans and parses the log data:

- Splits each line into `timestamp`, `level`, and `message`  
- Skips malformed lines  
- Ensures consistent formatting  

---

### ** Load**
Inserts the transformed data into a SQLite database:

- Creates **logs.db**  
- Ensures `logs` table exists  
- Loads all log entries  

---

### ** Analyze**
Performs log analysis:

- Total log entries  
- Log level count (INFO, ERROR, WARNING, etc.)  
- Summary output for debugging and monitoring  

---

## Run the Pipeline

### **Install Dependencies**
*(No external dependencies needed — uses Python standard library only.)*

---

### **Run ETL**
```bash
python main.py
```

### **Run Analysis**
```bash
python analyze.py
```

### **Example Output**
```bash
 Extracting logs...
 Transforming logs...
 Loading logs into database...
 ETL Pipeline completed successfully!
 Data saved to logs.db
```
### **Analysis Output**
```bash 
  Total log entries: 4

  Log Level Summary:
  INFO: 2
  ERROR: 1
  WARNING: 1
```
### **Create Your Log Files**
  - Create files like logs/app1.log with the format:
```bash
2025-01-12 10:02:01, INFO, Server started
2025-01-12 10:05:23, ERROR, Failed to connect to DB
2025-01-12 10:15:10, WARNING, High memory usage
2025-01-12 11:00:00, INFO, Scheduled maintenance started
```
### **Project Structure**
----
Local-Log-to-Database-ETL-Pipeline/
│
├── logs/
│     └── app1.log
│
├── src/
│     ├── extract.py
│     ├── transform.py
│     └── load.py
│
├── main.py
└── analyze.py
----
### **Author**
**Matthew Lawrence L**
Bengaluru,Karnataka
lawrence82773824@gmail.com
