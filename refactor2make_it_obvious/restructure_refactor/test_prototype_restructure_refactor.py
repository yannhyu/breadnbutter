import unittest
from prototype_version_selector import *

class TestCustID2VersionMapping(unittest.TestCase):

    def test_cust_id_15(self):
        v1 = V1(15)
        v2 = V2(15)
        v2_invoice = V2_INVOICE(15)
        v3 = V3(15)
        v3_invoice = V3_INVOICE(15)
        v4 = V4(15)
        v4_invoice = V4_INVOICE(15)                  
        v5 = V5(15)
        v6 = V6(15)
        self.assertTrue(v1)
        self.assertFalse(v2)
        self.assertFalse(v2_invoice)
        self.assertFalse(v3)
        self.assertFalse(v3_invoice)
        self.assertFalse(v4)
        self.assertFalse(v4_invoice)
        self.assertFalse(v5)               
        self.assertFalse(v6)

    def test_cust_id_5093(self):
        v1 = V1(5093)
        v2 = V2(5093)
        v2_invoice = V2_INVOICE(5093)
        v6 = V6(5093)
        self.assertFalse(v1)
        self.assertFalse(v2)
        self.assertFalse(v2_invoice)
        self.assertTrue(v6)

    def test_cust_id_171(self):
        v1 = V1(171)
        v2 = V2(171)
        v2_invoice = V2_INVOICE(171)
        v6 = V6(171)
        self.assertFalse(v1)
        self.assertFalse(v2)
        self.assertFalse(v2_invoice)
        self.assertFalse(v6)


if __name__ == '__main__':
    unittest.main()
