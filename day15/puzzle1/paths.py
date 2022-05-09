import sys


def lowest_risk(risks):
    rows = len(risks)
    columns = len(risks[0])
    costs = [[0 for _ in range(rows)] for _ in range(columns)]

    costs[0][1] = risks[0][1]
    costs[1][0] = risks[1][0]

    for i in range(1, columns):
        for j in range(0, rows):
            neighbours = []
            if i - 1 >= 0:
                neighbours.append(costs[i - 1][j])
            if i + 1 < columns:
                neighbours.append(costs[i + 1][j])
            if j - 1 >= 0:
                neighbours.append(costs[i][j - 1])
            if j + 1 < rows:
                neighbours.append(costs[i][j + 1])

            costs[i][j] = min(neighbours) + risks[i][j]

    return costs


def main(input_file):
    with open(input_file, "r") as f:
        risk_map = [[int(c) for c in line.strip()] for line in f]

    costs = lowest_risk(risk_map, )
    print(f"Lowest risk: {costs[-1][-1]}")


if __name__ == "__main__":
    main(sys.argv[1])
