import numpy as np
import pygame
from numba import jit

# Function to create a grid given as input at least w, h, n_cols, n_rows
@jit(nopython=True, fastmath=True)
def create_grid(w, h, n_cols=1, n_rows=1, spacex=0, spacey=0, shiftx=0, shifty=0):
    x   = np.zeros(n_cols, np.int32)
    y   = np.zeros(n_rows, np.int32)
    pos = np.zeros((n_rows*n_cols, 2), np.int32)
    lx  = w//n_cols-spacex
    ly  = h//n_rows-spacey
    for i in range(n_cols):
        x[i]    = shiftx + i*(w/n_cols) + spacex/2
    for j in range(n_rows):
        y[j]    = shifty + j*(h/n_rows) + spacey/2
    for i in range(n_cols * n_rows):
        pos[i,0]  = x[i%n_cols]
        print(y[i//n_cols])
        pos[i,1]  = y[i//n_cols]
    # print(x, y, pos)
    return (x, y, lx, ly, pos)

# Function to draw grid. It gets problem when using integer instead of array bc of x[i]
def drawgrid(X, Y, l, h, screen, images):
    import pygame
    n_cols  = X.size
    for i in range(n_cols):
        for j in range(Y.size):
            char    = pygame.image.load(images[i + j*n_cols])
            char    = pygame.transform.scale(char, (l, h))
            screen.blit(char, (X[i], Y[j]))

# Function to check if the parameter is between the interval
@jit(nopython=True)
def checkBT(x, x1, x2):
    temp1   = min(x1, x2)
    temp2   = x1 + x2 - temp1
    return x < temp2 and x > temp1
