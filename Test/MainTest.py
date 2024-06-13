import unittest
from LPStructure.ActivationFunctions import ActivationFunctions
from main_application import TestParser


class MyTestCase1(unittest.TestCase):
    def test_weight(self):
        self.assertTrue((TestParser.calculator()))
        pass

    def test_risk(self):
        self.assertTrue((TestParser.riskcalc()))

    def test_holester(self):
        self.assertTrue((TestParser.holstercalc()))

        pass

    def test_start(self):
        self.assertTrue(TestParser.startcalc())
        pass

    @staticmethod
    def test_product():
        assert (ActivationFunctions.relu(2)) == 2

        pass


if __name__ == '__main__':
    unittest.main()
