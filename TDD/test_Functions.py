from functions import *
import unittest

class printTest(unittest.TestCase):

    def test_printSomething(self):
        input = "something"
        self.assertEqual(printSomething(input),"something")

    def test_printSomething1(self):
        input = "something"
        self.assertEqual(printSomething(input),"something")

    def test_printSomething2(self):
        input = "something"
        self.assertEqual(printSomething(input),"something")

if __name__ == '__main__':
    unittest.main()