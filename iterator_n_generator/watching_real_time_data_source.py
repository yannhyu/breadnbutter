# watching_real_time_data_source.py

# Watch a log file

import os
import time

f = open('Data/somelogfile.log', 'r')
f.seek(0, os.SEEK_END)

while True:
    line = f.readline()
    if not line:
        time.sleep(0.1)
        continue    # Retry
    print('Got:', line)