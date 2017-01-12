# allow_multiple_ways2initialize_obj.py

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, s):    # cls is "Date"
        parts = s.split('-')
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))

    @classmethod
    def today(cls):
        import time
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


d = Date(2017, 1, 10)
e = Date.from_string('2007-06-11')
f = Date.today()

print(d.month, ' ', d.day, ' ', d.year)
print(e.month, ':', e.day, ':', e.year)

print(f.year)
print(f.month)
print(f.day)       