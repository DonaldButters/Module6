import unittest
import test_functions.test_string_functions

class MyTestCase(unittest.TestCase):
    def multiple_string(self):
        self.failUnless(range (1,10))


if __name__ == '__main__':
    unittest.main()
