import numpy as np

class Tile:
    def __init__(self, idd, grid_str):
        self.id = idd
        self.grid = np.array([list(row) for row in grid_str.splitlines()])

    def __eq__(self, o):
        return self.id == o.id

    def __repr__(self):
        return f"{self.id}"

    def get_str(self):
        return '\n'.join(''.join(row) for row in self.grid)

    def print(self):
        print(self.get_str())

    def rotateLeft(self, k=1):
        self.grid = np.rot90(self.grid, k=k)

    def flipx(self):
        self.grid = np.fliplr(self.grid)

    def check(self, o, d):
        if d == 'top': # check my top edge against other bottom
            return list(self.grid[0]) == list(o.grid[-1])
        if d == 'bot':
            return list(self.grid[-1]) == list(o.grid[0])
        if d == 'left':
            return [row[0] for row in self.grid] == [row[-1] for row in o.grid]
        if d == 'right':
            return [row[-1] for row in self.grid] == [row[0] for row in o.grid]