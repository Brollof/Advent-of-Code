import re


with open("input.txt") as file:
	data = file.read()


prev_len = 0
llen = len(data)

# remove cancelled characters
while prev_len != llen:
	data = re.sub(r"!.", "", data)
	prev_len = llen
	llen = len(data)


# remove garbage
l = len(data)
data, subs = re.subn(r"<.*?>", "", data)


# calculate score
level, score = 0, 0
for c in data:
	if c == '{':
		level += 1
	elif c == '}':
		score += level
		level -= 1

print(f"Part1: {score}")
assert 11347 == score

garbage_len = l - len(data) - subs * 2
print(f"Part2: {garbage_len}")
assert 5404 == garbage_len