# switching_overhead.py
from __future__ import generators
import time
 
TIMES = 100000
threads = []

def stringops():
    for n in xrange(TIMES):
        s = "Mary had a little lamb"
        s = s.upper()
        s = "Mary had a little lamb"
        s = s.lower()
        s = "Mary had a little lamb"
        s = s.replace('a','A')
 
def scheduler():
    for n in xrange(TIMES):
        for thread in threads: thread.next()
 
def upper():
    while 1:
        s = "Mary had a little lamb"
        s = s.upper()
        yield None
 
def lower():
    while 1:
        s = "Mary had a little lamb"
        s = s.lower()
        yield None
 
def replace():
    while 1:
        s = "Mary had a little lamb"
        s = s.replace('a','A')
        yield None
 
if __name__=='__main__':
    start = time.clock()
    stringops()
    looptime = time.clock()-start
    print"LOOP TIME:", looptime
 
    #global threads
    threads.append(upper())
    threads.append(lower())
    threads.append(replace())
    start = time.clock()
    scheduler()
    threadtime = time.clock()-start
    print"THREAD TIME:", threadtime
