HALT = 99
ADD = 1
MULTIPLY = 2
GOAL = 19690720


def calc(intcode, inp1, inp2):
    index = 0
    intcode = list(intcode)
    intcode[1], intcode[2] = inp1, inp2

    while intcode[index] != HALT:
        opcode, i1, i2, ires = intcode[index: index + 4]
        if opcode == ADD:
            intcode[ires] = intcode[i1] + intcode[i2]
        elif opcode == MULTIPLY:
            intcode[ires] = intcode[i1] * intcode[i2]
        index += 4
    return intcode[0]


with open("input.txt") as file:
    data = file.read()

intcode = [int(val) for val in data.split(",")]

# part 1
print(calc(intcode, 12, 2))

# part 2
for noun, verb in ((j, i) for j in range(100) for i in range(100)):
    if calc(intcode, noun, verb) == GOAL:
        print(noun, verb, noun * 100 + verb)
        break