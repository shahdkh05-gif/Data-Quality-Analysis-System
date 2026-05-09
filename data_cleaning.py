import pandas as pd


def load_dataset(file_path):
    """Load the CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def standardize_column_names(data):
    """Make column names easier to use in Python."""
    data = data.copy()
    data.columns = (
        data.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return data


def clean_data(data):
    """Clean the dataset by fixing names, missing values, and duplicates."""
    cleaned_data = standardize_column_names(data)

    # Remove rows that are repeated exactly.
    cleaned_data = cleaned_data.drop_duplicates()

    # Fill missing text values with a simple label.
    text_columns = cleaned_data.select_dtypes(include=["object"]).columns
    for column in text_columns:
        cleaned_data[column] = cleaned_data[column].fillna("Unknown")

    # Fill missing numeric values with the median of that column.
    numeric_columns = cleaned_data.select_dtypes(include=["number"]).columns
    for column in numeric_columns:
        median_value = cleaned_data[column].median()
        cleaned_data[column] = cleaned_data[column].fillna(median_value)

    return cleaned_data


def analyze_data_quality(data):
    """Create a simple data quality summary for the original dataset."""
    total_cells = data.shape[0] * data.shape[1]
    missing_cells = int(data.isnull().sum().sum())
    duplicate_records = int(data.duplicated().sum())

    missing_percentage = (missing_cells / total_cells) * 100 if total_cells > 0 else 0
    completeness_score = 100 - missing_percentage

    column_missing_percentages = data.isnull().mean() * 100

    summary = {
        "total_rows": len(data),
        "total_columns": len(data.columns),
        "total_cells": total_cells,
        "missing_cells": missing_cells,
        "missing_percentage": round(missing_percentage, 2),
        "duplicate_records": duplicate_records,
        "completeness_score": round(completeness_score, 2),
        "column_missing_percentages": column_missing_percentages,
    }

    return summary


def export_summary_report(summary, output_path):
    """Save the main quality results as a CSV report."""
    report_data = {
        "metric": [
            "Total Rows",
            "Total Columns",
            "Total Cells",
            "Missing Cells",
            "Missing Percentage",
            "Duplicate Records",
            "Completeness Score",
        ],
        "value": [
            summary["total_rows"],
            summary["total_columns"],
            summary["total_cells"],
            summary["missing_cells"],
            f'{summary["missing_percentage"]}%',
            summary["duplicate_records"],
            f'{summary["completeness_score"]}%',
        ],
    }

    report = pd.DataFrame(report_data)
    report.to_csv(output_path, index=False)
