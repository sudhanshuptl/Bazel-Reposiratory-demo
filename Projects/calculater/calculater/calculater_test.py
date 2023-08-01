from calculater import add, sub, div, mult
import unittest


class Testcase(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(5, 3), 8)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)

    def test_mult(self):
        self.assertEqual(mult(5, 3), 15)

    def test_div(self):
        self.assertEqual(div(15, 3), 5)


if __name__ == '__main__':
    unittest.main()
