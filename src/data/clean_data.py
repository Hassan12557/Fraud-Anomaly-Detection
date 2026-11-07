
from pathlib import Path

import numpy as np
import pandas as pd

from src.data.validate_data import (
    EXPECTED_COLUMNS,
    validate_dataset,
)

RAW_FILE = Path("D:/Data science Project/Fraud & Anomaly Detection/data/raw/creditcard.csv")
PROCESSED_DIR = Path("D:/Data science Project/Fraud & Anomaly Detection/data/processed")
OUTPUT_FILE = PROCESSED_DIR / "creditcard_validated.csv"


def clean_dataset():
    # Validate before transforming anything
    validate_dataset(RAW_FILE)

    df = pd.read_csv(RAW_FILE)

    # Make a separate working copy
    cleaned = df.copy()

    # Enforce expected column order
    cleaned = cleaned[EXPECTED_COLUMNS]

    # Ensure numeric values are represented consistently
    for column in EXPECTED_COLUMNS:
        cleaned[column] = pd.to_numeric(
            cleaned[column],
            errors="raise"
        )

    # Reject missing and infinite values
    if cleaned.isnull().any().any():
        raise ValueError("Missing values found.")

    if not np.isfinite(cleaned.to_numpy()).all():
        raise ValueError("Infinite values found.")

    # Do NOT remove duplicates automatically
    duplicate_count = cleaned.duplicated().sum()

    print("Duplicate records retained:", duplicate_count)

    # Do NOT use Class as a cleaning or training feature
    # Class remains available for later evaluation.

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    cleaned.to_csv(OUTPUT_FILE, index=False)

    print("\nCleaning process completed.")
    print("Original shape:", df.shape)
    print("Processed shape:", cleaned.shape)
    print("Saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    clean_dataset()
