import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLife:
    def __init__(self, grid_size, initial_state=None):
        self.grid_size = grid_size
        if initial_state is None:
            self.grid = np.random.choice([0, 1], size=(grid_size, grid_size))
        else:
            self.grid = initial_state
        self.rules = (2, 3, 3)  # Default rules: (min_survive, max_survive, reproduce)

    def update_grid(self):
        new_grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                live_neighbors = self.count_live_neighbors(row, col)
                if self.grid[row, col] == 1:
                    if self.rules[0] <= live_neighbors <= self.rules[1]:
                        new_grid[row, col] = 1
                    else:
                        new_grid[row, col] = 0
                else:
                    if live_neighbors == self.rules[2]:
                        new_grid[row, col] = 1
        self.grid = new_grid

    def count_live_neighbors(self, row, col):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                total += self.grid[(row + i) % self.grid_size, (col + j) % self.grid_size]
        return total

    def update_rules(self, min_survive, max_survive, reproduce):
        self.rules = (min_survive, max_survive, reproduce)

    def run(self, generations, interval):
        fig, ax = plt.subplots()
        img = ax.imshow(self.grid, cmap='binary')

        def update(*args):
            self.update_grid()
            img.set_data(self.grid)
            return img,

        ani = animation.FuncAnimation(fig, update, frames=generations, interval=interval, blit=True)
        plt.show()

if __name__ == "__main__":
    grid_size = 50
    generations = 100
    interval = 200  # milliseconds
    initial_state = None

    game = GameOfLife(grid_size, initial_state)

    while True:
        try:
            min_survive = int(input("Enter the minimum number of live neighbors for survival: "))
            max_survive = int(input("Enter the maximum number of live neighbors for survival: "))
            reproduce = int(input("Enter the exact number of live neighbors for reproduction: "))
            game.update_rules(min_survive, max_survive, reproduce)
            break
        except ValueError:
            print("Please enter valid integers.")

    game.run(generations, interval)
