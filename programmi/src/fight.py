def fist(p):
    print('fist')
def kick(p):
    print('kick')
def jump(p):
    print('jump')

def fight(WIDTH, HEIGHT):
    screen  = pygame.display.set_mode((WIDTH, HEIGHT))
    # health bar
    x1  = 10
    y1  = 10
    l   = WIDTH//2-30
    h   = 20
    x2  = WIDTH//2+20
    health1 = pygame.Surface((l, h))
    health1.fill((255,0,0))
    screen.blit(health1, (x1, y1))
    screen.blit(health1, (x2, y1))
    pygame.display.update()
