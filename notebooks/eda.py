import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

# Reproducible visualization style
sns.set_theme(style="whitegrid")

# Load processed dataset
DATA_PATH = Path(
    "D:/Data science Project/Fraud & Anomaly Detection/data/processed/creditcard_validated.csv"
)

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully")
print("Shape:", df.shape)

#First, let's understand how much data we have and how it is distributed.
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nStatistical summary:")
print(df.describe())