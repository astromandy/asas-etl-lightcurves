#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from pyasassn.client import SkyPatrolClient
client = SkyPatrolClient()

# -----------------------------
# EXTRACT
# -----------------------------
def extract_light_curves(coords, tolerance=0.005):
    results = []
    for name, ra, dec in coords:
        query = f"""
        SELECT * 
        FROM master_list 
        WHERE DISTANCE(ra_deg, dec_deg, {ra}, {dec}) <= {tolerance}
        """
        lcs = client.adql_query(query, download=True)
        if lcs is not None and not lcs.data.empty:
            results.append((name, lcs.data))
    return results

# -----------------------------
# TRANSFORM
# -----------------------------
def transform_light_curve(df):
    # Remove null values 
    df = df.dropna(subset=["jd", "mag"])
    df = df.sort_values(by="jd")
    return df

# -----------------------------
# LOAD
# -----------------------------
def load_to_pdf(light_curves, output_path):
    with PdfPages(output_path) as pdf:
        for name, df in light_curves:
            df = transform_light_curve(df)
            plt.figure(figsize=(10, 4))
            plt.scatter(df["jd"], df["mag"], s=5)
            plt.gca().invert_yaxis()
            plt.title(f'Light Curve: {name}')
            plt.xlabel('HJD')
            plt.ylabel('mag')
            plt.grid(True)
            pdf.savefig()
            plt.close()

# -----------------------------
# MAIN PIPELINE
# -----------------------------
if __name__ == "__main__":
    coords = [
        ('SS Cyg', 325.678348, 43.586074),
        ('CC Cnc', 129.079806, 21.351507),
        # ... others coordinates
    ]
    
    output_pdf = 'your/path/asas_lcs_ETL.pdf'
    
    extracted_data = extract_light_curves(coords)
    load_to_pdf(extracted_data, output_pdf)


# In[ ]:




