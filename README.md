# ETL Pipeline: Largest Banks by Market Capitalization

This project implements a complete **ETL (Extract, Transform, Load) pipeline** in Python to collect, process, and store financial data for the world’s largest banks.

The pipeline extracts market capitalization data from Wikipedia, transforms values into multiple currencies using external exchange rates, and loads the results into both CSV files and a relational database for querying.

## 🚀 What This Project Does

- Extracts top global banks by market capitalization (USD) from the web
- Transforms values into **GBP, EUR, and INR**
- Loads processed data into:
  - CSV file (local storage)
  - SQLite database (queryable)
- Supports SQL queries for region-specific reporting
- Maintains execution logs for traceability


## 🧱 Tech Stack

- Python
- Pandas
- BeautifulSoup (Web Scraping)
- SQLite
- SQL
- CSV-based data exchange
- File-based logging


## 📁 Project Structure

Each ETL stage is implemented as a separate module to ensure clarity, testability, and extensibility.

src/ → ETL pipeline source code \
data/ → Raw and processed datasets \
logs/ → ETL execution logs 

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/etl.py
