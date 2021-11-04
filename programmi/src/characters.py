from numpy import loadtxt
import pygame
# Character's class. Everyone has different statistics.
# melee : short range damage
# range : throwing damage (usually less than melee)
# health : max health
# velocity : how many pixel/frame (60 fps, v = 1 => 60 pixel/s)
# jump : max height of the jump
# regeneration : Hp regenerated per second (ogni 60 frame)

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

        self.melee, self.range, self.maxHealth, self.velocity, self.jump,  self.regeneration = loadtxt('./src/stat.txt', skiprows=n+2, max_rows=1, unpack=True)
        self.health       = self.maxHealth
        self.superMax   = 100
        self.super      = 0
        self.move       = False
        self.d          = -1
        if p==0:
            self.x      = 10
        else:
            self.x      = WIDTH-10-w_image
        self.y      = 0.
        self.vy     = 0.

    # damages
    def hit_melee(self, p2):
        self.health  -= p2.melee
    def hit_dist(self, p2):
        self.health  -= p2.range

    # movements
    def Move(self, d):                          # d=0,1 : 0=sx, 1=dx
        if d==0 and self.move:
            self.x -= self.velocity*2.
        elif d==1 and self.move:
            self.x += self.velocity*2.
    def Jump(self):
        if self.y==0:
            self.vy = self.jump/2.
    def Update(self, gravity):
        if self.y >= 0:
            self.vy-= gravity
            self.y += self.vy
            if self.y < 0:
                self.y = 0.
        if self.move:
            self.Move(self.d)
    def Show(self, screen, HEIGHT, base):
        import pygame
        screen.blit(self.image, (self.x, HEIGHT - self.h_image - self.y - base))
