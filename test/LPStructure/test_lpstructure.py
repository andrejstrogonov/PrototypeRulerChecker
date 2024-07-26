import unittest
from LPStructure.lpstructure import LPStructure


class MyTestCase(unittest.TestCase):
    def test_sum(self):
        self.assertTrue(LPStructure.sum())
        pass

    def test_multiplication(self):
        self.assertFalse(LPStructure.multiplication())
        pass

    def test_implication(self):
        self.assertFalse(LPStructure.implication())
        pass


if __name__ == '__main__':
    unittest.main()
