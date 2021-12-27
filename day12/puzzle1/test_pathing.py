import unittest


from pathing import map_as_paths, valid_paths


class PathFindingTest(unittest.TestCase):

    def test_parsing_map(self):
        map = [
            "start-A",
            "start-b",
            "A-c",
            "A-b",
            "b-d",
            "A-end",
            "b-end",
        ]
        self.assertEquals(
            {
                'start': ['A', 'b'],
                'A': ['c', 'b', 'end'],
                'c': ['A'],
                'b': ['A', 'd', 'end'],
                'd': ['b']
            },
            dict(map_as_paths(map))
        )

    def test_example_1(self):
        paths = {
            'start': ['A', 'b'],
            'A': ['c', 'b', 'end'],
            'c': ['A'],
            'b': ['A', 'd', 'end'],
            'd': ['b']
        }
        self.assertEquals(
            [
                ["start", "A", "c", "A", "b", "A", "end"],
                ["start", "A", "c", "A", "b", "end"],
                ["start", "A", "c", "A", "end"],
                ["start", "A", "b", "A", "c", "A", "end"],
                ["start", "A", "b", "A", "end"],
                ["start", "A", "b", "end"],
                ["start", "A", "end"],
                ["start", "b", "A", "c", "A", "end"],
                ["start", "b", "A", "end"],
                ["start", "b", "end"]
            ],
            valid_paths([], 'start', paths)
        )

    def test_example_2(self):
        connections = [
            "dc-end",
            "HN-start",
            "start-kj",
            "dc-start",
            "dc-HN",
            "LN-dc",
            "HN-end",
            "kj-sa",
            "kj-HN",
            "kj-dc"
        ]
        self.assertEquals(
            [
                ["start", "HN", "dc", "HN", "end"],
                ["start", "HN", "dc", "HN", "kj", "HN", "end"],
                ["start", "HN", "dc", "end"],
                ["start", "HN", "dc", "kj", "HN", "end"],
                ["start", "HN", "end"],
                ["start", "HN", "kj", "HN", "dc", "HN", "end"],
                ["start", "HN", "kj", "HN", "dc", "end"],
                ["start", "HN", "kj", "HN", "end"],
                ["start", "HN", "kj", "dc", "HN", "end"],
                ["start", "HN", "kj", "dc", "end"],
                ["start", "dc", "HN", "end"],
                ["start", "dc", "HN", "kj", "HN", "end"],
                ["start", "dc", "end"],
                ["start", "dc", "kj", "HN", "end"],
                ["start", "kj", "HN", "dc", "HN", "end"],
                ["start", "kj", "HN", "dc", "end"],
                ["start", "kj", "HN", "end"],
                ["start", "kj", "dc", "HN", "end"],
                ["start", "kj", "dc", "end"]
            ],
            sorted(valid_paths([], 'start', map_as_paths(connections)))
        )


if __name__ == "__main__":
    unittest.main()
