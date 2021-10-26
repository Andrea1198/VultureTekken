import pygame
# from src.colors import col
from src.characters import char
from src.startingWindows import start, select_player, sel_map
from src.fight import fight
success, failures   = pygame.init()
print('Initializing pygame: {0} successes and {1} failures.'.format(success, failures))

WIDTH   = 720
HEIGHT  = 480
screen  = pygame.display.set_mode((WIDTH, HEIGHT))
clock   = pygame.time.Clock()
FPS     = 60
pygame.display.set_caption('Vulture Tekken')
gravity = []
# c       = col()
running = True
step    = 0
# schermata iniziale
start(WIDTH, HEIGHT)
# select_player dà in uscita un numero intero che indica quale personaggio ha preso
n1, n2  = select_player(WIDTH, HEIGHT)
# char è la classe dei personaggi che in entrata chiede un numero per identificare quale personaggio prendere
p1      = char(n1, WIDTH, 0)
p2      = char(n2, WIDTH, 1)
# quindi p1 e p2 sono i due personaggi che si scontrano, ognuno con caratteristiche diverse
map     = sel_map(WIDTH, HEIGHT)
gravity = gravity[map]

while running:
    dt  = float(clock.tick(FPS)) / 1000.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
