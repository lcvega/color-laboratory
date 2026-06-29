# Color Laboratory

## What this is

Color Laboratory is a Streamlit-based tool for capturing, transforming, and analyzing color data.

It allows input in HEX or RGB and generates a full color harmony dataset for each sample.

Each observation becomes a structured data point for analysis in design and perception studies.

---

## Input modes

- HEX input
- RGB input

---

## Outputs per sample

For every color, the system generates:

- Base color
- Analogous 1
- Analogous 2
- Complementary
- Triad 1
- Triad 2

---

## Data tracking

Each entry includes:

- Timestamp
- HEX value
- RGB values
- Full derived palette

---

## How to run

Install dependencies:

```bash id="2xv9q3"
pip install -r requirements.txt

Run the app:

streamlit run app.py

Export

You can export all collected samples as a CSV file for further analysis in Excel, Python, or statistical tools.

Why this matters

This tool is designed as a bridge between:

Color perception
Computational representation
Design research
Environmental analysis

It turns color input into structured data for experimental use.