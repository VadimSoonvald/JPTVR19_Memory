import pygame
FPS = 60
W = 700 # ширина экрана
H = 700 # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RIGHT = "to the right"
LEFT = "to the left"
UP = "to the up"
DOWN = "to the down"
STOP = "stop"
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
# координаты и радиус круга
x = W // 2
y = H // 2
r = 50
motion = STOP
done = True

while done:
    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
            elif i.key == pygame.K_UP:
                motion = UP
            elif i.key == pygame.K_DOWN:
                motion = DOWN
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                 motion = STOP
            if i.key in [pygame.K_UP, pygame.K_DOWN]:
                 motion = STOP
                 
    if motion == LEFT:
        x -= 3
    elif motion == STOP:
        if x < W // 2:
            x += 3
    if motion == RIGHT:
        x += 3
    elif motion == STOP:
        if x > W // 2:
            x -= 3
    if motion == UP:
        y -= 3
    elif motion == STOP:
        if y < H // 2:
            y += 3
    if motion == DOWN:
        y += 3
    elif motion == STOP:
        if y > H // 2:
            y -= 3
            
    clock.tick(FPS)

pygame.quit()
