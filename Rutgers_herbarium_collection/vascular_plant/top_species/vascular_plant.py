import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import xml.dom.minidom
import requests

# Read data from CSV file into a pandas DataFrame
# data = pd.read_csv("D:/RU/2023 - 2024/Spring/Independent Study/Week 3/Collections/Rutgers/Vascular Plant Collection/SymbOutput_2024-02-08_152645_DwC-A/identifications.csv", encoding='latin1')

url = "https://midatlanticherbaria.org/portal/collections/listtabledisplay.php?db=316"
response = requests.get(url)

if response.status_code == 200:
    data = pd.read_html(response.content)[0]

    print(data.shape[0])
    print(data['Country'].value_counts())



# # Convert DataFrame to XML
# root = ET.Element("data")

# for index, row in data.iterrows():
#     observation = ET.SubElement(root, "observation")
#     for col_name, col_value in row.items():
#         element = ET.SubElement(observation, col_name)
#         element.text = str(col_value)

# # Create an ElementTree object
# tree = ET.ElementTree(root)

# # Save the ElementTree object to an XML file
# tree.write("output.xml")

# # Prettify the XML file
# dom = xml.dom.minidom.parse("output.xml")
# with open("output.xml", "w", encoding="iso-8859-1") as xml_file: 
#     xml_file.write(dom.toprettyxml())



# data.to_json("data.json", orient="records", indent=4)

# Plot count of unique scientific names
# plt.figure(figsize=(12, 8))  # Adjust figure size if needed
# sns.countplot(y='scientificName', data=data, order=data['scientificName'].value_counts().iloc[:20].index)
# plt.xlabel("Frequency")
# plt.ylabel("Scientific Names")
# plt.title("Top 00 Most Common Vascular Plant Species")
# # plt.savefig("top20 Vascular Plants.png")
# plt.show()