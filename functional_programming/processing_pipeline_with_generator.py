# processing_pipeline_with_generator.py

# use python2

import os
import fnmatch
import sys

def find(topdir, pattern):
    print(topdir)
    for path, dirname, filelist in os.walk(topdir):
        print(path)
        for name in filelist:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path,name)

import gzip, bz2
def opener(filenames):
    for name in filenames:
        if name.endswith(".gz"): f = gzip.open(name)
        elif name.endswith(".bz2"): f = bz2.BZ2File(name)
        else: f = open(name)
        yield f

def cat(filelist):
    for f in filelist:
        for line in f:
            yield line

def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


if __name__ == '__main__':
    # An example of using these functions to set up a processing pipeline
    wwwlogs = find("/tmp/www", "insurance*")
    #print([ f for f in wwwlogs ])
    files = opener(wwwlogs)
    lines = cat(files)
    #print([ type(line) for line in lines ])
    pylines = grep("run_batch", lines)
    for line in pylines:
        #sys.stdout.write(line)
        print(line)     