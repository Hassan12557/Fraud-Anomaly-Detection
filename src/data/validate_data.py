
from pathlib import Path

import numpy as np
import pandas as pd


RAW_FILE = Path("D:/Data science Project/Fraud & Anomaly Detection/data/raw/creditcard.csv")

EXPECTED_COLUMNS = (
    ["Time"]
    + [f"V{i}" for i in range(1, 29)]
    + ["Amount", "Class"]
)


def validate_dataset(file_path: Path) -> None:
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    print("\n========== DATASET OVERVIEW ==========")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())

    print("\n========== DATA TYPES ==========")
    print(df.dtypes)

    print("\n========== MISSING VALUES ==========")
    print(df.isnull().sum().to_string())

    print("\n========== DUPLICATES ==========")
    print("Exact duplicate rows:", df.duplicated().sum())

    print("\n========== CLASS DISTRIBUTION ==========")
    if "Class" in df.columns:
        print(df["Class"].value_counts(dropna=False))
        print("\nClass proportions:")
        print(df["Class"].value_counts(normalize=True))

    print("\n========== NUMERIC SUMMARY ==========")
    print(df.describe().to_string())

    # 1. Schema validation
    missing_columns = set(EXPECTED_COLUMNS) - set(df.columns)
    extra_columns = set(df.columns) - set(EXPECTED_COLUMNS)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {sorted(missing_columns)}"
        )

    if extra_columns:
        raise ValueError(
            f"Unexpected columns: {sorted(extra_columns)}"
        )

    if list(df.columns) != EXPECTED_COLUMNS:
        raise ValueError("Columns are not in expected order.")

    # 2. Numeric validation
    if not all(
        pd.api.types.is_numeric_dtype(df[col])
        for col in EXPECTED_COLUMNS
    ):
        raise ValueError("One or more columns are not numeric.")

    # 3. Missing-value validation
    if df.isnull().any().any():
        raise ValueError("Missing values detected.")

    # 4. Infinite-value validation
    numeric_values = df[EXPECTED_COLUMNS].to_numpy()

    if not np.isfinite(numeric_values).all():
        raise ValueError("Infinite values detected.")

    # 5. Label validation
    if not set(df["Class"].unique()).issubset({0, 1}):
        raise ValueError("Class contains unexpected values.")

    # 6. Basic domain checks
    if (df["Time"] < 0).any():
        raise ValueError("Negative transaction time detected.")

    if (df["Amount"] < 0).any():
        print(
            "WARNING: Negative amounts found. "
            "Investigate before deciding how to handle them."
        )

    print("\n========== VALIDATION RESULT ==========")
    print("All mandatory validation checks passed.")


if __name__ == "__main__":
    validate_dataset(RAW_FILE)
