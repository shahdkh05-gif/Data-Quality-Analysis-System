import os

import pandas as pd

from data_cleaning import analyze_data_quality, clean_data, export_summary_report, load_dataset
from database import save_to_sqlite
from visualization import create_visualizations


DATA_PATH = os.path.join("data", "customer_data.csv")
OUTPUT_DIR = "outputs"
DATABASE_PATH = os.path.join(OUTPUT_DIR, "data_quality.db")
REPORT_PATH = os.path.join(OUTPUT_DIR, "data_quality_summary.csv")


def main():
    print("Data Quality Analysis System")
    print("----------------------------")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Loading dataset from: {DATA_PATH}")
    raw_data = load_dataset(DATA_PATH)

    print("Analyzing original data quality...")
    quality_summary = analyze_data_quality(raw_data)

    print("Cleaning data...")
    cleaned_data = clean_data(raw_data)

    print("Saving cleaned data to SQLite database...")
    save_to_sqlite(cleaned_data, DATABASE_PATH, table_name="cleaned_customers")

    print("Creating charts...")
    create_visualizations(quality_summary, OUTPUT_DIR)

    print("Exporting summary report...")
    export_summary_report(quality_summary, REPORT_PATH)

    print("\nProject finished successfully.")
    print(f"Cleaned rows: {len(cleaned_data)}")
    print(f"SQLite database: {DATABASE_PATH}")
    print(f"Summary report: {REPORT_PATH}")
    print(f"Charts folder: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
