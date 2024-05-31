import unittest

from LPStructure.ActivationFunctions import ActivationFunctions


class MyTestCase1(unittest.TestCase):
    def test_weight(self):
        self.assertTrue((main.TestParser.calculator()))
        pass

    def test_risk(self):
        self.assertTrue((main.TestParser.riskcalc()))

        def test_holester():
            self.assertTrue((main.TestParser.holstercalc()))

        pass

    def test_start(self):
        self.assertTrue(main.TestParser.startcalc())
        pass

    @staticmethod
    def test_product(self):
        self.assertEqual(ActivationFunctions.relu(2), 2)

        pass


if __name__ == '__main__':
    unittest.main()
