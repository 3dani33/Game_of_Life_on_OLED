"""Game of Life implementation."""

import numpy as np
from copy import deepcopy


class GameOfLife:
    width: int
    height: int
    grid: np.array
    generation: int
    neighbour_idx = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    
    def __init__(self, width: int, height: int, random=False):
        """Initialise empty grid with specified width and height."""
        self.width = width
        self.heigth = height
        if random:
            self.grid = np.random.rand(width, height) > 0.9
        else:
            self.grid = np.array([[False] * height] * width)  # generate empty grid
        self.generation = 0
    
    @classmethod
    def fromArray(cls, grid):
        """Initialise with the passed grid."""
        gol = GameOfLife(len(grid), len(grid[0]))
        gol.grid = grid
        return gol
    
    def next(self) -> np.array:
        """Generate the next generation and return the new grid."""
        old_grid = deepcopy(self.grid)  # copy old grid
        for x in range(self.width):
            for y in range(self.heigth):
                # for each cell, count neighbours in old_grid
                neighbours = 0
                for x_, y_ in self.neighbour_idx:
                    x_idx = x + x_
                    y_idx = y + y_
                    # check bounds
                    if x_idx >= self.width:
                        x_idx = 0
                    if y_idx >= self.heigth:
                        y_idx = 0

                    if old_grid[x_idx, y_idx]:
                        neighbours += 1
                # rules:
                # 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                # 2. Any live cell with two or three live neighbours lives on to the next generation.
                # 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
                # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                if old_grid[x, y]:
                    # a live cell with two or three live neighbours survives
                    self.grid[x, y] = neighbours == 2 or neighbours == 3
                else:
                    # a dead cell with exactly three neighbours becomes a live cell
                    self.grid[x, y] = neighbours == 3
        self.generation += 1
        return self.grid

    def __str__(self):
        string = '+' + '-'*self.width + '+\n'
        for y in range(self.heigth):
            string += '|'
            for cell in self.grid[:,y]:
                string += 'O' if cell else ' '
            string += '|\n'
        string += '+' + '-'*self.width + '+\n'
        return string


if __name__ == '__main__':
    print("Press enter for the next generation and enter a 'q' to quit.")
    n = 0
    gol = GameOfLife(20, 10, True)
    print(gol)
    while 'q' not in input():
        gol.next()
        n += 1
        print(f'generation {n}')
        print(gol)