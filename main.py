

"""
Created on Tue Jan 17 20:17:39 2023.

@author: jonin
"""
import pygame as pg
import sys
import grid
import numpy as np
from pygame.locals import QUIT
import copy
import time
import random

import Apple
import Snake
pg.init()
disx = 800
disy = 800
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

def ai_moves( moves):
        for move in moves:
            snake.ai_move(move)
            snake.plot()
            apple.plot()

            pg.display.update()
            Dis.fill(BLACK)
            time.sleep(0.2)
            events = pg.event.get()
            for event in events:
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
            
def ai(map_s):
    p_m = [ "Left", "Up", "Right", "Down"]
    c = 0
    while(1):
        
        moves = []
        c += 1
        for i in range(10):
            tmp_1 = random.randint(0,3)
            moves.append(p_m[tmp_1])

        tmp = snake.sim_moves(moves)
        if(type(tmp) != int and c > 5000):
           
            return moves[0]
        if(type(tmp)== int):
            if(tmp == 1):
                if (snake.legal_move(moves[0],snake.map_s)):
                    print(c)
                    return moves[0]

        
while running:
    
    #snake.sim_size = snake.size
    
    
            
        
   
   
    
    
    snake.ai_move(ai(snake.map_s))
    
    snake.plot()
    apple.plot()

    pg.display.update()
    Dis.fill(BLACK)
    time.sleep(0.2)
    events = pg.event.get()
    for event in events:
        if event.type == QUIT:
            pg.quit()
            sys.exit()
            

   
