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

class_counts = df["Class"].value_counts().sort_index()

class_percentages = (
    df["Class"]
    .value_counts(normalize=True)
    .sort_index() * 100
)

distribution = pd.DataFrame({
    "Transaction Count": class_counts,
    "Percentage": class_percentages
})

print(distribution)
plt.figure(figsize=(8, 5))

sns.barplot(
    x=class_counts.index,
    y=class_counts.values
)

plt.title("Legitimate vs Fraudulent Transactions")
plt.xlabel("Class (0 = Legitimate, 1 = Fraud)")
plt.ylabel("Number of Transactions")
plt.xticks([0, 1], ["Legitimate", "Fraud"])

plt.show()

#Investigate the 1081 duplicate rows
#First: Count duplicates by class
duplicate_rows = df[df.duplicated(keep=False)]

print("Rows involved in duplicate groups:",
      len(duplicate_rows))

print("\nDuplicate rows by class:")

print(
    duplicate_rows["Class"]
    .value_counts()
)
#Second: Investigate identical features with different labels
#We should also ask whether identical transaction features have ever been assigned conflicting fraud labels
feature_columns = [
    col for col in df.columns if col != "Class"
]

label_counts = (
    df.groupby(feature_columns, dropna=False)["Class"]
    .nunique()
)

conflicting_groups = label_counts[label_counts > 1]

print(
    "Identical feature groups with conflicting labels:",
    len(conflicting_groups)
)