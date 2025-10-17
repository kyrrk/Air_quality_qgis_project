import csv
from qgis.PyQt.QtWidgets import QFileDialog
from qgis.core import QgsProject


output_csv = r".\air_quality_stations_grouped.csv"

# All original fields plus the new ones
field_names = [f.name() for f in layer.fields()]
field_names += ['Pollutant_Group', 'In_Particulates'] 

with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()

    for feature in layer.getFeatures():
        pollutant = feature['Air Pollutant'].lower().strip()
        # Determine if particulate-bound
        in_pm = any(x in pollutant for x in ['pm10', 'pm2.5', 'in pm'])
        # Determine chemical group
        if any(pollutant.startswith(x) for x in ['no', 'no2', 'nox', 'no3', 'nh4']):
            group = 'Nitrogen compounds'
        elif any(pollutant.startswith(x) for x in ['as', 'cd', 'pb', 'hg', 'ni', 'ca', 'mg', 'k', 'na']):
            group = 'Metals'
        elif any(x in pollutant for x in ['so2', 'so4']):
            group = 'Sulphur compounds'
        elif (
            'benz' in pollutant
            or pollutant.endswith('ene')
            or '-' in pollutant
            or '=' in pollutant
            or ('c' in pollutant and 'h' in pollutant)
            or 'ene in' in pollutant
        ):
            group = 'Volatile organic compounds'
        elif pollutant in ['pm10', 'pm2.5']:
            group = 'Particulates'
            in_pm = True



        else:
            group = 'Others'

        
        row_dict = {f: feature[f] for f in [f.name() for f in layer.fields()]}
        row_dict['Pollutant_Group'] = group
        row_dict['In_Particulates'] = in_pm

        writer.writerow(row_dict)
