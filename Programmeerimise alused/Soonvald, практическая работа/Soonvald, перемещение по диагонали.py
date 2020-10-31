import pygame
FPS = 60
W = 700 # ширина экрана
H = 700 # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RIGHT = "to the right"
LEFT = "to the left"
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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    elif keys[pygame.K_RIGHT]:
        x += 1
    elif keys[pygame.K_UP]:
        y -= 1
    elif keys[pygame.K_DOWN]:
        y += 1
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        x -= 1
        y -= 1
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        x += 1
        y += 1
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        x += 1
        y -= 1
    if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        x -= 1
        y += 1
        
clock.tick(FPS)

pygame.quit()