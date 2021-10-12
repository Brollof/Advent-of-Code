import re


with open("inp5.txt") as file:
    data = file.read()


nice = 0
for s in data.splitlines():
    vowels = len(re.findall(r"[aeiou]", s)) >= 3
    twice = re.findall(r"(.)\1", s)
    contains = re.findall(r"(ab|cd|pq|xy)", s)
    if vowels and twice and not contains:
        nice += 1

print(f"Part 1: {nice}")
assert 258 == nice


nice = 0
for s in data.splitlines():
    pair = re.findall(r"(..).*\1", s)
    repeat = re.findall(r"(.).\1", s)
    if pair and repeat:
        nice += 1

print(f"Part 2: {nice}")
assert 53 == nice
