import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

csv_file = r".\Hubdistance.csv"
df = pd.read_csv(csv_file)

group_counts = (
    df.groupby("Pollutant_Group")["Air Quality Station Name"]
    .nunique()
    .reset_index()
    .rename(columns={"Air Quality Station Name": "Station_Count"})
)

colors = sns.color_palette("Paired", len(group_counts))  
random.shuffle(colors)
# -----------------------------


# Create pie chart
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


plt.savefig("pollutant_group_pie.png", dpi=300)
plt.show()
