from collections import Counter

is_increasing = lambda x: [*str(x)] == sorted(str(x))

def get_range():
    with open("input.txt") as file:
        return map(int, file.read().split("-"))


def same_digits1(x):
    c = Counter(list(str(x)))
    for v in c.values():
        if v > 1:
            return True
    return False


def same_digits2(x):
    c = Counter(list(str(x)))
    return 2 in c.values()


min_r, max_r = get_range()

# part 1
cnt = sum(1 for n in range(min_r, max_r + 1) if is_increasing(n) and same_digits1(n))
print(cnt)

# part 2
cnt = sum(1 for n in range(min_r, max_r + 1) if is_increasing(n) and same_digits2(n))
print(cnt)