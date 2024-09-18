import json
import csv
import os

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Write headers
        headers = data[0].keys()
        writer.writerow(headers)

        # Write rows
        for item in data:
            writer.writerow(item.values())

def convert_all_json_to_csv(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json"):
                json_file = os.path.join(root, file)
                csv_file = os.path.join(root, file.replace('.json', '.csv'))
                print(f"Converting {json_file} to {csv_file}")
                json_to_csv(json_file, csv_file)

# Specify the base directory for components
base_directory = 'components-data'
convert_all_json_to_csv(base_directory)
