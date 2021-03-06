previous = None
increasing_depths = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        next_reading = int(line)
        if previous and next_reading > previous:
            increasing_depths += 1
        previous = next_reading

print(f"Number of increasing depths: {increasing_depths}")
