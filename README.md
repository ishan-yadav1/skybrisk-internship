# Skybrisk Internship — Month 1: Python Basics and Data Manipulation

## Project
**Weather Data Cleaning, Analysis, and Visualization Dashboard**

This project follows the Month 1 task brief:
- Python basics, variables, types, conditions, loops, input/output
- Data structures and functions
- Data cleaning and transformation
- NumPy and Pandas analysis
- Matplotlib and Seaborn visualizations

The project uses a small sample weather dataset (`data/weather_data.csv`) so it runs without downloading external data. The dataset is illustrative and is not live weather data.

## Features
- Validates and cleans weather observations
- Handles missing values and duplicate rows
- Uses NumPy for numerical summaries
- Uses Pandas for filtering, grouping, and aggregation
- Calculates average temperature by city
- Creates a CSV of cleaned data and a city summary
- Produces histograms, scatter plots, a correlation heatmap, and a simple HTML dashboard

## Requirements
- Python 3.10 or newer recommended
- VS Code (or another Python editor)

## Setup (Windows / VS Code)
Open this folder in VS Code, then open Terminal and run:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, you can skip activation and run:
```bash
python -m pip install -r requirements.txt
python -m src.main
```

## Run
From the project root:

```bash
python -m src.main
```

After it finishes, check:
- `outputs/cleaned_weather_data.csv`
- `outputs/city_weather_summary.csv`
- `outputs/temperature_histogram.png`
- `outputs/temperature_vs_humidity.png`
- `outputs/correlation_heatmap.png`
- `outputs/dashboard.html`

## Project structure
```text
skybrisk_month1_data_science/
├── data/
│   └── weather_data.csv
├── outputs/                 # generated when the script runs
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── visualizations.py
│   └── main.py
├── concepts_summary.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Notes
- The original sample CSV intentionally includes a few missing values and a duplicate row to demonstrate cleaning.
- The script keeps the raw data unchanged and writes cleaned results to `outputs/`.
- The HTML dashboard is a simple local report, not a hosted interactive web app.

## Submission checklist
1. Run the script successfully.
2. Review the generated outputs.
3. Update the author details if desired.
4. Push the complete project to GitHub.
5. Submit the repository URL in Google Classroom, along with any files the assignment asks for separately.
