"""Data loading, cleaning, and analysis functions for the weather project."""

from pathlib import Path
import numpy as np
import pandas as pd

EXPECTED_COLUMNS = [
    "date", "city", "temperature_c", "humidity_pct", "rainfall_mm"
]


def load_weather_data(csv_path: str | Path) -> pd.DataFrame:
    """Load a CSV file and validate that required columns are present."""
    df = pd.read_csv(csv_path)
    missing_columns = sorted(set(EXPECTED_COLUMNS) - set(df.columns))
    if missing_columns:
        raise ValueError(f"CSV is missing required columns: {missing_columns}")

    df = df[EXPECTED_COLUMNS].copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for column in ["temperature_c", "humidity_pct", "rainfall_mm"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df["city"] = df["city"].astype("string").str.strip().str.title()
    return df


def clean_weather_data(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Remove duplicates, standardize values, and handle missing/invalid data."""
    starting_rows = len(df)
    duplicate_rows = int(df.duplicated().sum())
    cleaned = df.drop_duplicates().copy()

    # Empty or invalid city names cannot be used for city-level analysis.
    cleaned["city"] = cleaned["city"].replace("", pd.NA)
    cleaned = cleaned.dropna(subset=["date", "city"])

    # Treat physically implausible percentages and negative rainfall as missing.
    cleaned.loc[~cleaned["humidity_pct"].between(0, 100), "humidity_pct"] = np.nan
    cleaned.loc[cleaned["rainfall_mm"] < 0, "rainfall_mm"] = np.nan

    # Impute missing numeric values with the median of that column.
    # If a whole column is missing, use zero as a safe fallback for this demo.
    for column in ["temperature_c", "humidity_pct", "rainfall_mm"]:
        median_value = cleaned[column].median()
        if pd.isna(median_value):
            median_value = 0.0
        cleaned[column] = cleaned[column].fillna(median_value)

    # Keep one decimal place for readability.
    cleaned["temperature_c"] = cleaned["temperature_c"].round(1)
    cleaned["humidity_pct"] = cleaned["humidity_pct"].round(1)
    cleaned["rainfall_mm"] = cleaned["rainfall_mm"].round(1)

    report = {
        "starting_rows": starting_rows,
        "duplicate_rows_removed": duplicate_rows,
        "final_rows": len(cleaned),
        "missing_values_after_cleaning": int(cleaned.isna().sum().sum()),
    }
    return cleaned.sort_values(["date", "city"]).reset_index(drop=True), report


def analyze_weather_data(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Create city-level aggregates and overall numerical summaries."""
    city_summary = (
        df.groupby("city", as_index=False)
        .agg(
            average_temperature_c=("temperature_c", "mean"),
            average_humidity_pct=("humidity_pct", "mean"),
            total_rainfall_mm=("rainfall_mm", "sum"),
            observations=("date", "count"),
        )
        .sort_values("average_temperature_c", ascending=False)
    )

    temperatures = df["temperature_c"].to_numpy(dtype=float)
    overall = {
        "observations": int(len(df)),
        "cities": int(df["city"].nunique()),
        "average_temperature_c": float(np.mean(temperatures)) if len(temperatures) else 0.0,
        "minimum_temperature_c": float(np.min(temperatures)) if len(temperatures) else 0.0,
        "maximum_temperature_c": float(np.max(temperatures)) if len(temperatures) else 0.0,
        "temperature_std_dev_c": float(np.std(temperatures)) if len(temperatures) else 0.0,
    }

    return city_summary.round(2), overall


def filter_hot_days(df: pd.DataFrame, threshold_c: float = 30.0) -> pd.DataFrame:
    """Return rows whose temperature is at or above a threshold."""
    return df.loc[df["temperature_c"] >= threshold_c].copy()


def demo_python_basics() -> None:
    """Small terminal examples covering input/output, conditions, and loops."""
    temperatures = [28.0, 31.5, 26.0]
    print("\nPython basics demonstration")
    print("--------------------------")
    for index, temperature in enumerate(temperatures, start=1):
        label = "Hot" if temperature >= 30 else "Moderate or cool"
        print(f"Observation {index}: {temperature:.1f}°C — {label}")

    # Demonstrate a function and list comprehension.
    fahrenheit = [round((c * 9 / 5) + 32, 1) for c in temperatures]
    print(f"Temperatures in Fahrenheit: {fahrenheit}")
    print(f"Average of sample temperatures: {np.mean(temperatures):.2f}°C")
