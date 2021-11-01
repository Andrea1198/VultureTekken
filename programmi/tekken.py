import pygame
from src.colors import *
from src.characters import char
from src.start.startWind import start
from src.start.select_player import select_player
from src.start.select_map import select_map, selectGravity
from src.Fight.fight import fight
success, failures   = pygame.init()
print('Initializing pygame: {0} successes and {1} failures.'.format(success, failures))

WIDTH   = 1080
HEIGHT  = 720
# screen  = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
screen  = pygame.display.set_mode((WIDTH, HEIGHT))
clock   = pygame.time.Clock()
FPS     = 60
pygame.display.set_caption('Vulture Tekken')
# c       = col()
running = True
step    = 0
# schermata iniziale
# start(WIDTH, HEIGHT)
# select_player dà in uscita un numero intero che indica quale personaggio ha preso
# [n1, n2]  = select_player(WIDTH, HEIGHT, 0, 0)
# Debugging variables
n1          = 0
n2          = 1
# char è la classe dei personaggi che in entrata chiede un numero per identificare quale personaggio prendere
p1          = char(n1, WIDTH, 0)
p2          = char(n2, WIDTH, 1)
# quindi p1 e p2 sono i due personaggi che si scontrano, ognuno con caratteristiche diverse
map, scene  = select_map(WIDTH, HEIGHT)
print("The selected map is ", map)
# gravity = selectGravity(map)

# Fight!
while running:
    dt  = float(clock.tick(FPS)) / 1000.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    fight(WIDTH, HEIGHT, p1, p2, scene)
