# read_write_csv_with_generator.py

import csv
from faker import Factory
fake = Factory.create()

def csv_dict_reader(filename):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(filename, delimiter=',')
    headers = reader.fieldnames
    for line in reader:
        yield headers, line

def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """
    with open(path, "w") as out_file:
        writer = csv.DictWriter(out_file, delimiter='|', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def transform(dict_data):
    dict_data['name'] = fake.name()
    dict_data['favorite'] = fake.street_address()

    return dict_data

if __name__ == "__main__":
    with open("sample.csv") as fh:
        rows = csv_dict_reader(fh)
        results = []
        for headers, row in rows:
            print(headers)
            results.append(transform(row))

        path = "sample_output.csv"
        csv_dict_writer(path, headers, results)