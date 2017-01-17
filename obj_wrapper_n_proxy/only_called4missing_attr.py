# only_called4missing_attr.py

class Spam(object):
    def __getattr__(self, name):
        # Failsafe.   Only called for missing attributes
        print('Getting', name)


if __name__ == '__main__':
    s = Spam()
    s.x =42
    s.y = 20
    print(s.x)
    print(s.missininaction)        