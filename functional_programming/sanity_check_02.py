# sanity_check_02.py

import os
import fnmatch
def find(topdir, pattern):
    for path, dirname, filelist in os.walk(topdir):
        for name in filelist:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path,name)


if __name__ == '__main__':
    # An example of using these functions to set up a processing pipeline
    wwwlogs = find("/tmp/www","insurance*")
    print([ f for f in wwwlogs ])       