import re


with open("inp11.txt") as file:
    password = file.read()


def inc_str(s):
    temp = s.rstrip('z')
    out = temp[:-1] + chr(ord(temp[-1]) + 1)
    out += 'a' * (len(s) - len(temp))
    return out


def new_password(password):
    while True:
        password = inc_str(password)

        # cannot contain
        if 'i' in password or 'l' in password or 'o' in password:
            continue

        # increased 3 letters
        inc = False
        for i in range(len(password) - 2):
            if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i + 1]) + 1 == ord(password[i + 2]):
                inc = True

        # two non-overlapping pairs
        two_pairs = len(re.findall(r"(.)\1", password)) >= 2

        if inc and two_pairs:
            return password


p1 = new_password(password)
print(f"Part 1: {p1}")
assert "vzbxxyzz" == p1

p2 = new_password(p1)
print(f"Part 2: {p2}")
assert "vzcaabcc" == p2
