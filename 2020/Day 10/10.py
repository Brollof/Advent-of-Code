with open('input.txt') as file:
    data = [int(line.strip()) for line in file]

data = sorted(data)


current_joltage = 0
diffs = {1: 0, 2: 0, 3: 0}

for adapter in data:
    diff = adapter - current_joltage
    if diff <= 3:
        current_joltage += diff
        diffs[diff] += 1
    else:
        raise "O CHUJA"

current_joltage += 3
diffs[3] += 1

print(diffs, current_joltage)
# part1
print(diffs[1] * diffs[3])

# data = [16,10,15,5,1,11,7,19,6,12,4]
# data = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
# data = sorted(data)
# current_joltage = 0


def check(adapters, index=0):
    possible = []
    i = 1
    while index + i < len(adapters) and adapters[index + i] - adapters[index] <= 3:
        possible.append(adapters[index + i])
        i += 1
    # print(possible)
    return possible

#    0  1  2  3  4  5  6  7  8  9
r = [1, 3, 2, 1, 1, 2, 1, 1, 1, 1]
r1 = []
for i in range(len(data) - 1):
    r1.append(check(data, i))

# print(r1)



# cnt = 0
data.sort()
data.insert(0, 0)
# print(data)
call = 0
def check(adapters, seq=[0]):
    global call
    call += 1
    if call % 1_000_000 == 0:
        print(call)

    cv = seq[-1]
    ci = adapters.index(cv)
    possible = []
    for i in range(1, 4):
        if ci + i < len(adapters) and adapters[ci + i] - adapters[ci] <= 3:
            possible.append(adapters[ci + i])
    # print(possible)
    # print(possible, seq)
    # print(adapters[index], possible)
    # if index + 1 == len(adapters):
        # print(seq)
    if not possible:
        # print(seq)
        return 1

    cnt = 0
    for p in possible:
        # if seq[-1] < p:
        cnt += check(adapters, seq + [p])
    return cnt

a = check(data)
print(a)