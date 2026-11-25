# CSV Data Cleaning & Reporting Tool (Mini ETL Pipeline)

A lightweight, modular ETL (Extract, Transform, Load) pipeline built entirely with Python's standard library. It ingests raw e-commerce transaction records, validates data quality, deduplicates transaction IDs, normalizes fields, exports a clean CSV dataset, and generates a JSON summary report.

## Project Structure

```text
mini-etl-project/
├── data/
│   ├── input/
│   │   └── raw_transactions.csv
│   └── output/
│       ├── cleaned_data.csv
│       └── report.json
├── src/
│   ├── main.py
│   ├── reader.py
│   ├── validator.py
│   ├── transformer.py
│   └── reporter.py
├── README.md
└── requirements.txt