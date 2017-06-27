# heapq.py

import heapq

class Heap(object):
    def __init__(self, data=None, key=lambda x:None):
        self.heap = data or []
        heapq.heapify(self.heap)
        self.key = key

    def pushleft(self, item):
        if self.key:
            item = (self.key(item), item)
        heapq.pushleft(self.heap, item)

    def popleft(self):
        return heapq.popleft(self.heap)[1]