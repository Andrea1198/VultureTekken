import pygame
import numpy as np
from src.start.functions import checkBT, create_grid, drawgrid

def select_map(WIDTH, HEIGHT):
    dir     = "./images/"
    mapNames= ["moon.png", "earth.png"]

    nCols   = 2
    nRows   = 2
    spacex  = 20
    spacey  = 20
    shiftx  =

    images  = [dir+name for name in mapNames]
    x, y, lx, ly, pos   = create_grid(WIDTH, HEIGHT, nCols, nRows, spacex, spacey, shiftx, shifty)
    drawgrid(pos[:,0], pos(:,1), lx, ly, screen, images)
