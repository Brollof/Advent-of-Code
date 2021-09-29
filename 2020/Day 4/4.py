import re


with open('input.txt') as file:
    passports = file.read().split('\n\n')


def check_height(x):
    if m := re.match(r'^(\d{1,})(cm|in)$', x):
        if m[2] == 'cm' and 150 <= int(m[1]) <= 193:
            return True
        elif m[2] == 'in' and 59 <= int(m[1]) <= 76:
            return True
    return False


# Validation rules
V = {
    'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    'hgt': check_height,
    'hcl': lambda x: re.match(r'#[a-f0-9]{6}', x),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: len(x) == 9 and x.isdigit()
}


part1, part2 = 0, 0
for p in passports:
    d = dict(x.split(':') for x in p.replace('\n', ' ').split(' '))
    if all(prop in d for prop in V):
        part1 += 1
        if all(test(d[prop]) for prop, test in V.items()):
            part2 += 1


print(part1)
print(part2)