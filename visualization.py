import os

import matplotlib.pyplot as plt
import numpy as np


def create_visualizations(summary, output_dir):
    """Create the charts used in the project output."""
    create_missing_values_chart(summary, output_dir)
    create_duplicates_chart(summary, output_dir)
    create_completeness_score_chart(summary, output_dir)


def create_missing_values_chart(summary, output_dir):
    """Create a bar chart for missing values by column."""
    missing_values = summary["column_missing_percentages"]

    plt.figure(figsize=(10, 5))
    plt.bar(missing_values.index, missing_values.values, color="#4C78A8")
    plt.title("Missing Values by Column")
    plt.xlabel("Column")
    plt.ylabel("Missing Values (%)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "missing_values_chart.png"))
    plt.close()


def create_duplicates_chart(summary, output_dir):
    """Create a small chart showing duplicate and unique records."""
    duplicate_records = summary["duplicate_records"]
    unique_records = summary["total_rows"] - duplicate_records

    plt.figure(figsize=(6, 5))
    plt.bar(["Unique Records", "Duplicate Records"], [unique_records, duplicate_records], color=["#59A14F", "#E15759"])
    plt.title("Duplicate Records Count")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "duplicates_chart.png"))
    plt.close()


def create_completeness_score_chart(summary, output_dir):
    """Create a simple completeness score chart."""
    score = summary["completeness_score"]
    remaining = 100 - score

    plt.figure(figsize=(6, 6))
    plt.pie(
        np.array([score, remaining]),
        labels=["Complete Data", "Missing Data"],
        autopct="%1.1f%%",
        colors=["#76B7B2", "#F28E2B"],
        startangle=90,
    )
    plt.title("Data Completeness Score")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "completeness_score_chart.png"))
    plt.close()
