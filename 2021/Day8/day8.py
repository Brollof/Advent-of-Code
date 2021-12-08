def get_2(digits, one, seven, four):
    for digit in digits:
        if len(digit - one - seven - four) == 2:
            return digit
    assert False, f"2 cannot be calculated from {digits=} using {one=}, {seven=} and {four=}"


def get_3(digits, two):
    for digit in digits:
        if len(digit - two) == 1:
            return digit
    assert False, f"3 cannot be calculated from {digits=} using {two=}"


def get_9(digits, three):
    for digit in digits:
        if len(digit - three) == 1:
            return digit
    assert False, f"9 cannot be calculated from {digits=} using {three=}"


def get_0(digits, five):
    for digit in digits:
        if len(digit - five) == 2:
            return digit
    assert False, f"0 cannot be calculated from {digits=} using {five=}"


def process_entry(patterns: list, output: list):
    one = [set(p) for p in patterns if len(p) == 2][0]
    seven = [set(p) for p in patterns if len(p) == 3][0]
    four = [set(p) for p in patterns if len(p) == 4][0]
    eight = [set(p) for p in patterns if len(p) == 7][0]
    two_three_five = [set(p) for p in patterns if len(p) == 5]
    zero_six_nine = [set(p) for p in patterns if len(p) == 6]
    two = get_2(two_three_five, one, seven, four)
    three_five = [digit for digit in two_three_five if digit != two]
    three = get_3(three_five, two)
    five = [digit for digit in three_five if digit != three][0]
    nine = get_9(zero_six_nine, three)
    zero = get_0(zero_six_nine, five)
    zero_six_nine.remove(zero)
    zero_six_nine.remove(nine)
    six = zero_six_nine[0]

    digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    value = ''.join(str(digits.index(set(d))) for d in output)
    return int(value)


with open("inp8.txt") as file:
    data = file.read()


p1, p2 = 0, 0
for line in data.splitlines():
    patterns, output = line.split(' | ')
    patterns, output = patterns.split(), output.split()
    p1 += sum(1 for digit in output if len(digit) in (2, 3, 4, 7))
    p2 += process_entry(patterns, output)


print(f"Part 1: {p1}")
assert p1 == 344

print(f"Part 2: {p2}")
assert p2 == 1048410
