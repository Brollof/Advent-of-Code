with open('input.txt') as file:
    data = [line.strip() for line in file]


tr = str.maketrans('FBLR', '0101')
ids = sorted(int(seat.strip().translate(tr), 2) for seat in data)
lowest, highest = min(ids), max(ids)


# part 1
print(highest)

# part 2
print((lowest + highest) / 2 * (len(ids) + 1) - sum(ids))
