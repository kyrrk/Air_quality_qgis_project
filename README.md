# Air_quality_qgis_project
This project visualizes air quality monitoring stations in Belgium, using 2024 data from the European Environment Agency (EEA). Pollutants are categorized by chemical group (Nitrogen compounds, Metals, Sulphur compounds, Volatile Organic Compounds, Particulates, Others) and displayed on a QGIS map with color-coded symbols.

## Data
- Source: European Environment Agency (EEA), 2024
- Raw and processed CSV files are included in the `/data` folder.

## Methods
- Python script `categorize_pollutants.py` categorizes pollutants and outputs a CSV with new fields.
- QGIS used for map visualization, legend creation, and color symbology.

## Map
![Brussels Air Quality Map](maps/Air_Quality_Map_Balgium.png)

## How to Use
1. Open the CSV in QGIS.
2. Run the Python script to categorize pollutants if needed.
3. Join the processed CSV back to your spatial layer.
4. Apply categorized symbology based on the `Pollutant_Group` field.

## Author
Kyriaki Kefala