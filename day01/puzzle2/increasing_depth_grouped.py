previous = None
increasing_depths = 0
with open("input.txt", "r") as f:
    measurements = f.readlines()
    for i in range(len(measurements) - 2):
        current_window = sum(map(int, measurements[i:i+3]))
        if previous and current_window > previous:
            increasing_depths += 1
        previous = current_window

print(f"Number of increasing depths: {increasing_depths}")
