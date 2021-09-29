with open('input.txt') as file:
    data = [int(line.strip()) for line in file.readlines()]

# to speed things up a little bit...
data = list(sorted(data))

def part1():
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]
    return 0



def part2():
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]
    return 0


print(part1())
print(part2())
