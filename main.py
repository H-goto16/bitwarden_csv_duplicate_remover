import csv
import argparse

parser = argparse.ArgumentParser(
    description='Remove duplicate entries from a Bitwarden CSV export.')
parser.add_argument('--input', '-i', default='bitwarden.csv',
                    help='Path to input CSV file')
parser.add_argument(
    '--output', '-o', default='bitwarden_unique.csv', help='Path to output CSV file')
args = parser.parse_args()

seen = set()
unique_rows = []

with open(args.input, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        key = (row['login_uri'], row['login_username'], row['login_password'])
        if key not in seen:
            seen.add(key)
            unique_rows.append(row)

with open(args.output, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(unique_rows)
