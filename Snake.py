
"""
Created on Tue Jan 17 20:40:26 2023.

@author: jonin
"""
import pygame as pg
import random
import sys
import numpy as np
import datetime
import copy
import time


class Snake():
    """Class on the Snake object."""
    sim_size = 0
    display = 0
    sizex = 0
    sizey = 0
    map_s = 0
    last_move = "None"
    next_move = "None"
    RED1 = (0,   250,   0)
    RED2 = (100,   170,   50)
    RED10 = (0,   250,   0)
    RED20 = (0,   100,   0)
    size = 30
    last = datetime.datetime.now()
    gsizex = 0
    gsizex = 0

    def __init__(self, dis, sizex, sizey, map_s, grid):
        self.display = dis
        self.sizex = sizex
        self.sizey = sizey
        self.map_s = map_s
        self.grid = grid
        self.gsizex = np.size(map_s[:, 0])
        self.gsizey = np.size(map_s[0, :])


    def legal_move(self,move,map_s):
        for x in range(0, self.gsizex):
                    for y in range(0, self.gsizey):
                        if (map_s[x, y] == 2):

                            if(move == "Left"):
                                if(x == 0 or map_s[x-1, y] < 0):
                                    return -1
                         
                                if(map_s[x-1, y] == 1):
                                    return 1
                                return 0
                              

                            elif(move == "Right"):
                                if(x == self.gsizex-1 or map_s[x+1, y] < 0):
                                    return -1

                          
                                if(map_s[x+1, y] == 1):
                                    return 1
                                return 0

                            elif(move == "Down"):
                                if(y == self.gsizey - 1 or map_s[x, y+1] < 0):
                                    return -1
                                
                                if(map_s[x, y+1] == 1):
                                    return 1
                                return 0

                            elif(move == "Up"):
                                if(y == 0 or map_s[x, y-1] < 0):
                                    return -1
                                
                                if(map_s[x, y-1] == 1):
                                    return 1
                                return 0
    def sim_move(self, move, tmp_map_s):
     

            #if (self.legal_move(move, tmp_map_s) == -1):
             #   return -1
            
            for x in range(0, self.gsizex):
                for y in range(0, self.gsizey):
                    if (tmp_map_s[x, y] == 2):

                        if(move == "Left"):
                            if(x == 0 or tmp_map_s[x-1, y] < 0):
                                return -2
                            tmp_map_s[x, y] = -self.size
                            if(tmp_map_s[x-1, y] == 1):
                                return 1
                            tmp_map_s[x-1, y] = 2
                           

                        elif(move == "Right"):
                            if(x == self.gsizex-1 or tmp_map_s[x+1, y] < 0):
                                return -2

                            tmp_map_s[x, y] = -self.size
                            if(tmp_map_s[x+1, y] == 1):
                                return 1
                            tmp_map_s[x+1, y] = 2
                           
                            

                        elif(move == "Down"):
                            if(y == self.gsizey - 1 or tmp_map_s[x, y+1] < 0):
                                return -2
                            tmp_map_s[x, y] = -self.size
                            if(tmp_map_s[x, y+1] == 1):
                                return 1
                            tmp_map_s[x, y+1] = 2
                            

                        elif(move == "Up"):
                            if(y == 0 or tmp_map_s[x, y-1] < 0):
                               return -2
                            tmp_map_s[x, y] = -self.size
                            if(tmp_map_s[x, y-1] == 1):
                                return 1
                            tmp_map_s[x, y-1] = 2
                          

                        for x1 in range(0, self.gsizex):
                            for y1 in range(0, self.gsizey):
                                if tmp_map_s[x1, y1] < 0:
                                    tmp_map_s[x1, y1] += 1
                        return tmp_map_s
    def move(self):
        """For  the Snake object movement."""
        pressed_keys = pg.key.get_pressed()
        if(pressed_keys[pg.K_LEFT] and self.next_move != "Right"):
            self.next_move = "Left"
        if(pressed_keys[pg.K_RIGHT] and self.next_move != "Left"):
            self.next_move = "Right"
        if(pressed_keys[pg.K_DOWN] and self.next_move != "Up"):
            self.next_move = "Down"
        if(pressed_keys[pg.K_UP] and self.next_move != "Down"):
            self.next_move = "Up"

        now = datetime.datetime.now()
        if((now-self.last).total_seconds() < 0.11):
            return

        if(self.next_move != "None"):

            if (self.legal_move(self.next_move, self.map_s) == -1):
                
                pg.quit()
                sys.exit()
            for x in range(0, self.gsizex):
                for y in range(0, self.gsizey):
                    if (self.map_s[x, y] == 2 and (now-self.last).total_seconds() > 0.1):

                        if(self.next_move == "Left"):
                            if(x == 0 or self.map_s[x-1, y] < 0):
                                pg.quit()
                                sys.exit()
                            self.map_s[x, y] = -self.size
                            if(self.map_s[x-1, y] == 1):
                                self.size += 1
                                self.eaten()
                            self.map_s[x-1, y] = 2
                            self.last_move = self.next_move
                            self.last = now

                        elif(self.next_move == "Right"):
                            if(x == self.gsizex-1 or self.map_s[x+1, y] < 0):
                                pg.quit()
                                sys.exit()

                            self.map_s[x, y] = -self.size
                            if(self.map_s[x+1, y] == 1):
                                self.size += 1
                                self.eaten()
                            self.map_s[x+1, y] = 2
                            self.last_move = self.next_move
                            self.last = now

                        elif(self.next_move == "Down"):
                            if(y == self.gsizey - 1 or self.map_s[x, y+1] < 0):
                                pg.quit()
                                sys.exit()
                            self.map_s[x, y] = -self.size
                            if(self.map_s[x, y+1] == 1):
                                self.size += 1
                                self.eaten()
                            self.map_s[x, y+1] = 2
                            self.last_move = self.next_move
                            self.last = now

                        elif(self.next_move == "Up"):
                            if(y == 0 or self.map_s[x, y-1] < 0):
                                pg.quit()
                                sys.exit()
                            self.map_s[x, y] = -self.size
                            if(self.map_s[x, y-1] == 1):
                                self.size += 1
                                self.eaten()
                            self.map_s[x, y-1] = 2
                            self.last_move = self.next_move
                            self.last = now

                        for x1 in range(0, self.gsizex):
                            for y1 in range(0, self.gsizey):
                                if self.map_s[x1, y1] < 0:
                                    self.map_s[x1, y1] += 1

    def plot(self):
        """Plott of the Snake object."""
        for x in range(0, self.gsizex):
            for y in range(0, self.gsizey):
                if self.map_s[x, y] == 2:
                    tmpx, tmpy = self.grid.pos(x, y)
                    pg.draw.rect(self.display, self.RED1, (tmpx, tmpy, self.sizex, self.sizey))
                if self.map_s[x, y] < 0:
                    tmpx, tmpy = self.grid.pos(x, y)
                    pg.draw.rect(self.display,(50,   70+ 5*(-self.map_s[x, y]),   100) , (tmpx, tmpy, self.sizex, self.sizey))

    def eaten(self):
        """For when the snake eats a apple."""
        for x in range(0, self.gsizex):
            for y in range(0, self.gsizey):
                if self.map_s[x, y] == 1:
                    self.map_s[x, y] = 0
        for x1 in range(0, self.gsizex):
            for y1 in range(0, self.gsizey):
                if self.map_s[x1, y1] < 0:
                    self.map_s[x1, y1] -= 1
        while 1:
            newposx = random.randint(0, self.gsizex-1)
            newposy = random.randint(0, self.gsizey-1)
            if(self.map_s[newposx, newposy] == 0):
                self.map_s[newposx, newposy] = 1
                return 0
            
    def sim_moves(self,moves):
        self.sim_size = self.size
        tmp_s_map = copy.deepcopy(self.map_s)

        for move in moves:
            
            tmp_s_map = self.sim_move(move,tmp_s_map)
            if (type(tmp_s_map) == int):
                return tmp_s_map
        return tmp_s_map
    
    def ai_move(self, move):
        """For  the Snake object movement."""
        
        
        self.next_move = move
        

      
        

        if(self.next_move != "None"):

        
            #    pg.quit()
             #   sys.exit()
            for x in range(0, self.gsizex):
                for y in range(0, self.gsizey):
                    if (self.map_s[x, y] == 2):
                        moved = False
                        if(self.next_move == "Left"):
                            if(x == 0 or self.map_s[x-1, y] < 0):
                                pg.quit()
                                sys.exit()
                            self.map_s[x, y] = -self.size
                            if(self.map_s[x-1, y] == 1):
                                self.size += 1
                                self.eaten()
                            self.map_s[x-1, y] = 2
                            self.last_move = self.next_move
                            moved = True
                        

                        elif(self.next_move == "Right"):
                            if(x == self.gsizex-1 or self.map_s[x+1, y] < 0):
                                pg.quit()
                                sys.exit()

                            self.map_s[x, y] = -self.size
                            if(self.map_s[x+1, y] == 1):
                                self.size += 1
                                self.eaten()
                            self.map_s[x+1, y] = 2
                            self.last_move = self.next_move
                            moved = True
                            

                        elif(self.next_move == "Down"):
                            if(y == self.gsizey - 1 or self.map_s[x, y+1] < 0):
                                pg.quit()
                                sys.exit()
                            self.map_s[x, y] = -self.size
                            if(self.map_s[x, y+1] == 1):
                                self.size += 1
                                self.eaten()
                            self.map_s[x, y+1] = 2
                            self.last_move = self.next_move
                            moved = True
                            

                        elif(self.next_move == "Up"):
                            if(y == 0 or self.map_s[x, y-1] < 0):
                                pg.quit()
                                sys.exit()
                            self.map_s[x, y] = -self.size
                            if(self.map_s[x, y-1] == 1):
                                self.size += 1
                                self.eaten()
                            self.map_s[x, y-1] = 2
                            self.last_move = self.next_move
                            moved = True
                           
                        if(moved):
                            for x1 in range(0, self.gsizex):
                                for y1 in range(0, self.gsizey):
                                    if self.map_s[x1, y1] < 0:
                                        self.map_s[x1, y1] += 1
                        return
            
            
    
