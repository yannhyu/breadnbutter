# swiss_army_knife.py

import os

def cd(dirname):
    os.chdir(dirname)

def pwd():
    print(os.getcwd())

def ls(dirname=''):
    os.system('dir %s' % dirname)

def allfiles(topdir):
    return ((path, filename)
            for path, dirs, files in os.walk(topdir)
            for filename in files)

def filetypes(topdir):
    from collections import Counter
    from pprint import pprint
    c = Counter(os.path.splitext(name)[1]
                for _, name in allfiles(topdir))
    pprint(c.most_common())

def find(topdir, pattern):
    from fnmatch import fnmatch
    return ((path, name)
            for path, name in allfiles(topdir)
            if fnmatch(name, pattern))

def find_versions(topdir):
    import re
    for path, _ in find(topdir, 'pgen.c'):
        pypath, _ = os.path.split(path)
        print(pypath)
        version = re.search(r'-(\w+\.\w+(\.\w+)?)$',
                            pypath).group(1)
        yield version, pypath

def write_manifest(topdir):
    import csv
    f = open('manifest.csv','w')
    csv.writer(f).writerows(find_versions(topdir))
    f.close()