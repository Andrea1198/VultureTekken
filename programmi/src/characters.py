from numpy import loadtxt
import pygame
# Classe dei personaggi. ognuno di essi ha diverse caratteristiche.
# corpo_a_corpo : danni da vicino
# distanza : danni per cose lanciate (minori del corpo a corpo)
# vita : vita totale
# velocity : quanti pixel/frame (60 fps, v = 1 => 60 pixel al secondo)
# salto : altezza max del salto
# rigenerazione : punti vita rigenerati al secondo (ogni 60 frame)

class char:
    def __init__(self, n, WIDTH, p):
        self.n          = n
        dir             = './images/characters/'
        chars           = ["Pi.jpeg", "Dan.jpeg", "Albi.jpeg", "Mt_Conta.jpeg", "Cinto.jpeg", "JD.jpeg", "Niscoreggia.jpeg", "Steve.jpeg"]
        char_im         = [pygame.image.load(dir+chars[i]) for i in range(len(chars))]
        image           = char_im[self.n]
        w_image         = 100
        self.h_image    = 100
        self.image      = pygame.transform.scale(image, (w_image, self.h_image))

        self.corpo_a_corpo, self.distanza, self.vitaMax, self.velocity, self.salto,  self.rigenerazione = loadtxt('./src/stat.txt', skiprows=n+2, max_rows=1, unpack=True)
        self.vita       = self.vitaMax
        self.superMax   = 100
        self.super      = 0
        if p==0:
            self.x      = 10
        else:
            self.x      = WIDTH-10-w_image
        self.y      = 0.
        self.vy     = 0.

    # damages
    def hit_melee(self, p2):
        self.vita  -= p2.corpo_a_corpo
    def hit_dist(self, p2):
        self.vita  -= p2.distanza

    # movements
    def move(self, d):                          # d=0,1 : 0=sx, 1=dx
        if d==0:
            self.x -= self.velocity
        else:
            self.x += self.velocity
    def jump(self):
        if self.y==0:
            self.vy = self.salto
    def update(self, gravity):
        if self.y >= 0:
            self.vy-= gravity
            self.y -= self.vy
            if self.y < 0:
                self.y = 0.
    def show(self, screen, HEIGHT, base):
        import pygame
        screen.blit(self.image, (self.x, HEIGHT - self.h_image - self.y - base))
