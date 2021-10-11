from hashlib import md5


with open("inp4.txt") as file:
    data = file.read()


i = 1
five = None
six = None

while True:
    hash = md5(f"{data}{i}".encode("utf-8")).hexdigest()
    if not five and hash.startswith("00000"):
        five = i
    elif not six and hash.startswith("000000"):
        six = i
        break
    i += 1


print(f"Part 1: {five}")
assert 346386 == five

print(f"Part 2: {six}")
assert 9958218 == six
