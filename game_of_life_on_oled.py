"""Conway's Game of Life on a OLED display."""
from PIL import Image
import numpy as np
import time

import display
from game_of_life import GameOfLife


if __name__ == '__main__':
    print("Starting Game of Life on OLED display.")
    print('Initialising display...')
    display.init()
    print('Create Random Game of Life...')
    gol = GameOfLife(display.WIDTH, display.HEIGHT, random=True)
    print('Starting Game of Life.')
    try:
        while True:
            print(f'generation {gol.generation}')
            # convert numpy array to binary image
            im = Image.fromarray(np.rot90(gol.grid))
            display.show_image(im)
            gol.next()
            time.sleep(0.05)
    except KeyboardInterrupt:
        print('\nExiting.')
        display.deinit()