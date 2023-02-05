"""
Created on Tue Jan 17 22:22:02 2023.

@author: jonin
"""

import pygame as pg
import numpy as np


class Apple():
    """Class on the Apple object."""

    display = 0
    sizex = 0
    sizey = 0
    map_s = 0
    RED = (255,   0,   0)
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

    def plot(self):
        """Plott of the Apple object."""
        for x in range(0, self.gsizex):
            for y in range(0, self.gsizey):
                if self.map_s[x, y] == 1:
                    tmpx, tmpy = self.grid.pos(x, y)
                    pg.draw.rect(self.display, self.RED, (tmpx, tmpy, self.sizex, self.sizey))
