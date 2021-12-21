from math import ceil, floor


def build_list(arr):
    level = -1
    num = ''
    out = []
    for c in str(arr):
        if c.isdigit():
            num += c
        elif num != '':
            out.append((int(num), level))
            num = ''

        if c == '[':
            level += 1
        elif c == ']':
            level -= 1
    return out


def explode(arr):
    for i in range(len(arr) - 1):
        if arr[i][1] == 4 and arr[i + 1][1] == 4:
            if i > 0:
                v, depth = arr[i - 1]
                arr[i - 1] = (arr[i][0] + v, depth)
            if i < len(arr) - 2:
                v, depth = arr[i + 2]
                arr[i + 2] = (arr[i + 1][0] + v, depth)

            arr[i] = (0, arr[i][1] - 1)
            del arr[i + 1]
            return True
    return False


def split(arr):
    for i in range(len(arr)):
        value, depth = arr[i]
        if value >= 10:
            left, right = floor(value / 2), ceil(value / 2)
            arr[i] = (left, depth + 1)
            arr.insert(i + 1, (right, depth + 1))
            return True
    return False


def reduce(arr):
    while explode(arr) or split(arr):
        pass


def add(a1, a2):
    return [(v, d + 1) for v, d in a1 + a2]


def calc_magnitude(arr):
    arr = arr[::]
    while len(arr) >= 2:
        for i in range(len(arr) - 1):
            if arr[i][1] == arr[i + 1][1]:
                m = arr[i][0] * 3 + arr[i + 1][0] * 2
                arr[i] = (m, arr[i][1] - 1)
                del arr[i + 1]
                break
    return arr[0][0]


def part1(s):
    current = None
    for line in s.splitlines():
        arr = eval(line)
        arr = build_list(arr)

        if current is None:
            current = arr
        else:
            current = add(current, arr)
            reduce(current)
    return calc_magnitude(current)


def part2(s):
    numbers = []
    for line in s.splitlines():
        arr = eval(line)
        arr = build_list(arr)
        numbers.append(arr)

    biggest_mag = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):

            result = add(numbers[i], numbers[j])
            reduce(result)
            biggest_mag = max(biggest_mag, calc_magnitude(result))

            result = add(numbers[j], numbers[i])
            reduce(result)
            biggest_mag = max(biggest_mag, calc_magnitude(result))

    return biggest_mag


with open("inp18.txt") as file:
    data = file.read()


p1 = part1(data)
print(f"Part 1: {p1}")
assert p1 == 4391


p2 = part2(data)
print(f"Part 2: {p2}")
assert p2 == 4626
