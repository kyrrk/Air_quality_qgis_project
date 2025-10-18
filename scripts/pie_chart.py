import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# -----------------------------
# 1. Load exported CSV
# -----------------------------
csv_file = r"D:\Users\Kyriaki\Documents\QGSISProject\emission_sources_Belgium\Hubdistance.csv"
df = pd.read_csv(csv_file)

# -----------------------------
# 2. Count number of stations per pollutant group
# -----------------------------
group_counts = (
    df.groupby("Pollutant_Group")["Air Quality Station Name"]
    .nunique()
    .reset_index()
    .rename(columns={"Air Quality Station Name": "Station_Count"})
)


# -----------------------------
# 3. Choose color palette (options: 'Spectral', 'viridis', 'plasma', 'coolwarm')
# -----------------------------
colors = sns.color_palette("Paired", len(group_counts))  
random.shuffle(colors)
# -----------------------------
# 4. Create pie chart
# -----------------------------
plt.figure(figsize=(7, 7))
plt.pie(
    group_counts["Station_Count"],
    labels=group_counts["Pollutant_Group"],
    autopct="%1.1f%%",
    startangle=90,
    counterclock=False,
    colors=colors
)

plt.title("Share of Air Quality Stations by Pollutant Group")
plt.tight_layout()

# Save and show chart
plt.savefig("pollutant_group_pie_spectrum.png", dpi=300)
plt.show()