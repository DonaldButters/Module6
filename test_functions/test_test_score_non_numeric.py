import unittest


class MyTestCase(unittest.TestCase):
    def test_test_score_non_numeric(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
