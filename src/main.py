"""Run the Month 1 weather data cleaning and analysis project."""

from pathlib import Path
import pandas as pd

from src.data_processing import (
    load_weather_data,
    clean_weather_data,
    analyze_weather_data,
    filter_hot_days,
    demo_python_basics,
)
from src.visualizations import create_visualizations, create_html_dashboard

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "weather_data.csv"
OUTPUT_DIR = ROOT / "outputs"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    demo_python_basics()

    print("\nLoading weather dataset...")
    raw_df = load_weather_data(DATA_PATH)
    print(f"Rows loaded: {len(raw_df)}")

    cleaned_df, cleaning_report = clean_weather_data(raw_df)
    cleaned_path = OUTPUT_DIR / "cleaned_weather_data.csv"
    cleaned_df.to_csv(cleaned_path, index=False)

    summary_df, overall = analyze_weather_data(cleaned_df)
    summary_path = OUTPUT_DIR / "city_weather_summary.csv"
    summary_df.to_csv(summary_path, index=False)

    hot_days = filter_hot_days(cleaned_df, threshold_c=30.0)
    hot_days.to_csv(OUTPUT_DIR / "hot_days_30c_or_more.csv", index=False)

    plots = create_visualizations(cleaned_df, OUTPUT_DIR)
    dashboard_path = create_html_dashboard(
        summary_df, overall, plots, OUTPUT_DIR / "dashboard.html"
    )

    print("\nCleaning report")
    print("---------------")
    for key, value in cleaning_report.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    print("\nOverall statistics")
    print("------------------")
    for key, value in overall.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    print("\nCity summary")
    print("------------")
    print(summary_df.to_string(index=False))

    print("\nFiles created:")
    for path in [cleaned_path, summary_path, OUTPUT_DIR / "hot_days_30c_or_more.csv", *plots, dashboard_path]:
        print(f"- {path.relative_to(ROOT)}")

    print("\nDone! Open outputs/dashboard.html in your browser to view the report.")


if __name__ == "__main__":
    main()
