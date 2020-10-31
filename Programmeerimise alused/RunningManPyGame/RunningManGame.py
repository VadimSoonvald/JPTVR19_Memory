import pygame
import random
pygame.init()

display_width = 1920
display_height = 1080
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Running Man")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

wall_img = [pygame.image.load("wall.png"), pygame.image.load("wall1.png"), pygame.image.load("wall2.png")]
wall_options = [42, 824, 42, 824, 42, 824]

class Cactus:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        #self.height = height
        self.image = image
        self.speed = speed
        
    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            #pygame.draw.rect(display, (114, 221, 231), (self.x, self.y, self.width, self.height))
            self.x -= self.speed
            return True
        else:
            #self.x = display_width + 100 + random.randrange(-80, 60)
            return False
    
    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self_image = image
        display.blit(self.image, (self.x, self.y))

man_width = 130
man_height = 170
man_x = display_width // 6 
man_y = display_height - man_height - 200

cactus_width = 40
cactus_height = 100
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 200

clock = pygame.time.Clock()

make_jump = False
jump_counter = 30

def run_game():
    global make_jump
    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)
    background = pygame.image.load('background.png')
    
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True
        
        if make_jump:
            jump()
                
        display.blit(background, (0,0))
        #display.fill((255,255,255))
        draw_array(cactus_arr)
        #draw_cactus()
        
        pygame.draw.rect(display, (147, 140, 222), (man_x, man_y, man_width, man_height))
        
        pygame.display.update()
        clock.tick(60)

def jump():
    global man_y, jump_counter, make_jump
    if jump_counter >= -30:
        man_y -= jump_counter
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False
        
#def draw_cactus():
    #global cactus_x, cactus_y, cactus_width, cactus_height
    
    #if cactus_x >= -cactus_width:
        #pygame.draw.rect(display, (224, 121, 31), (cactus_x, cactus_y, cactus_width, cactus_height))
        #cactus_x -= 5
    #else:
        #cactus_x = display_width - 50
        
def create_cactus_arr(array):
    choice = random.randrange(0, 3)
    img = wall_img[choice]
    width = wall_options[choice * 2]
    height = wall_options[choice * 2 + 1]
    array.append(Cactus(display_width - 400, height, width, img, 4))
    
    choice = random.randrange(0, 3)
    img = wall_img[choice]
    width = wall_options[choice * 2]
    height = wall_options[choice * 2 + 1]
    array.append(Cactus(display_width + 300, height, width, img, 4))
    
    choice = random.randrange(0, 3)
    img = wall_img[choice]
    width = wall_options[choice * 2]
    height = wall_options[choice * 2 + 1]
    array.append(Cactus(display_width + 600, height, width, img, 4))

def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)
    
    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum
    
    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)
    return radius

def draw_array(array):
    for cactus in array:
        cactus.move()
        check = cactus.move()
        if not check:
            radius = find_radius(array)
            choice = random.randrange(0, 3)
            img = wall_img[choice]
            width = wall_options[choice * 2]
            height = wall_options[choice * 2 + 1]
            
            cactus.return_self(radius, height, width, img)

run_game()