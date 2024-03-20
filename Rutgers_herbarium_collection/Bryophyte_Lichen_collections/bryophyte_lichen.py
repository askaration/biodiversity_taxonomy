import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import xml.dom.minidom
import requests

# Read data from URL into a pandas DataFrame
url = "https://bryophyteportal.org/portal/collections/listtabledisplay.php?db=32"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract data from HTML table
    data = pd.read_html(response.content)[0]

    fam_count = data["Family"].value_counts()

    top_20 = fam_count.iloc[:20]

    # Convert DataFrame to JSON and save to file
    data.to_json("data.json", orient="records", indent=4)

    # Plot count of unique families
    plt.figure(figsize=(12, 8))
    sns.countplot(y='Family', data=data, order=top_20.index)
    plt.xlabel("Frequency")
    plt.ylabel("Families")
    plt.title("Top 20 Most Common Families")
    plt.savefig("top20Fams.png", dpi=300)
    plt.show()
else:
    print("Error: Failed to fetch data from the URL.")
