# read_csv_cherry_pick_columns_n_write.py

import csv                 

with open("fake_123_inc.txt", "r") as rfh, open("med_123_cherry_picked.txt", "w", newline='') as wfh:
    r = csv.DictReader(rfh, delimiter='|')
    headers = r.fieldnames
    print(headers)
    headers = headers[4:8]
    print(headers)
    w = csv.DictWriter(wfh, fieldnames=headers, extrasaction='ignore', delimiter='|')
    w.writeheader()
    for row in r:
        #print(row)
        w.writerow(row)
