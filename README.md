📊 Log Data ETL Pipeline (Python + SQL)

## 🚀 Overview

This project demonstrates a basic **ETL (Extract, Transform, Load)** pipeline built using Python and SQL to process system log data.

It simulates real-world data engineering workflows such as:

* Data ingestion
* Data transformation
* Data storage
* Data analysis

---

## ⚙️ Tech Stack

* Python
* Pandas
* SQLite
* SQL

---

## 🔄 ETL Workflow

### 1️⃣ Extract

* Load log data from CSV file using Pandas

### 2️⃣ Transform

* Clean and process data
* Convert CPU usage to numeric
* Create derived column (`status_flag`) for failure detection

### 3️⃣ Load

* Store processed data into SQLite database

### 4️⃣ Analyze

* Perform SQL queries to extract insights:

  * Failure count per device
  * Average CPU usage

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python etl.py
```

---

## 📈 Sample Output

* Processed dataset stored in database
* Failure analysis per device
* System performance insights

---

## 🎯 Learning Outcomes

* Understanding of ETL pipelines
* Data transformation and validation
* SQL-based data analysis
* Python-based data processing

---

## 💡 Future Improvements

* Integrate real-time data sources (APIs)
* Deploy pipeline on cloud (AWS/Snowflake)
* Add dashboard visualization (Power BI / Grafana)
