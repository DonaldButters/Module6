import unittest


class MyTestCase(unittest.TestCase):
    def test_score_input_test_score_below_range(self):
        self.assertLessEqual(100)


if __name__ == '__main__':
    unittest.main()
