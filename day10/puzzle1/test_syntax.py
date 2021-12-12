import unittest

from syntax import line_score


class CorruptedLineCheck(unittest.TestCase):

    def test_line(self):
        line = "[{[{({}]{}}([{[{{{}}([]"
        self.assertEquals(57, line_score(line))


if __name__ == "__main__":
    unittest.main()
