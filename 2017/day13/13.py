with open("input.txt") as file:
	data = file.read()

layers = {}

for line in data.splitlines():
	idd, r = line.split(": ")
	idd, r = int(idd), int(r)
	layers[idd] = r


def calc_severity(layers):
    severity = 0
    for idd, r in layers.items():
        if idd % ((r - 1) * 2) == 0:
            severity += idd * r
    return severity


severity = calc_severity(layers)
print(f"Part 1: {severity}")
assert 1632 == severity

#############################################################################
#############################################################################

delay = 0
while any((delay + idd) % ((r - 1) * 2) == 0 for idd, r in layers.items()):
    delay += 1

print(f"Part 2: {delay}")
assert 3834136 == delay