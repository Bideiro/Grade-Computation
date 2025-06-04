import pandas as pd

# Load the CSV
df = pd.read_csv("grade_report.csv")

# Options to include/exclude NSTP and PE
include_nstp = 0  # Set to 1 to include NSTP, 0 to exclude
include_pe = 0    # Set to 1 to include PE, 0 to exclude

# Filter out NSTP and/or PE based on course codes
if not include_nstp:
    df = df[~df["Course Code"].str.contains("NSTP", na=False)]
if not include_pe:
    df = df[~df["Course Code"].str.contains("PE", na=False)]

# Calculate Grade Units
df["Grade Unit"] = df["Credit Units"] * df["Grade"]

# GPA Calculation
total_grade_units = df["Grade Unit"].sum()
total_units = df["Credit Units"].sum()

gpa = total_grade_units / total_units if total_units else 0

print(f"GPA: {gpa:.4f}")
