# 📊 ETL Pipeline for ASAS-SN Light Curves

This project implements an ETL (Extract, Transform, Load) pipeline to retrieve and visualize light curve data from the ASAS-SN database using a list of coordinates.

## 🧩 Project Structure

- **Extract**: Queries the ASAS-SN catalog for objects near given coordinates.
- **Transform**: Cleans and sorts the light curve data (e.g., removing NaNs, sorting by time).
- **Load**: Generates a multi-page PDF with one plot per light curve.

## 💡 Technologies Used

- Python
- Pandas
- Matplotlib
- PyASASSN (ASAS-SN client wrapper)
- Jupyter Notebook / .py script

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/asas-etl-lightcurves.git
cd asas-etl-lightcurves
