# -*- coding: utf-8 -*-
# In Python 2 you often need the line above at the top of your file
# so you can see Unicode characters
a = 'niño'
print(a)
print(type(a))

# Use u'bob' to create unicode, 'bob' is str (ascii)
b = u'bob'
print(b)
print(type(b))

# A lot of times you will get text from some unknown encoding. 
# UTF-8 is the most common representation.
# If you need to catch errros, you can remove errors='ignore'
def convert_unicode(text):
    if isinstance(text,str):
        return text.decode('utf-8',errors='ignore')
    else:
        return text

in_str = 'à'
print(type(in_str))
in_unicode = convert_unicode(in_str)
print(type(in_unicode))
