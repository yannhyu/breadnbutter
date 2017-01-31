# read_transform_write_csv.py
import csv

with open("sample.csv", "r") as rfh, open("output.csv", "w") as wfh:
    r = csv.DictReader(rfh, delimiter=',')
    headers = r.fieldnames
    print(headers)
    w = csv.DictWriter(wfh, fieldnames=headers, delimiter='|')
    w.writeheader()
    for row in r:
        print(row)
        w.writerow(row)
