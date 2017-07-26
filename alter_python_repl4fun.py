result = '''
++++++++++++++++++++++++++++++++++++++
+               HELLO                +
+       Customized Python REPL       +           
++++++++++++++++++++++++++++++++++++++
'''


class SlideWrapper(object):
    def __init__(self, cls, text):
        self.cls = cls
        self.text = text
    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)
    def __repr__(self):
        # Create the slide text
        return result

dict = SlideWrapper(dict, '... slide text ...')
tuple = SlideWrapper(tuple, '... slide text ...') 
set = SlideWrapper(set, '... slide text ...')
