
"""
Created on Tue Jan 17 20:43:11 2023.

@author: jonin
"""

from math import trunc


class Grid():
    """Grid."""

    sizex = 0
    sizey = 0
    dissizex = 0
    dissizey = 0

    gridx = 0
    gridy = 0

    def __init__(self, sizex, sizey, dissizex, dissizey):
        self.sizex = sizex
        self.sizey = sizey
        self.dissizex = dissizex
        self.dissizey = dissizey

        self.gridx = trunc(dissizex / (sizex))
        self.gridy = trunc(dissizey / (sizey))

    def pos(self, x, y):
        """Recives the grid pos.

        returns picsel possision
        """
        renx = (x)*self.gridx + self.gridx / 2
        reny = (y)*self.gridy + self.gridy / 2
        return renx, reny

    def getsize(self):
        """Retruns size of gridhex."""
        return self.gridx, self.gridy
