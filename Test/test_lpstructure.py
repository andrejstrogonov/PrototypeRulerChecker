import unittest
from LPStructure.lpstructure import LPStructure


class MyTestCase(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(LPStructure.sum(), True)
        pass

    def test_multiplication(self):
        self.assertEqual(LPStructure.multiplication(), False)
        pass

    def test_implication(self):
        self.assertEqual(LPStructure.implication(), False)
        pass


if __name__ == '__main__':
    unittest.main()
