from collections import deque

with open('input.txt', 'r') as f:
    data = [int(x.strip()) for x in f.readlines()]

data = [16,10,15,5,1,11,7,19,6,12,4]


data.append(0)
data.sort()
data.append(max(data)+3)
print(data)
ones = 0
threes = 0
for low, high in zip(data, data[1:]):
    if high - low == 3:
        threes += 1
    elif high - low == 1:
        ones += 1
print('Part 1:', ones*threes)

index = {x: [y for y in data if y>x and y-x <= 3] for x in data}
print(index)
results = {}

def partTwo(joltages):
    compatible = {}
    for i, joltage in enumerate(joltages[:-1]):
        compatible[joltage] = [j for j in joltages[i+1:i+4] if j - joltage <= 3]

    numArrangements = {joltages[-1]: 1}
    # print(numArrangements)
    for joltage in reversed(joltages[:-1]):
        print(numArrangements, compatible[joltage])
        numArrangements[joltage] = sum(numArrangements[j] for j in compatible[joltage])

    return numArrangements[0]


a = partTwo(data)
print(a)