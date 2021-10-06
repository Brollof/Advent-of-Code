import sys
sys.path.append("..")
from knot import *

def main():
	with open("input.txt") as file:
		data = file.read().strip()

	lens = [int(n) for n in data.split(',')]
	table = knot_rounds(lens, rounds=1)

	p1 = table[0] * table[1]
	print(f"Part 1: {p1}")
	assert 37230 == p1

	#############################################################################################
	#############################################################################################

	part2 = knot_hash(data)
	print(f"Part 2: {part2}")
	assert "70b856a24d586194331398c7fcfa0aaf" == part2


if __name__ == '__main__':
	main()