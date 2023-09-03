import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_weight(self):
        self.assertTrue((main.TestParser.calculator("normal")))


if __name__ == '__main__':
    unittest.main()
