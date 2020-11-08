import pygame
from pygame import mixer
import sys
import random

mixer.init()
pygame.init()

#Backgrounds
screen = pygame.display.set_mode((1200, 700))
park = pygame.image.load('Park.png')
Img_scale = pygame.transform.scale(park, (1200, 700))
Menu_screen = pygame.image.load('Logo2.png')

# Player
RobotIMG = pygame.image.load('Robot.png')
RobotX = 600
RobotY = 350
RXchange = 0
RYchange = 0
# Couds
cloudz = []
Cloudx = []
Cloudy = []
Cloudx_change = 10
number_of_clouds = 2
for i in range(number_of_clouds):
    cloudz.append(pygame.image.load('Clouds.png'))
    Cloudx.append(-40)
    Cloudy.append(random.randint(0, 600))

# cloudz = pygame.image.load('Clouds.png')
# Cloudx = -40
# Cloudy = random.randint(0, 680)
# Cloudx_change = 10
def Quote(x, y):
    screen.blit(RobotIMG, (x, y))

def clouds(x, y, i):
    screen.blit(cloudz[i], (x, y))


no1_calm = pygame.mixer.Sound('Calm.ogg')
no1_calm.play()


Menu = True
running = True
Park = False
while running:
    while Menu:
        # Sound1.play()
        screen.fill((0, 128, 255))
        screen.blit(Menu_screen,(400, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Menu = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    Menu = False
                    Park = True
        for i in range(number_of_clouds):
            clouds(Cloudx[i], Cloudy[i], i)
            Cloudx[i] += Cloudx_change
            if Cloudx[i] >= 1250:
                cloudz[i] = pygame.image.load('Clouds.png')
                Cloudy[i] = (random.randint(0, 600))
                Cloudx[i] = -100
        pygame.display.flip()


    while Park:
        screen.blit(park, (0, 0))
        screen.blit(Img_scale, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        Quote(RobotX, RobotY)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    RXchange = -10
                if event.key == pygame.K_RIGHT:
                    RXchange = 10
                if event.key == pygame.K_UP:
                    RYchange = -10
                if event.key == pygame.K_DOWN:
                    RYchange = 10
#This is a test