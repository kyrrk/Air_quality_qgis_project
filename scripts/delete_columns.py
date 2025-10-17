import csv

layer = iface.activeLayer()

# Columns to keep
keep_fields = [
    'Air Pollutant', 
    'Air Quality Station Name', 
    'Air Quality Station Type', 
    'Longitude', 
    'Latitude'
]


output_path = r".\air_quality_stations_clean.csv"
field_indices = [layer.fields().indexOf(f) for f in keep_fields]

with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # write header
    writer.writerow(keep_fields)
    # write rows
    for feat in layer.getFeatures():
        writer.writerow([feat.attributes()[i] for i in field_indices])

print("Exported cleaned CSV")
