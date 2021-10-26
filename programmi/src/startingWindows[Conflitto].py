def create_grid(w, h, n_col=1, n_row=1, spacex=0, spacey=0, shiftx=0, shifty=0):
    x=[]
    y=[]
    lx  = w/n_col-spacex
    ly  = h/n_row-spacey
    print(lx, ly)
    for i in range(n_col*n_row):
        xx  = shiftx + i%n_col*(w/n_col) + spacex/2
        yy  = shifty + i//n_col*(h/n_row) + spacey/2
        x.append(xx)
        y.append(yy)
        print(xx, yy)
        return (x, y, lx, ly)

# Schermata iniziale

def start(WIDTH, HEIGHT, step):
    import pygame
    running = True
    dir = "./images/start/"
    background  = "background.jpg"
    start       = ["start_selected.png", "start_not_selected.png"]
    exit        = ["quit_not_selected.png", "quit_selected.png"]

    i   = 0
    screen  = pygame.display.set_mode((WIDTH, HEIGHT))
    bkg = pygame.image.load(dir+background)
    bkg = pygame.transform.scale(bkg, (WIDTH, HEIGHT))
    while running:
        (x_mouse, y_mouse)  = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if pygame.key == pygame.K_BACKSPACE:
                    step   -= 1
                    return
            if y_mouse < HEIGHT*3//4 and y_mouse > HEIGHT // 2:
                i==0
            else:
                i==1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if i==0:
                    running = False
                else:
                    pygame.quit()
        btn1    = pygame.image.load(dir+start[i])
        btn1    = pygame.transform.scale(btn1, (WIDTH//2, HEIGHT//4))
        btn2    = pygame.image.load(dir+exit[i])
        btn2    = pygame.transform.scale(btn2, (WIDTH//2, HEIGHT//4))
        screen.blit(bkg,(0,0))
        screen.blit(btn1,(WIDTH//4,HEIGHT//2))
        screen.blit(btn2,(WIDTH//4,HEIGHT//4*3))
        pygame.display.update()

# La funzione deve mostrare le icone con i vari personaggi per selezionarne uno e dare in uscita un intero

def select_player(WIDTH, HEIGHT, p, nq, step):
    import pygame
    from numpy import loadtxt

    chars       = ["Pi.jpeg", "Dan.jpeg", "Albi.jpeg", "Mt_Conta.jpeg", "Cinto.jpeg", "JD.jpeg", "Niscoreggia.jpeg", "Steve.jpeg"]
    running     = True
    n           = len(chars)
    n_col       = 2
    n_row       = (n+1)//n_col
    # Altezza e lunghezza dei rettangoli che contengono le immagini dei personaggi
    length      = (WIDTH//3)//n_col
    height      = HEIGHT//n_row
    x           = [length*(i//n_row) + WIDTH//3 for i in range(n)]
    y           = [height*(i%n_row) for i in range(n)]
    max_stats   = loadtxt("./src/stat.txt", skiprows=1, max_rows=1)
    stats       = loadtxt("./src/stat.txt", skiprows=2)
    l_bars      = []
    n_players   = len(stats)
    n_stats     = len(max_stats)

    for i in range(n_players):
        l_bars.append([stats[i][j]/max_stats[j]*(WIDTH//6) for j in range(n_stats)])

    # for i in range(n_players):
    #     for j in range(n_stats):
    #         l_bars[i][j]  = l_bars[i][j]*(WIDTH//6)

    x_bars      = [WIDTH//6 for i in range(n_stats)]
    h_stat_rect = HEIGHT//3
    h_bars      = (h_stat_rect/n_stats*2)//3
    y_bars      = [HEIGHT//3*2 + h_bars//4 + i*h_stat_rect//6 for i in range(n_stats)]
    GREEN       = (0,   255,    0)
    BLACK       = (0,     0,    0)
    dir         = "./images/characters/"
    char_im     = [pygame.image.load(dir+chars[i]) for i in range(n)]
    big_char_im = [pygame.transform.scale(char_im[i], (WIDTH//3, HEIGHT*2//3)) for i in range(n)]
    char_im     = [pygame.transform.scale(char_im[i], (length,height)) for i in range(n)]
    screen      = pygame.display.set_mode((WIDTH, HEIGHT))
    half_left   = pygame.Surface((WIDTH//3, HEIGHT))
    half_left.fill(BLACK)

    for i in range(n):
        screen.blit(char_im[i], (x[i], y[i]))
    if p==1:
        redd    = pygame.Surface((length, height))
        redd.fill((255,0,0))
        redd.set_alpha(155)
        screen.blit(redd, (x[nq], y[nq]))

    while True:
        (x_mouse,y_mouse) = pygame.mouse.get_pos()
        # correcting mouse position reading
        if x_mouse >= WIDTH//3*2:
            x_mouse = WIDTH//3*2-1
        elif x_mouse < WIDTH//3:
            x_mouse = WIDTH//3
        if y_mouse >= HEIGHT:
            y_mouse = HEIGHT-1
        elif y_mouse < 0:
            y_mouse = 0
        x_mouse-= WIDTH//3
        # get different integer for different characters from mouse x and y
        x_mouse = x_mouse//length
        y_mouse = y_mouse//height
        n_c     = x_mouse*n//2+y_mouse
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.key == pygame.K_BACKSPACE:
                    step   -= 1
                    return
            if event.type == pygame.QUIT:
                running = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    if n_c != nq:
                        return n_c
        if p==0:
            screen.blit(half_left, (0,0))
            screen.blit(big_char_im[n_c], (0,0))
            for i in range(n_stats):
                image    = pygame.Surface((l_bars[n_c][i], h_bars))
                image.fill(GREEN)
                screen.blit(image, (x_bars[i], y_bars[i]))
        elif p==1:
            shiftx  = 2*WIDTH//3
            screen.blit(half_left, (shiftx, 0))
            screen.blit(big_char_im[nq], (0,0))
            screen.blit(big_char_im[n_c], (WIDTH//3*2,0))
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
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.key == pygame.K_BACKSPACE:
                    step   -= 1
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
        for i in range(n_of_maps):
            screen.blit(rect_sur, (x[i], y[i]))
        pygame.display.update()
