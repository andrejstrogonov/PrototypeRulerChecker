import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_weight(self):
        self.assertTrue((main.TestParser.calculator()))
        pass

    def test_risk(self):
        self.assertTrue((main.TestParser.riskcalc()))
        pass


if __name__ == '__main__':
    unittest.main()
