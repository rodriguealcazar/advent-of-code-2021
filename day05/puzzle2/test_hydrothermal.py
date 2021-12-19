import unittest

from collections import defaultdict

from hydrothermal_all import diagonal


class HydrothermalTestCase(unittest.TestCase):

    def test_diagonal(self):
        d = defaultdict(lambda: 0)
        diagonal(d, 9, 7, 7, 9)
        print(d)


if __name__ == "__main__":
    unittest.main()
