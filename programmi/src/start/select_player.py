import numpy as np
import pygame
from src.start.functions import create_grid, drawgrid
from src.start.startWind import start
from src.colors import *

def select_player(WIDTH, HEIGHT, step, p):

    # Defining arrangement of the grid and number of players variable
    dir = "./images/characters/"
    screen      = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    chars       = ["Pi.jpeg", "Dan.jpeg", "Albi.jpeg", "Mt_Conta.jpeg", "Cinto.jpeg", "JD.jpeg", "Niscoreggia.jpeg", "Steve.jpeg"]
    n_players   = len(chars)
    n_cols      = 4
    n_rows      = n_players // n_cols
    chars       = [dir + chars[i] for i in range(n_players)]
    running     = True

    # Creating grid of players
    bottom      = 3*HEIGHT//4
    x, y, length, height, pos   = create_grid(WIDTH, bottom, n_cols, n_rows, 20, 20)

    # Reading stats and max stats
    maxStats    = np.loadtxt("./src/stat.txt", skiprows=1, max_rows=1)
    stats       = np.loadtxt("./src/stat.txt", skiprows=2)
    nStats      = len(maxStats)

    # Computing length of stats bars
    maxLen      = WIDTH//3
    l_bars      = np.zeros((n_players, nStats), np.int32)
    for i in range(n_players):
        l_bars[i, :] = stats[i, :] / maxStats[:] * maxLen

    # Creating grid of stats bars
    hTabBars    = HEIGHT - bottom
    x_bars, y_bars, lll, h_bars, pos    = create_grid(WIDTH, hTabBars, 1, nStats, 20, 20)     # lll is a dummy variable
    y_bars += bottom
    print(x_bars, y_bars, h_bars, pos)

    # Starting  while cycle for the player's selection
    player = np.zeros(2, np.int32) - 1
    while True:
        screen.fill(BLACK)
        drawgrid(x, y, length, height, screen, chars)
        (x_mouse,y_mouse) = pygame.mouse.get_pos()

        # correcting mouse position's reading
        if y_mouse >= bottom:
            y_mouse = bottom
        elif y_mouse < 0:
            y_mouse = 0
        # nx and ny are the col and row index of the selected player. nc the resulting
        dx      = WIDTH / n_cols
        nx      = x_mouse // dx
        dy      = (HEIGHT - HEIGHT//4) / n_rows
        ny      = y_mouse // dy
        nc      = int(nx + ny * n_cols)

        # Player selection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    if p == 0:
                        player[0]   = nc
                        p = 1
                    else:
                        if nc != player[0]:
                            player[1] = nc
                            return player
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if p==0:
                            start(WIDTH, HEIGHT)
                            screen.fill(BLACK)
                        elif p==1:
                            screen.fill(BLACK)
                            player[0], player[1]  = select_player(WIDTH, HEIGHT, 0, 0)
        if player[0] != -1 and player[1] != -1:
            quit()
        x_bars   = pos[:,0]
        y_bars   = pos[:,1]
        shifty  = 2*HEIGHT//3
        if p==0:
            # screen.blit(big_char_im[n_c], (0,0))
            for i in range(nStats):
                image   = pygame.Surface((l_bars[nc][i], h_bars))
                image.fill(GREEN)
                screen.blit(image, (x_bars[i], y_bars[i] + shifty))
        else:
            nq      = player[0]
            shiftx  = 2*WIDTH//3
            # screen.blit(big_char_im[nq], (0,0))
            # screen.blit(big_char_im[n_c], (WIDTH//3*2,0))
            for i in range(nStats):
                image   = pygame.Surface((l_bars[nq][i], h_bars))
                image.fill(GREEN)
                screen.blit(image, (x_bars[i], y_bars[i] + shifty))
                image   = pygame.Surface((l_bars[nc][i], h_bars))
                image.fill(GREEN)
                screen.blit(image, (shiftx+x_bars[i], y_bars[i] + shifty))
        pygame.display.update()
        if not running :
            quit()
