horizontal = 0
depth = 0

with open("input.txt", "r") as f:
    for movement in f:
        direction, distance = movement.split(" ")
        if direction == 'forward':
            horizontal += int(distance)
        elif direction == 'down':
            depth += int(distance)
        else:
            depth -= int(distance)

print(f"Final position: {horizontal}")
print(f"Final depth: {depth}")
print(horizontal * depth)
