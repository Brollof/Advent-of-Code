import numpy as np


def check_board(board):
    for row in board:
        if set(row).issubset(drawn):
            return True
    for col in board.T:
        if set(col).issubset(drawn):
            return True
    return False


def find_winner(boards):
    winner = None
    for i, board in enumerate(boards):
        if board is not None and check_board(board):
            boards[i] = None
            if winner is None:
                winner = board
    return winner


with open("inp4.txt") as file:
    data = file.read()


numbers, *boards_raw = data.split('\n\n')
numbers = [int(num) for num in numbers.split(',')]
boards = [np.array([int(n) for n in s.split()]).reshape(5, 5) for s in boards_raw]

p1 = None
for i in range(5, len(numbers) + 1):
    drawn = set(numbers[:i])
    if (board := find_winner(boards)) is not None:
        score = sum(set(board.flatten()) - drawn) * numbers[i - 1]
        if p1 is None:
            p1 = score


print(f"Part 1: {p1}")
assert 55770 == p1

print(f"Part 2: {score}")
assert 2980 == score
