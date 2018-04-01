__author__ = '10014422'

import pygame
import random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
orange = (255, 69, 0)
purple = (148, 0, 211)
y = 0
add = False
font = pygame.font.SysFont("comicsansms", 50)
speed = 0
level = 0
pause = False

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dodge it")
pygame.display.update()
person = pygame.Rect(400, 540, 50, 50)
fallingblock = pygame.Rect(400, y, 15, 15)
power_up1 = pygame.Rect(random.randrange(50, 750), 540, 30, 30)
power_up2 = pygame.Rect(random.randrange(50, 750), 540, 30, 30)
img = pygame.image.load("stickman.png")
img = pygame.transform.scale(img, (50, 50))
img1 = pygame.image.load("Fireball.jpg")
img1 = pygame.transform.scale(img1, (30, 30))

clock = pygame.time.Clock()
rectlist = list()
rectlist.append(fallingblock)
poweruplist = list()
poweruplist.append(power_up1)
poweruplist.append(power_up2)


menuExit = False
while not menuExit:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    name = font.render("Dodge it", True, white)
    gameDisplay.blit(name, (300, 10))

    easybutton = pygame.Rect(200, 150, 400, 80)
    pygame.draw.rect(gameDisplay, blue, easybutton)
    gameDisplay.blit(font.render("Easy", True, white), (350, 150))
    click = pygame.mouse.get_pressed()
    if 600 > pos[0] > 200 and 230 > pos[1] > 150 and click[0] == 1:
        menuExit = True
        level = 1

    mediumbutton = pygame.Rect(200, 300, 400, 80)
    pygame.draw.rect(gameDisplay, green, mediumbutton)
    gameDisplay.blit(font.render("Medium", True, white), (310, 300))
    if 600 > pos[0] > 200 and 380 > pos[1] > 300 and click[0] == 1:
        menuExit = True
        level = 2

    hardbutton = pygame.Rect(200, 450, 400, 80)
    pygame.draw.rect(gameDisplay, red, hardbutton)
    gameDisplay.blit(font.render("Hard", True, white), (340, 450))
    if 600 > pos[0] > 200 and 450+80 > pos[1] > 450 and click[0] == 1:
        menuExit = True
        level = 3
    pygame.display.update()

if level == 1:
    speed = 300
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    while not pause:
                        gameDisplay.blit(font.render("Paused", True, white), (320, 200))
                        gameDisplay.blit(font.render("Press c to continue or q to quit", True, white), (40, 300))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                    pause = True
                                if event.key == pygame.K_q:
                                    pygame.quit()
                                    quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and person.x < 750:
            person = person.move(1, 0)
        elif keys[pygame.K_LEFT] and person.x > 0:
            person = person.move(-1, 0)

        gameDisplay.fill(black)
        for n in range(len(rectlist)):
            #pygame.draw.rect(gameDisplay, white, rectlist[n])
            gameDisplay.blit(img1, rectlist[n])

        for n in range(len(rectlist)):
            rectlist[n] = rectlist[n].move(0, 1)

            if person.colliderect(rectlist[n]):
                gameExit = True
            if rectlist[n].y == 600:
                rectlist[n].y = 1
                add = True

        if add:
            temp = pygame.Rect(random.randrange(20, 770), 1, 15, 15)
            rectlist.append(temp)
            add = False
            if speed != 450:
                speed += 50

        if (7 <= len(rectlist) <= 10) and len(poweruplist) >= 2:
            pygame.draw.rect(gameDisplay, red, power_up1)
            if person.colliderect(power_up1):
                poweruplist.remove(power_up1)
                speed = 300

        if 20 <= len(rectlist) <= 24:
            for item in poweruplist:
                if item == power_up2:
                    pygame.draw.rect(gameDisplay, purple, power_up2)
                    if person.colliderect(power_up2):
                        poweruplist.remove(power_up2)
                        img = pygame.transform.scale(img, (30, 30))
                        person = pygame.Rect(person.x, person.y, 30, 30)
                        speed = 300
        #pygame.draw.rect(gameDisplay, green, person)
        gameDisplay.blit(img, person)
        text = font.render("Score: " + str((len(rectlist)-1)), True, blue)
        gameDisplay.blit(text, (2, 2))
        pygame.display.update()
        clock.tick(speed)

