import pygame

fps = 60
w = 700
h = 300
white = (255, 255, 255)
blue = (0, 70, 225)

pygame.init()
sc = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

x = w // 2
y = h // 2
r = 30

done = True
while done:
    sc.fill(white)
    pygame.draw.circle(sc, blue, (x , y), r)
    pygame.display.update()
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 3
            elif i.key == pygame.K_RIGHT:
                x += 3
    clock.tick(fps)

pygame.quit()