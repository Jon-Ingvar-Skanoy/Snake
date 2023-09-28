

"""
Created on Tue Jan 17 20:17:39 2023.

@author: jonin
"""
import pygame as pg
import sys
import grid
import numpy as np
from pygame.locals import QUIT

import Apple
import Snake
pg.init()
disx = 1000
disy = 1000
gridx = 18
gridy = 18

map_s = np.zeros((gridx - 1, gridy - 1))
BLACK = (0,   0,   0)
grid = grid.Grid(gridx, gridy, disx, disy)
hexx, hexy = grid.getsize()

Dis = pg.display.set_mode((disx, disy), 0, 32)
pg.display.set_caption('Snake')
running = True
apple = Apple.Apple(Dis, hexx, hexy, map_s, grid)
snake = Snake.Snake(Dis, hexx, hexy, map_s, grid)
map_s[round(gridx/2), round(gridx/2)] = 1
map_s[round(gridx/5), round(gridx/2)] = 2

while running:
    snake.move()
    apple.plot()
    snake.plot()
    events = pg.event.get()
    for event in events:
        if event.type == QUIT:
            pg.quit()
            sys.exit()
            running = False

    pg.display.update()
    Dis.fill(BLACK)
