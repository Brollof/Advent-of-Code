with open("input.txt") as file:
	data = file.read()

tree = {}

for line in data.splitlines():
	id, comm = line.replace(' ', '').split("<->")
	comm = comm.split(",")
	tree[id] = comm


def traverse(check_id):
	to_check = tree[check_id]
	checked = set()

	while len(to_check):
		if (idd := to_check.pop()) not in checked:
			checked.add(idd)
			to_check.extend(tree[idd])

	return checked


group = traverse('0')
print(f"Part 1: {len(group)}")
assert 288 == len(group)


programs = set(tree.keys())
groups_cnt = -1 # ???

while len(programs):
	groups_cnt += 1
	idd = next(iter(programs))
	group = traverse(idd)
	programs -= group


print(f"Part 2: {groups_cnt}")
assert 211 == groups_cnt