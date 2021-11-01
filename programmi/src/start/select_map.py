import pygame
import numpy as np
from src.colors import *
from src.start.functions import checkBT, create_grid, drawgrid

def select_map(WIDTH, HEIGHT):
    dir         = "./images/maps/"
    mapNames    = ["moon.png", "earth.png", "moon.png", "earth.png"]
    sceneNames  = ["moon.jpg", "moon.jpg", "moon.jpg", "moon.jpg"]
    dirScene    = "./images/scenarios/"
    # screen  = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen  = pygame.display.set_mode((WIDTH, HEIGHT))
    nCols   = 2
    nRows   = 2
    nMaps   = nCols * nRows
    spacex  = 20
    spacey  = 20
    shiftx  = 0
    shifty  = 0

    images  = [dir+name for name in mapNames]
    scenes  = [pygame.transform.scale(pygame.image.load(dirScene+name), (WIDTH, HEIGHT)) for name in sceneNames]
    x, y, lx, ly, pos   = create_grid(WIDTH, HEIGHT, nCols, nRows, spacex, spacey, shiftx, shifty)
    while True:
        screen.fill(BLACK)
        drawgrid(x, y, lx, ly, screen, images)
        x_mouse, y_mouse    = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # nx and ny are the col and row index of the selected player. nc the resulting
                dx      = WIDTH / nCols
                nx      = x_mouse // dx
                dy      = HEIGHT / nRows
                ny      = y_mouse // dy
                nc      = int(nx + ny * nCols)
                if nc >= nMaps:
                    nc -= nCols
                return nc, scenes[nc]

        pygame.display.update()

def selectGravity(map):
    gravity = np.array([1., 1., 0.6, 1.])
    return gravity[map]
