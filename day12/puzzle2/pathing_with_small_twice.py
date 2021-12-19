import sys

from collections import defaultdict


def valid_paths(so_far, current, paths, small_twice=False):
    if current == 'end':
        return [so_far + [current]]
    elif so_far and current == 'start':
        return [[]]
    elif current.islower() and current in so_far:
        if small_twice:
            return [[]]
        else:
            small_twice = True
    return list(filter(
        None,
        [
            p for n in paths[current]
            for p in valid_paths(so_far + [current], n, paths, small_twice)
        ]
    ))


def map_as_paths(connections):
    paths = defaultdict(list)
    for conn in connections:
        start, end = conn.strip().split("-")
        paths[start].append(end)
        if start != 'start' and end != 'end':
            paths[end].append(start)
    return paths


def main(input_file):
    with open(input_file, "r") as f:
        paths = map_as_paths([path.strip() for path in f.readlines()])

    print(len(valid_paths([], 'start', paths)))


if __name__ == "__main__":
    main(sys.argv[1])