if level == 2:
    speed = 400
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    while not pause:
                        gameDisplay.blit(font.render("Paused", True, white), (320, 200))
                        gameDisplay.blit(font.render("Press c to continue or q to quit", True, white), (40, 300))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                    pause = True
                                if event.key == pygame.K_q:
                                    pygame.quit()
                                    quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and person.x < 750:
            person = person.move(1, 0)
        elif keys[pygame.K_LEFT] and person.x > 0:
            person = person.move(-1, 0)

        gameDisplay.fill(black)
        for n in range(len(rectlist)):
            #pygame.draw.rect(gameDisplay, white, rectlist[n])
            gameDisplay.blit(img1, rectlist[n])

        for n in range(len(rectlist)):
            rectlist[n] = rectlist[n].move(0, 1)

            if person.colliderect(rectlist[n]):
                gameExit = True
            if rectlist[n].y == 600:
                rectlist[n].y = 1
                add = True

        if add:
            temp = pygame.Rect(random.randrange(20, 770), 1, 15, 15)
            rectlist.append(temp)
            add = False
            if speed != 550:
                speed += 50

        if (7 <= len(rectlist) < 10) and len(poweruplist) >= 2:
            pygame.draw.rect(gameDisplay, red, power_up1)
            if person.colliderect(power_up1):
                poweruplist.remove(power_up1)
                speed = 400

        if 12 <= len(rectlist) < 18:
            for item in poweruplist:
                if item == power_up2:
                    pygame.draw.rect(gameDisplay, purple, power_up2)
                    if person.colliderect(power_up2):
                        poweruplist.remove(power_up2)
                        img = pygame.transform.scale(img, (30, 30))
                        person = pygame.Rect(person.x, person.y, 30, 30)
                        speed = 400
        #pygame.draw.rect(gameDisplay, green, person)
        gameDisplay.blit(img, person)
        text = font.render("Score: " + str((len(rectlist)-1)), True, blue)
        gameDisplay.blit(text, (2, 2))
        pygame.display.update()
        clock.tick(speed)

if level == 3:
    speed = 600
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    while not pause:
                        gameDisplay.blit(font.render("Paused", True, white), (320, 200))
                        gameDisplay.blit(font.render("Press c to continue or q to quit", True, white), (40, 300))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                    pause = True
                                if event.key == pygame.K_q:
                                    pygame.quit()
                                    quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and person.x < 750:
            person = person.move(1, 0)
        elif keys[pygame.K_LEFT] and person.x > 0:
            person = person.move(-1, 0)

        gameDisplay.fill(black)
        for n in range(len(rectlist)):
            #pygame.draw.rect(gameDisplay, white, rectlist[n])
            gameDisplay.blit(img1, rectlist[n])

        for n in range(len(rectlist)):
            rectlist[n] = rectlist[n].move(0, 1)

            if person.colliderect(rectlist[n]):
                gameExit = True
            if rectlist[n].y == 600:
                rectlist[n].y = 1
                add = True

        if add:
            temp = pygame.Rect(random.randrange(20, 770), 1, 15, 15)
            rectlist.append(temp)
            add = False
            if speed != 750:
                speed += 50

        if (7 <= len(rectlist) < 10) and len(poweruplist) >= 2:
            pygame.draw.rect(gameDisplay, red, power_up1)
            if person.colliderect(power_up1):
                poweruplist.remove(power_up1)
                speed = 600

        if 12 <= len(rectlist) < 18:
            for item in poweruplist:
                if item == power_up2:
                    pygame.draw.rect(gameDisplay, purple, power_up2)
                    if person.colliderect(power_up2):
                        poweruplist.remove(power_up2)
                        img = pygame.transform.scale(img, (30, 30))
                        person = pygame.Rect(person.x, person.y, 30, 30)
                        speed = 600
        #pygame.draw.rect(gameDisplay, green, person)
        gameDisplay.blit(img, person)
        text = font.render("Score: " + str((len(rectlist)-1)), True, blue)
        gameDisplay.blit(text, (2, 2))
        pygame.display.update()
        clock.tick(speed)

EndMenuExit = False
while not EndMenuExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EndMenuExit = True
#    gameDisplay.fill(black)
    gameDisplay.blit(text, (300, 250))
    pygame.display.update()

pygame.quit()
quit()
