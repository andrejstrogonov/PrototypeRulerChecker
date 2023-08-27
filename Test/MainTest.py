import unittest
import pytest
import main


class MyTestCase(unittest.TestCase):
    def test_good(self):
        self.aassrtTrue("good", main.TestParser.parser(main.testdata))


if __name__ == '__main__':
    unittest.main()
