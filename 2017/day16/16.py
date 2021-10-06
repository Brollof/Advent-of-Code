from string import ascii_lowercase as abc


with open("input.txt") as file:
    moves = file.read().split(",")


def dance(moves, n):
    programs = list(abc[:16])
    for dance_idx in range(n % 60):
        for move in moves:
            if move[0] == 's':
                size = int(move[1:])
                programs = programs[-size:] + programs[:-size]
            elif move[0] == 'x':
                i1, i2 = move[1:].split("/")
                i1, i2 = int(i1), int(i2)
                programs[i1], programs[i2] = programs[i2], programs[i1]
            elif move[0] == 'p':
                p1, p2 = move[1:].split("/")
                i1, i2 = programs.index(p1), programs.index(p2)
                programs[i1], programs[i2] = programs[i2], programs[i1]
    return "".join(programs)


p1 = dance(moves, 1)
print(f"Part 1: {p1}")
assert "fnloekigdmpajchb" == p1


p2 = dance(moves, 1_000_000_000)
print(f"Part 2: {p2}")
assert "amkjepdhifolgncb" == p2
