import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        headers = data[0].keys()
        writer.writerow(headers)

        for item in data:
            writer.writerow(item.values())

# Exemple d'utilisation
json_to_csv('cpu/cpu_data.json', 'cpu/cpu_data.csv')
