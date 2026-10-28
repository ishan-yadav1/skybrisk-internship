"""Plot and HTML report generation."""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")  # Allows saving plots without opening GUI windows.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def create_visualizations(df: pd.DataFrame, output_dir: str | Path) -> list[Path]:
    """Save a histogram, scatter plot, and correlation heatmap."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    created = []

    sns.set_theme()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x="temperature_c", bins=10, kde=True, color="steelblue", ax=ax)
    ax.set_title("Distribution of Daily Temperatures")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Number of observations")
    fig.tight_layout()
    path = output_dir / "temperature_histogram.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    created.append(path)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=df, x="temperature_c", y="humidity_pct",
        hue="city", size="rainfall_mm", sizes=(30, 180), ax=ax
    )
    ax.set_title("Temperature vs Humidity")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Humidity (%)")
    fig.tight_layout()
    path = output_dir / "temperature_vs_humidity.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    created.append(path)

    numeric = df[["temperature_c", "humidity_pct", "rainfall_mm"]]
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
    ax.set_title("Weather Feature Correlation Heatmap")
    fig.tight_layout()
    path = output_dir / "correlation_heatmap.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    created.append(path)

    return created


def create_html_dashboard(
    summary: pd.DataFrame, overall: dict, plot_paths: list[Path], output_path: str | Path
) -> Path:
    """Create a compact HTML dashboard with summary metrics and embedded plots."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    metrics = [
        ("Observations after cleaning", overall["observations"]),
        ("Cities covered", overall["cities"]),
        ("Mean temperature", f'{overall["average_temperature_c"]:.2f} °C'),
        ("Minimum temperature", f'{overall["minimum_temperature_c"]:.1f} °C'),
        ("Maximum temperature", f'{overall["maximum_temperature_c"]:.1f} °C'),
    ]
    metric_html = "".join(
        f'<div class="metric"><span>{label}</span><strong>{value}</strong></div>'
        for label, value in metrics
    )

    table_html = summary.to_html(index=False, classes="summary", border=0)
    image_html = "".join(
        f'<section><h2>{path.stem.replace("_", " ").title()}</h2>'
        f'<img src="{path.name}" alt="{path.stem.replace("_", " ")} chart"></section>'
        for path in plot_paths
    )

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Weather Data Analysis Dashboard</title>
<style>
body {{ font-family: Arial, sans-serif; max-width: 1100px; margin: 30px auto; padding: 0 18px; color: #202938; }}
header {{ padding: 22px; border-radius: 12px; background: #eef4ff; }}
.metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin: 20px 0; }}
.metric {{ padding: 16px; border: 1px solid #d8deea; border-radius: 10px; }}
.metric span {{ display: block; font-size: 13px; margin-bottom: 8px; color: #536174; }}
.metric strong {{ font-size: 22px; }}
section {{ margin: 26px 0; }}
img {{ width: 100%; max-width: 850px; height: auto; border: 1px solid #e0e4eb; border-radius: 8px; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ padding: 10px; border-bottom: 1px solid #e2e6ed; text-align: left; }}
th {{ background: #f3f5f8; }}
.note {{ color: #596579; font-size: 13px; }}
</style>
</head>
<body>
<header>
<h1>Weather Data Analysis Dashboard</h1>
<p>Month 1 Data Science Project — Skybrisk Intern Certification</p>
<p class="note">Demonstration dataset only; values are illustrative and are not live weather readings.</p>
</header>
<div class="metrics">{metric_html}</div>
<section><h2>City-level summary</h2>{table_html}</section>
{image_html}
</body>
</html>"""
    output_path.write_text(html, encoding="utf-8")
    return output_path
