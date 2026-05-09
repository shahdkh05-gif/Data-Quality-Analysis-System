# Data Quality Analysis System

This is a simple Python project I made for my student portfolio. The project works with a messy customer dataset, checks a few data quality problems, cleans the data, and saves the results.

The idea is to show a practical example of how raw business data can be reviewed before using it for reports or analysis.

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- Matplotlib

## Project Files

- `main.py` - runs the full project
- `data_cleaning.py` - loads, analyzes, and cleans the dataset
- `database.py` - saves the cleaned data into SQLite
- `visualization.py` - creates the charts
- `requirements.txt` - lists the Python packages needed
- `data/customer_data.csv` - sample messy customer dataset

## Features

- Loads a CSV customer dataset
- Standardizes column names
- Handles missing values
- Removes duplicate rows
- Calculates missing value percentage
- Counts duplicate records
- Calculates a completeness score
- Saves cleaned data into a SQLite database
- Creates simple charts with Matplotlib
- Exports a summary report as a CSV file

## How to Run

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Run the project from the terminal:

```bash
python main.py
```

## Sample Outputs

After running the project, the `outputs` folder will contain:

- `data_quality.db` - SQLite database with the cleaned customer data
- `data_quality_summary.csv` - summary report of the data quality results
- `missing_values_chart.png` - chart showing missing values by column
- `duplicates_chart.png` - chart showing duplicate records
- `completeness_score_chart.png` - chart showing the overall completeness score

Example terminal output:

```text
Data Quality Analysis System
----------------------------
Loading dataset from: data/customer_data.csv
Analyzing original data quality...
Cleaning data...
Saving cleaned data to SQLite database...
Creating charts...
Exporting summary report...

Project finished successfully.
```

## Why This Project Is Useful

Data quality is important because missing values, duplicates, and messy column names can affect reports and business decisions. This project is a small example of how I can use Python to inspect and clean data before using it for analysis.
