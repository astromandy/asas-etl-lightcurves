# 📊 ETL Pipeline for ASAS-SN Light Curves

This project implements an ETL (Extract, Transform, Load) pipeline to retrieve and visualize light curve data from the ASAS-SN database using a list of coordinates.

##Pipeline:
- **Extract**: Queries the ASAS-SN catalog for objects near given coordinates.
- **Transform**: Cleans and sorts the light curve data (e.g., removing NaNs, sorting by time).
- **Load**: Generates a multi-page PDF with one plot per light curve.

## 💡 Technologies Used

- Python
- Pandas
- Matplotlib
- PyASASSN (ASAS-SN client wrapper)
- Jupyter Notebook / .py script


## ⚙️ Installation

Clone this repository and install the required dependencies:

```bash
git clone https://github.com/astromandy/asas-etl-lightcurves.git
cd asas-etl-lightcurves
pip install -r requirements.txt

🚀 ## Usage
Edit the coords list in asas-etl-lightcurves.py with your target coordinates:

python
Copiar
Editar
coords = [
    ('ObjectName', RA_in_degrees, DEC_in_degrees),
    ...
]

###Run the pipeline:

bash
Copiar
Editar
python asas-etl-lightcurves.py
The script will generate a PDF file (e.g., asas_lcs_ETL.pdf) containing light curve plots for each object.
