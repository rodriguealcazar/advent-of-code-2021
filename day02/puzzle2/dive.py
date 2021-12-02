horizontal = 0
depth = 0
aim = 0

with open("input.txt", "r") as f:
    for movement in f:
        direction, distance = movement.split(" ")
        if direction == 'forward':
            horizontal += int(distance)
            depth += int(distance) * aim
        elif direction == 'down':
            aim += int(distance)
        else:
            aim -= int(distance)

print(f"Final position: {horizontal}")
print(f"Final depth: {depth}")
print(horizontal * depth)

