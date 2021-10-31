import pygame
from src.start.functions import checkBT
# from src.colors import *

# Starting window
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
    bt1x= WIDTH//4
    bt1y= HEIGHT//2
    hbt1= HEIGHT//4
    lbt1= WIDTH//2
    bt2x= bt1x
    bt2y= bt1y+hbt1
    hbt2=hbt1
    lbt2=lbt1
    btn1    = pygame.image.load(dir+start[i])
    btn1    = pygame.transform.scale(btn1, (lbt1, hbt1))
    btn2    = pygame.image.load(dir+exit[i])
    btn2    = pygame.transform.scale(btn2, (lbt2, hbt2))
    screen.blit(bkg, (0,0))
    screen.blit(btn1,(bt1x,bt1y))
    screen.blit(btn2,(bt2x,bt2y))
    pygame.display.update()
    while running:
        (x_mouse, y_mouse)  = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if checkBT(y_mouse, bt1y, bt1y+hbt1) and checkBT(x_mouse, bt1x, bt1x+lbt1):
                i = 0
            elif checkBT(y_mouse, bt2y, bt2y+hbt2) and checkBT(x_mouse, bt2x, bt2x+lbt2):
                i = 1
            else:
                i = -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if i==0:
                    running = False
                elif i==1:
                    pygame.quit()
