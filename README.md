# SIM Cards Analytics & BI Project

## Overview

Business Intelligence and Data Engineering project for telecom SIM card analytics.

The project includes:
- Python ETL pipelines
- PostgreSQL warehouse
- STAR schema
- Power BI dashboards
- KPI reporting

---

## Technologies

- Python
- PostgreSQL
- SQL
- Power BI
- Pandas
- SQLAlchemy

---

## Features

- Excel data ingestion
- Data cleaning
- Automated ETL
- KPI calculations
- Dashboard analytics
- STAR schema modeling

---

## PostgreSQL Configuration

The project uses PostgreSQL as the main database.

Before running the ETL pipeline:

1. Install PostgreSQL
2. Create a database:

```sql
CREATE DATABASE sim_db;
```

3. Update database credentials in:

```python
config/config.py
```

Example:

```python
DB_USER = 'postgres'
DB_PASSWORD = 'your_password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'sim_db'
```

4. Run the ETL pipeline:

```bash
python main.py
```

The project automatically creates and populates all required tables:
- sim_cards_raw
- employees
- devices
- tariff
- fact_sim_usage

No manual table creation is required.

---

## Requirements

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## Dashboard Preview

TBA

---

## Author

Bartosz Czarnowski
