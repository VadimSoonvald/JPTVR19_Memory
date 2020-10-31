import pygame #importing
import random #importing random
import time #importing time
pygame.init()

black = (0, 0, 0) #black color
white = (255, 255, 255) #white color
purple = (255, 0, 255) #purple color

wight = 800
height = 800
screen = pygame.display.set_mode((wight, height))
pygame.display.set_caption("Memory - Find a couple of the picture")
screen.fill(white)

#upload images 
p1 = pygame.image.load("p1.png")
p1 = pygame.transform.scale(p1, (200, 200))
p2 = pygame.image.load("p2.png")
p2 = pygame.transform.scale(p2, (200, 200))
p3 = pygame.image.load("p3.png")
p3 = pygame.transform.scale(p3, (200, 200))
p4 = pygame.image.load("p4.png")
p4 = pygame.transform.scale(p4, (200, 200))
p5 = pygame.image.load("p5.png")
p5 = pygame.transform.scale(p5, (200, 200))
p6 = pygame.image.load("p6.png")
p6 = pygame.transform.scale(p6, (200, 200))
p7 = pygame.image.load("p7.png")
p7 = pygame.transform.scale(p7, (200, 200))
p8 = pygame.image.load("p8.png")
p8 = pygame.transform.scale(p8, (200, 200))

rect = [False] * 16
#create mas
picture = [p1, p2, p3, p4, p5, p6, p7, p8,\
          p1, p2, p3, p4, p5, p6, p7, p8]
#shuffling images
random.shuffle(picture)

count = 0
first, second = None, None
f_index, s_index = None, None

#draw lines (game field)
def boardDraw(screen):
    pygame.draw.line(screen,purple,(0,0),(800,0), 5)
    pygame.draw.line(screen,purple,(800,0),(800,800), 5)
    pygame.draw.line(screen,purple,(0,0),(0,800), 5)

    pygame.draw.line(screen,purple,(0,200),(800,200), 5)
    pygame.draw.line(screen,purple,(0,400),(800,400), 5)
    pygame.draw.line(screen,purple,(0,600),(800,600), 5)
    pygame.draw.line(screen,purple,(0,800),(800,800), 5)

    pygame.draw.line(screen,purple,(200,0),(200,800), 5)
    pygame.draw.line(screen,purple,(400,0),(400,800), 5)
    pygame.draw.line(screen,purple,(600,0),(600,800), 5)

boardDraw(screen)
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
            screen.fill((255, 255, 255))
            rect = [False] * 16
            boardDraw(screen)
            count = 0

        if i.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if count == 8:
                screen.fill((255, 0, 255))
                font = pygame.font.Font(None, 60)
                text = font.render('WELL DONE! YOU WON!', True, (0, 255, 255))
                text_rect = text.get_rect()
                screen.blit(text, [140, 300])
                break
            if (x > 0 and y > 0 and x < 200 and y < 200):
                kv = 0 
                px = 0
                py = 00
                
            if (x > 200 and y > 0 and x < 400 and y < 400):
                kv = 1
                px = 200
                py = 0
         
            if (x > 400 and y > 0 and x < 600 and y < 600):
                kv = 2
                px = 400
                py = 0
             
            if (x > 600 and y > 0 and x < 800 and y < 800):
                kv = 3
                px = 600
                py = 0
            
            if (x > 0 and y > 200 and x < 800 and y < 800):
                kv = 4
                px = 0
                py = 200
            
            if (x > 200 and y > 200 and x < 800 and y < 800):
                kv = 5
                px = 200
                py = 200
           
            if (x > 400 and y > 200 and x < 800 and y < 800):
                kv = 6
                px = 400
                py = 200
           
            if (x > 600 and y > 200 and x < 800 and y < 800):
                kv = 7
                px = 600
                py = 200

            if (x > 0 and y > 400 and x < 800 and y < 800):
                kv = 8
                px = 0
                py = 400
            
            if (x > 200 and y > 400 and x < 800 and y < 800):
                kv = 9
                px = 200
                py = 400
            
            if (x > 400 and y > 400 and x < 800 and y < 800):
                kv = 10
                px = 400
                py = 400
           
            if (x > 600 and y > 400 and x < 800 and y < 800):
                kv = 11
                px = 600
                py = 400

            if (x > 0 and y > 600 and x < 800 and y < 800):
                kv = 12
                px = 0
                py = 600
            
            if (x > 200 and y > 600 and x < 800 and y < 800):
                kv = 13
                px = 200
                py = 600
            
            if (x > 400 and y > 600 and x < 800 and y < 800):
                kv = 14
                px = 400
                py = 600
           
            if (x > 600 and y > 600 and x < 800 and y < 800):
                kv = 15
                px = 600
                py = 600
            
            if rect[kv] == False:
                if first == None:
                    f_index = kv
                    f_xp, f_yp = px, py 
                    first = picture[kv]
                    screen.blit(first, (px, py))
                    pygame.display.flip()
                    
                elif first != None and second == None:
                    s_index = kv
                    s_xp, s_yp = px, py
                    second = picture[kv]
                    screen.blit(second, (px, py))
                    pygame.display.flip()
                    
                    if first == second:
                        rect[f_index] = True
                        rect[s_index] = True
                        first, second = None, None
                        count += 1

                    else:
                        time.sleep(0.1)
                        pygame.draw.rect(screen,white,(f_xp + 3, f_yp + 3, 196, 196))
                        time.sleep(0.1)
                        pygame.draw.rect(screen,white,(s_xp + 3, s_yp + 3, 196, 196))
                        first, second = None, None

    pygame.display.update()
pygame.quit()