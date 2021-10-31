import pygame
import numpy as np
from src.colors import *
def create_grid(w, h, n_col=1, n_row=1, spacex=0, spacey=0, shiftx=0, shifty=0):
    x=np.zeros(n_col*n_row, np.int32)
    y=np.zeros(n_col*n_row, np.int32)
    lx  = w/n_col-spacex
    ly  = h/n_row-spacey
    for i in range(n_col*n_row):
        xx      = shiftx + i%n_col*(w/n_col) + spacex/2
        yy      = shifty + i//n_col*(h/n_row) + spacey/2
        x[i]    = xx
        y[i]    = yy
    return (x, y, lx, ly)

def drawgrid(X, Y, l, h, screen, images):
    import pygame
    screen.fill(BLACK)
    for i in range(X.size):
        char    = pygame.image.load(images[i])
        char    = pygame.transform.scale(char, (l, h))
        screen.blit(char, (X[i], Y[i]))


    pygame.display.update()


# Schermata iniziale

def start(WIDTH, HEIGHT):
    import pygame
    running = True
    dir = "./images/start/"
    background  = "background.jpg"
    start       = ["start_selected.png", "start_not_selected.png"]
    exit        = ["quit_not_selected.png", "quit_selected.png"]

    i   = 0
    screen  = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    bkg = pygame.image.load(dir+background)
    bkg = pygame.transform.scale(bkg, (WIDTH, HEIGHT))
    while running:
        (x_mouse, y_mouse)  = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if y_mouse < HEIGHT*3//4 and y_mouse > HEIGHT // 2:
                i = 0
            else:
                i = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if i==0:
                    running = False
                else:
                    pygame.quit()
        btn1    = pygame.image.load(dir+start[i])
        btn1    = pygame.transform.scale(btn1, (WIDTH//2, HEIGHT//4))
        btn2    = pygame.image.load(dir+exit[i])
        btn2    = pygame.transform.scale(btn2, (WIDTH//2, HEIGHT//4))
        screen.blit(bkg, (0,0))
        screen.blit(btn1,(WIDTH//4,HEIGHT//2))
        screen.blit(btn2,(WIDTH//4,HEIGHT//4*3))
        pygame.display.update()

# La funzione deve mostrare le icone con i vari personaggi per selezionarne uno e dare in uscita un intero

def select_player(WIDTH, HEIGHT, step, p):
    from numpy import loadtxt

    dir = "./images/characters/"
    screen      = pygame.display.set_mode((WIDTH, HEIGHT))
    chars       = ["Pi.jpeg", "Dan.jpeg", "Albi.jpeg", "Mt_Conta.jpeg", "Cinto.jpeg", "JD.jpeg", "Niscoreggia.jpeg", "Steve.jpeg"]
    n           = len(chars)
    chars       = [dir + chars[i] for i in range(n)]
    running     = True
    n_row       = 2
    n_col       = 4
    (x, y, length, height)    = create_grid(WIDTH, 3*HEIGHT//4, n_col, n_row, 20, 20, 0, 0)
    max_stats   = loadtxt("./src/stat.txt", skiprows=1, max_rows=1)
    stats       = loadtxt("./src/stat.txt", skiprows=2)
    print(stats)
    n_players   = len(stats)
    n_stats     = len(max_stats)
    l_bars      = np.zeros((n_players, n_stats), np.int32)


    for i in range(n_players):
        for j in range(n_stats):
            l_bars[i,j] = stats[i,j] / max_stats[j] * WIDTH//3
        # l_bars.append([stats[i][j]/max_stats[j]*(WIDTH//6) for j in range(n_stats)])


    x_bars, y_bars, lll, h_bars = create_grid(WIDTH, HEIGHT//3, 2, n_stats, 20, 20)
    h_bars  = np.int(h_bars)
    y_bars += 3*HEIGHT//4
    print(type(l_bars[0,0]), type(h_bars))
    # if p==1:
    #     redd    = pygame.Surface((length, height))
    #     redd.fill((255,0,0))
    #     redd.set_alpha(155)
    #     screen.blit(redd, (x[nq], y[nq]))
    player = np.zeros(2)
    while True:
        screen.fill(WHITE)
        drawgrid(x, y, length, height, screen, chars)
        (x_mouse,y_mouse) = pygame.mouse.get_pos()
        # correcting mouse position reading
        if y_mouse >= HEIGHT*2//3:
            y_mouse = HEIGHT*2//3
        elif y_mouse < 0:
            y_mouse = 0
        # if x_mouse >= WIDTH//3*2:
        #     x_mouse = WIDTH//3*2-1
        # elif x_mouse < WIDTH//3:
        #     x_mouse = WIDTH//3
        # if y_mouse >= HEIGHT:
        #     y_mouse = HEIGHT-1
        # elif y_mouse < 0:
        #     y_mouse = 0

        # x_mouse-= WIDTH//3

        # get different integer for different characters from mouse x and y
        dx      = WIDTH / n_col
        x_mouse = x_mouse // dx
        dx      = HEIGHT / n_col
        x_mouse = x_mouse // dx
        # x_mouse = x_mouse//length
        # y_mouse = y_mouse//height
        # n_c     = int(x_mouse%4 + y_mouse//4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    if p == 0:
                        player[0] = n_c
                    else:
                        if n_c != player[0]:
                            player[1] = n_c
                            return player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if p==0:
                        start(WIDTH, HEIGHT)
                        screen.fill((0,0,0))
                    elif p==1:
                        screen.fill((0,0,0))
                        select_player(WIDTH, HEIGHT, 0, 0)
        if p==0:
            # screen.blit(big_char_im[n_c], (0,0))
            for i in range(n_stats):
                image    = pygame.Surface((l_bars[n_c][i], h_bars))
                image.fill(GREEN)
                screen.blit(image, (x_bars[i], y_bars[i]))
        elif p==1:
            shiftx  = 2*WIDTH//3
            # screen.blit(big_char_im[nq], (0,0))
            # screen.blit(big_char_im[n_c], (WIDTH//3*2,0))
            for i in range(n_stats):
                image    = pygame.Surface((l_bars[nq][i], h_bars))
                image.fill(GREEN)
                screen.blit(image, (x_bars[i], y_bars[i]))
                image    = pygame.Surface((l_bars[n_c][i], h_bars))
                image.fill(GREEN)
                screen.blit(image, (shiftx+x_bars[i], y_bars[i]))
        pygame.display.update()
        if not running :
            quit()


def sel_map(WIDTH, HEIGHT, step):
    import pygame
    n_of_maps   = 8
    (x, y, lx, ly)  = create_grid(WIDTH, HEIGHT, n_of_maps//2, 2, 40, 40)
    screen  = pygame.display.set_mode((WIDTH, HEIGHT))
    rect_sur= pygame.Surface((lx, ly))
    rect_sur.fill((0,0,0))
    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for i in range(n_of_maps):
            screen.blit(rect_sur, (x[i], y[i]))
        pygame.display.update()
