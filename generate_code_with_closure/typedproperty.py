# typedproperty.py

def typed_property(name, expected_type):
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('Expected {}'.format(expected_type))
        setattr(self, private_name, value)

    return prop