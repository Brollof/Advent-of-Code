import re
import json


with open("inp12.txt") as file:
    data = file.read()


p1 = sum(map(int, re.findall(r"-?\d+", data)))
print(f"Part 1: {p1}")
assert 156366 == p1


def go(obj):
    if type(obj) == dict:
        if 'red' in (x for x in obj.values() if type(x) == str):
            return 0
        to_check = obj.values()
    elif type(obj) == list:
        to_check = obj
    elif type(obj) == int:
        return obj
    else:
        return 0

    return sum(go(o) for o in to_check)


p2 = go(json.loads(data))
print(f"Part 2: {p2}")
assert 96852 == p2
