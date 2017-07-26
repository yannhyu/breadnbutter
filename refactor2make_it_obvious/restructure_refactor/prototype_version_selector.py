cust_ver_map = {
    'v1': [15, 30, 42],
    'v2': [19, 33, 39, 49],
    'v2_invoice': [52,],
    'v3': [73, 80, 81],
    'v3_invoice': [5005, 5006],
    'v4': [122, 127, 133],
    'v4_invoice': [153, 170, 171],
    'v5': [5011, 5013],
    'v6': [5031, 5083, 5093],
}

def found(cust_id):
    found = None
    for k, v in cust_ver_map.items():
        # print('{} <--- {}'.format(cust_id, v))
        if (cust_id in v):
            found = k
            break
    return found

class Selected(object):
    def __init__(self, cust_id):
        self.cust_id = cust_id
        self.key_found = found(cust_id)
        self._result = False

    def __nonzero__(self):
        return self._result


class V1(Selected):
    def __init__(self, cust_id):
        super(V1, self).__init__(cust_id)
        if self.key_found:
            self._result = (self.key_found == 'v1')


class V2(Selected):
    def __init__(self, cust_id):
        super(V2, self).__init__(cust_id)
        if self.key_found:
            self._result = (self.key_found == 'v2')


class V2_INVOICE(Selected):
    def __init__(self, cust_id):
        super(V2_INVOICE, self).__init__(cust_id)
        if self.key_found:
            self._result = (self.key_found == 'v2_invoice')


class V3(Selected):
    def __init__(self, cust_id):
        super(V3, self).__init__(cust_id)
        if self.key_found:
            self._result = (self.key_found == 'v3')


class V3_INVOICE(Selected):
    def __init__(self, cust_id):
        super(V3_INVOICE, self).__init__(cust_id)
        if self.key_found:
            self._result = (self.key_found == 'v3_invoice')


class V4(Selected):
    def __init__(self, cust_id):
        super(V4, self).__init__(cust_id)
        if self.key_found:
            self._result = (self.key_found == 'v4')


class V4_INVOICE(Selected):
    def __init__(self, cust_id):
        super(V4_INVOICE, self).__init__(cust_id)
        if self.key_found:
            self._result = (self.key_found == 'v4_invoice')


class V5(Selected):
    def __init__(self, cust_id):
        super(V5, self).__init__(cust_id)
        if self.key_found:
            self._result = (self.key_found == 'v5')


class V6(Selected):
    def __init__(self, cust_id):
        super(V6, self).__init__(cust_id)
        if self.key_found:
            self._result = (self.key_found == 'v6')


if __name__ == '__main__':
    v1 = V1(15)
    v2 = V2(15)
    v2_invoice = V2_INVOICE(15)
    v6 = V6(15)
    assert v1
    assert not v2
    assert not v2_invoice
    assert not v6


    v1 = V1(5093)
    v2 = V2(5093)
    v2_invoice = V2_INVOICE(5093)
    v6 = V6(5093)
    assert not v1
    assert not v2
    assert not v2_invoice
    assert v6    
