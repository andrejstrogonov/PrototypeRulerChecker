import unittest
from main_application import TestParser


class MyTestCase1(unittest.TestCase):
    def test_weight(self):
        self.assertTrue((TestParser.calculator()))
        pass

    def test_risk(self):
        self.assertTrue((TestParser.riskcalc()))

    def test_start(self):
        self.assertTrue(TestParser.startcalc())
        pass


if __name__ == '__main__':
    unittest.main()
