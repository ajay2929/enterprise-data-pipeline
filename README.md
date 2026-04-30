# 📊 Enterprise Data Pipeline Framework
**A modular ETL framework designed for scalable data orchestration between disparate sources and cloud data warehouses.**

## 📖 Overview
This project demonstrates a senior-level approach to Data Engineering. Instead of a single script, it uses a **Transformer Design Pattern** to ensure that data cleaning logic is modular, testable, and reusable across different business units (e.g., Finance, Marketing).

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Data Warehousing:** Snowflake / Amazon Redshift
* **Libraries:** Pandas, SQLAlchemy, Pytest
* **Infrastructure:** AWS S3, Docker

## 🏗️ Architectural Patterns
* **Factory Pattern:** Used to initialize different data loaders (S3, SQL, API) dynamically.
* **S.O.L.I.D Principles:** Ensuring the "Transformation" logic is decoupled from the "Loading" logic to prevent system fragility.

## ⚡ Setup & Usage
```bash
# Set up environment
pip install -r requirements.txt

# Run the pipeline
python main.py --source s3 --target snowflake
