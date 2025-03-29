import json
import xml.etree.ElementTree as ET
import os

# Get the current working directory
current_directory = os.getcwd()

# Read JSON data from file
with open('input.json', 'r', encoding='utf-8') as json_file:
    json_data = json_file.read()

# Parse JSON data
data_dict = json.loads(json_data)

# Create XML tree
root = ET.Element("root")
data_element = ET.SubElement(root, "data")

languages_element = ET.SubElement(data_element, "languages")

for language in data_dict["data"]["languages"]:
    language_element = ET.SubElement(languages_element, "language")
    code_element = ET.SubElement(language_element, "code")
    code_element.text = language["code"]
    name_element = ET.SubElement(language_element, "name")
    name_element.text = language["name"]

# Create and save the XML file
xml_tree = ET.ElementTree(root)
xml_tree.write("output.xml", encoding="utf-8", xml_declaration=True)

print("XML conversion complete. Output saved to {}\output.xml.".format(current_directory))
print('')
print('Updated using VSC')