import pygame, sys, random
from pygame.locals import *

pygame.init()

# FPS
FPS = 60
fpsClock = pygame.time.Clock()

# DISPLAY
X_DISPLAYSURF = 700
Y_DISPLAYSURF = 700
DISPLAYSURF = pygame.display.set_mode((X_DISPLAYSURF, Y_DISPLAYSURF))
pygame.display.set_caption('BoatRun Alpha1.0')

# BACKGROUNDS
MENUBACKGROUND = pygame.image.load('menu-background.png')
GAMEBACKGROUND = pygame.image.load('game-background.png')

# FONT
FONT = pygame.font.SysFont("Arial Black", 30)

# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# POSITIONS
COLUMN1 = 100
COLUMN2 = 200
COLUMN3 = 300
COLUMN4 = 400
COLUMN5 = 500
ALLCOLUMNS = (COLUMN1, COLUMN2, COLUMN3, COLUMN4, COLUMN5)

# POINTS
pointsN = 0
recordN = 0

# PLAYER
BOAT = pygame.image.load('boat.png') # 80px * 100px
xPlayer = 310
yPlayer = 500
speedPlayer = 16

# OBSTACLES
# 1ST CORAL
CORAL1 = pygame.image.load('coral1.png') # 100px * 100px
xCoral1 = random.choice(ALLCOLUMNS)
yCoral1 = -200
speedCoral = 15
# 2ND CORAL
CORAL2 = pygame.image.load('coral2.png') # 100px * 100px
xCoral2 = random.choice(ALLCOLUMNS)
yCoral2 = -200
speedCoral = 15
# OCTOPUS
OCTOPUS = pygame.image.load('octopus.png') # 100px * 100px
xOctopus = random.choice(ALLCOLUMNS)
yOctopus = -200
speedOctopus = 20

# LOOPS
menu = True
game = True

while True:
    while menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        start_game = pygame.key.get_pressed()
        if start_game[pygame.K_SPACE]:
            menu = False

        recordT = FONT.render(f" Record: {recordN}", True, (0, 0, 0), (255, 255, 255))
        pointsN = 0

        xPlayer = 310
        yCoral1 = -200
        yCoral2 = -200
        yOctopus = -200

        DISPLAYSURF.blit(MENUBACKGROUND, (0, 0))
        DISPLAYSURF.blit(recordT, (5, 5))
        pygame.display.update()
        fpsClock.tick(FPS)

    while game:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # MOVEMENT
        controls = pygame.key.get_pressed()
        if controls[pygame.K_LEFT]:
            xPlayer -= speedPlayer
        if controls[pygame.K_RIGHT]:
            xPlayer += speedPlayer

        # POINTS / RECORD
        pointsN += 1
        if pointsN > recordN:
            recordN = pointsN
        pointsT = FONT.render(f" Points: {pointsN}", True, (0, 0, 0), (255, 255, 255))

        # BARRIERS
        if xPlayer < 100:
            xPlayer = 100
        if xPlayer > 520:
            xPlayer = 520

        # SPEED
        yCoral1 += speedCoral
        yCoral2 += speedCoral
        yOctopus += speedOctopus

        # RESTART LOCATION
        if yCoral1 > 700:
            yCoral1 = -200
            xCoral1 = random.choice(ALLCOLUMNS)
        if yCoral2 > 700:
            yCoral2 = -200
            xCoral2 = random.choice(ALLCOLUMNS)
        if yOctopus > 700:
            yOctopus = -200
            xOctopus = random.choice(ALLCOLUMNS)

        # DIFFICULTY
        if pointsN == 1000:
            speedCoral += 3
            speedOctopus += 3
        if pointsN == 1500:
            speedCoral += 2
            speedOctopus += 2
        if pointsN == 2000:
            speedCoral += 5
            speedOctopus += 5

        # COLISIONS
        if yCoral1 + 90 > yPlayer:
            if yCoral1 < 600:
                if xCoral1 + 90 > xPlayer and xPlayer + 70 > xCoral1:
                    menu = True
                    break
        if yCoral2 + 90 > yPlayer:
            if yCoral2 < 600:
                if xCoral2 + 90 > xPlayer and xPlayer + 70 > xCoral2:
                    menu = True
                    break
        if yOctopus + 90 > yPlayer:
            if yOctopus < 600:
                if xOctopus + 90 > xPlayer and xPlayer + 70 > xOctopus:
                    menu = True
                    break


        DISPLAYSURF.blit(GAMEBACKGROUND, (0, 0))
        DISPLAYSURF.blit(BOAT, (xPlayer, yPlayer))
        DISPLAYSURF.blit(CORAL1, (xCoral1, yCoral1))
        DISPLAYSURF.blit(CORAL2, (xCoral2, yCoral2))
        DISPLAYSURF.blit(OCTOPUS, (xOctopus, yOctopus))
        DISPLAYSURF.blit(pointsT, (5, 5))
        pygame.display.update()
        fpsClock.tick(FPS)


