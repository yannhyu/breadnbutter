# toolchain.py
import csv

def scrub_data_value(input_dict):
    return {k: v.replace('|', r' ') for k, v in input_dict.items() if v}

def write(output_filename, toCSV):
    if toCSV:
        keys = (
            'author',
            'title',
            'genre',
            'publish_date',                   
            )
        with open(output_filename, 'wb') as output_file:
            dict_writer = csv.DictWriter(
                output_file,
                fieldnames=keys,
                extrasaction='ignore',
                delimiter="|")
            dict_writer.writeheader()
            dict_writer.writerows(toCSV)
