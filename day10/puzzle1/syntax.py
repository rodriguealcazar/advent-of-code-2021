import sys


PAIRS = {
    ')': "(",
    ']': "[",
    '}': "{",
    '>': "<"
}


POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def line_score(line):
    opened = []
    score = 0
    for c in line:
        if c in ["(", "[", "{", "<"]:
            opened.append(c)
        elif c in [")", "]", "}", ">"]:
            if not opened or opened[-1] != PAIRS[c]:
                score = POINTS[c]
                break
            else:
                opened.pop()
    return score


def main(input_file):
    with open(input_file, "r") as f:
        score = 0
        for l in f.readlines():
            line = l.strip()
            score += line_score(line)
    print(f"Final score: {score}")


if __name__ == "__main__":
    main(sys.argv[1])
