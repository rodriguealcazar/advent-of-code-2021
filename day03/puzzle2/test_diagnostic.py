import unittest

from diagnostic import matches_at_index


class TestDiagnostic(unittest.TestCase):

    def test_matches_at_index(self):
        numbers = [
            [0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 1, 1, 0],
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0]
        ]
        expected = (
            [
                [1, 1, 1, 1, 0],
                [1, 0, 1, 1, 0],
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 1, 1, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 1]
            ],
            [
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0]
            ]
        )

        self.assertEquals(expected, matches_at_index(numbers, 0))


if __name__ == "__main__":
    unittest.main()
