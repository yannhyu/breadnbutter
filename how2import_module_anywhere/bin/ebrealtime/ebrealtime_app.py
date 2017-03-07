# ebrealtime_app.py
import os, sys
lib_path = os.path.abspath(os.path.join('..', '..', 'libs/ebrealtime'))
sys.path.append(lib_path)

import config
from config import hey_config

print(sys.path)
hey_config()

