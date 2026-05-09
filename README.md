# Data Quality Analysis System

This is a Python project for checking and cleaning a messy customer dataset. It looks for missing values, duplicate rows, and overall data completeness, then saves the cleaned data and a few simple outputs. I built it as a portfolio project to show basic data cleaning, analysis, and reporting skills.

## Problem Statement

Real datasets are often not ready to use right away. They can have blank values, repeated records, and column names that are hard to work with. This project gives a small example of how I would check a dataset first, clean it, and create a short summary before using it for analysis.

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- Matplotlib

## Features

- Loads customer data from a CSV file
- Cleans missing values in text and number columns
- Removes duplicate records
- Standardizes column names
- Calculates missing value percentage
- Counts duplicate records
- Calculates a completeness score
- Saves the cleaned dataset into a SQLite database
- Creates simple charts for data quality results
- Exports a summary report as a CSV file

## How to Run the Project

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Run the project:

```bash
python main.py
```

The project will create an `outputs` folder with the cleaned database, report, and charts.

## Example Outputs

- `data_quality_summary.csv` gives a short report with total rows, missing values, duplicate records, and the completeness score.
- `data_quality.db` stores the cleaned customer dataset in a SQLite table.
- `missing_values_chart.png` shows which columns have missing data.
- `duplicates_chart.png` compares unique records with duplicate records.
- `completeness_score_chart.png` shows how complete the dataset is overall.
