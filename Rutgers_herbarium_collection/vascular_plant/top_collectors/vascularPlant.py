import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import xml.dom.minidom
import requests

# Read data from URL into a pandas DataFrame
url = "https://midatlanticherbaria.org/portal/collections/listtabledisplay.php?db=316"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract data from HTML table
    data = pd.read_html(response.content)[0]

    collector_count = data["Collector"].value_counts()
    state_count = data["State/Province"].value_counts()
    county_count = data["County"].value_counts()

    coll_top_10 = collector_count.iloc[:10]
    state_top_10 = state_count.iloc[:10]
    county_top_10 = county_count.iloc[:10]


    print("Top 10 Collectors are: ", coll_top_10)
    print("Top 10 Counties are: ", county_top_10)
    print("Top 10 States are: ", state_top_10)

    # Convert DataFrame to JSON and save to file
    data.to_json("data.json", orient="records", indent=4)

    # Plot count of unique families
    plt.figure(figsize=(14, 8))
    sns.countplot(y='Collector', data=data, order=coll_top_10.index)
    plt.xlabel("Frequency")
    plt.ylabel("Collectors")
    plt.title("Top 10 Collectors")
    plt.savefig("top10Collectors.png", dpi=300)
    plt.show()
else:
    print("Error: Failed to fetch data from the URL.")
