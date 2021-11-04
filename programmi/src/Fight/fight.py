import numpy as np
import pygame
from src.colors import *

def fist(p):
    print('fist')

def kick(p):
    print('kick')

def showScenario(WIDTH, HEIGHT, image):
    screen  = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BLACK)
    screen.blit(image, (0, 0))
    return screen


def showHS(WIDTH, HEIGHT, screen, p1, p2):

    xbar1p1 = 10
    ybar1p1 = 10
    lbarMax = WIDTH//2-30
    hbar    = 20
    xbar1p2 = WIDTH//2+20
    ybar1p2 = ybar1p1
    xbar2p1 = xbar1p1
    ybar2p1 = ybar1p1+hbar
    xbar2p2 = xbar1p2
    ybar2p2 = ybar2p1

    lbar1p1 = lbarMax
    lbar2p1 = 10
    lbar1p2 = lbarMax
    lbar2p2 = 10

    health1 = pygame.Surface((lbar1p1, hbar))
    health1.fill(RED)
    super1  = pygame.Surface((lbar2p2, hbar))
    super1.fill(YELLOW)
    health2 = pygame.Surface((lbar1p2, hbar))
    health2.fill(RED)
    super2  = pygame.Surface((lbar2p2, hbar))
    super2.fill(YELLOW)

    screen.blit(health1, (xbar1p1, ybar1p1))
    screen.blit(health2, (xbar1p2, ybar1p2))
    screen.blit(super1, (xbar2p1, ybar2p1))
    screen.blit(super2, (xbar2p2, ybar2p2))

def controls(p, pe):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_w and p.y == 0:
                p.Jump()
                print("jump")
            elif key == pygame.K_a:
                p.move = True
                p.d    = 0
                print("left")
            elif key == pygame.K_d:
                p.move = True
                p.d     = 1
            elif key == pygame.K_e:
                fist(p)
                if pe.x - p.x < 10:
                    pe.hit_melee
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                p.move = False


def fight(WIDTH, HEIGHT, p1, p2, scene, gravity):
    base    = 30
    # health and super bar
    screen  = showScenario(WIDTH, HEIGHT, scene)
    showHS(WIDTH, HEIGHT, screen, p1, p2)
    p1.Update(gravity)
    p1.Show(screen, HEIGHT, base)
    p2.Show(screen, HEIGHT, base)
    # Controls (only for p1)
    controls(p1, p2)
    pygame.display.update()
