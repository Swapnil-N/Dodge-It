__author__ = 'Swapnil'

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
font = pygame.font.SysFont("comicsansms", 50)
font1 = pygame.font.SysFont("comicsansms", 80)
font2 = pygame.font.SysFont("comicsansms", 50)
font3 = pygame.font.SysFont("comicsansms", 30)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dodge it")
pygame.display.update()
img = pygame.image.load("stickman.png")
img1 = pygame.image.load("Fireball.jpg")


while True:                                              # Loop to play the game again

    add = False
    speed = 0
    level = 0
    pause = False
    person = pygame.Rect(400, 540, 48, 48)                          # This block of code resets everything to play again
    fallingBlock = pygame.Rect(400, 1, 15, 15)
    power_up1 = pygame.Rect(random.randrange(50, 750), 540, 30, 30)
    power_up2 = pygame.Rect(random.randrange(50, 750), 540, 30, 30)
    img = pygame.transform.scale(img, (50, 50))
    img1 = pygame.transform.scale(img1, (30, 30))
    clock = pygame.time.Clock()
    rectList = [fallingBlock]
    powerUpList = [power_up1, power_up2]
    gameDisplay.fill(black)

    menuExit = False
    while not menuExit:                                         # The menu loop
        pos = pygame.mouse.get_pos()                        # Gives the mouses position

        for event in pygame.event.get():
            if event.type == pygame.QUIT:                    # allows the X button in the top corner to work
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        name = font.render("Dodge it", True, white)
        gameDisplay.blit(name, (300, 10))

        easyButton = pygame.Rect(200, 150, 400, 80)
        pygame.draw.rect(gameDisplay, blue, easyButton)
        gameDisplay.blit(font.render("Easy", True, white), (350, 150))     # draws the button on the screen
        click = pygame.mouse.get_pressed()
        if 600 > pos[0] > 200 and 230 > pos[1] > 150 and click[0] == 1:
            menuExit = True                                              # Determines if the person is clicking
            level = 1                                                    # on the button and ends the menu loop

        mediumButton = pygame.Rect(200, 300, 400, 80)
        pygame.draw.rect(gameDisplay, green, mediumButton)
        gameDisplay.blit(font.render("Medium", True, white), (310, 300))
        if 600 > pos[0] > 200 and 380 > pos[1] > 300 and click[0] == 1:
            menuExit = True
            level = 2

        hardButton = pygame.Rect(200, 450, 400, 80)
        pygame.draw.rect(gameDisplay, red, hardButton)
        gameDisplay.blit(font.render("Hard", True, white), (340, 450))
        if 600 > pos[0] > 200 and 450+80 > pos[1] > 450 and click[0] == 1:
            menuExit = True
            level = 3

        howToPlayButton = pygame.Rect(620, 540, 175, 55)
        pygame.draw.rect(gameDisplay, orange, howToPlayButton)
        gameDisplay.blit(font3.render("How to play", True, white), (625, 545))
        pygame.display.update()

        if 620 < pos[0] and 540 < pos[1] and click[0] == 1:
            instrExit = False
            while not instrExit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_b:     # Press C to continue
                            instrExit = True

                pos = pygame.mouse.get_pos()                        # Gives the mouses position
                click = pygame.mouse.get_pressed()

                gameDisplay.fill(black)
                gameDisplay.blit(font1.render("How to play", True, red), (190, 40))
                gameDisplay.blit(font3.render("Use arrow keys to control the player.", True, white), (150, 290))
                gameDisplay.blit(font3.render("Dodge the fireballs to gain points.", True, white), (160, 340))
                gameDisplay.blit(font3.render("The red and purple squares are power ups.", True, white), (100, 390))

                backButton = pygame.Rect(5, 540, 175, 55)
                pygame.draw.rect(gameDisplay, orange, backButton)
                gameDisplay.blit(font3.render("Main Menu", True, white), (13, 545))
                pygame.display.update()
                if pos[0] < 180 and 540 < pos[1] and click[0] == 1:
                    instrExit = True


    if level == 1:
        speed = 300
    elif level == 2:
        speed = 400                                     # Setting the initial speed of the game
    elif level == 3:
        speed = 550
    gameExit = False
    while not gameExit:                                 # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:                # if p is pressed then the game will pause
                if event.key == pygame.K_p:
                    pause = False
                    while not pause:                            # Pause menu loop
                        gameDisplay.blit(font.render("Paused", True, white), (320, 200))
                        gameDisplay.blit(font3.render("Press c to continue or q to quit", True, white), (200, 300))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:     # Press C to continue
                                    pause = True
                                if event.key == pygame.K_q:     # Press Q to quit
                                    pygame.quit()
                                    quit()

        keys = pygame.key.get_pressed()                     # Gets all the keys pressed and stores it in a list
        if keys[pygame.K_RIGHT] and person.x < 750:
            person = person.move(1, 0)
        elif keys[pygame.K_LEFT] and person.x > 0:
            person = person.move(-1, 0)

        gameDisplay.fill(black)
        for n in range(len(rectList)):
            #pygame.draw.rect(gameDisplay, white, rectList[n])              Draws all the falling objects
            gameDisplay.blit(img1, rectList[n])

        for n in range(len(rectList)):
            rectList[n] = rectList[n].move(0, 1)                # Moves the falling objects down

            if person.colliderect(rectList[n]):                 # Collision between the player and the falling objects
                gameExit = True                                 # End the game loop and displays the game over screen
            if rectList[n].y == 600:
                rectList[n].y = 1                               # Resets the position of the falling object to the top
                add = True                                      # Adds another block

        if add:
            if level == 1:
                myY = 1
            else:
                myY = 30
            temp = pygame.Rect(random.randrange(20, 770), myY, 15, 15)
            rectList.append(temp)                                      # Adds another block to the falling objects list
            add = False
            if (level == 1 and speed != 450) or (level == 2 and speed != 550) or (level == 3 and speed != 750):
                speed += 50                                             # increments the speed every round

        if (7 <= len(rectList) < 12) and len(powerUpList) >= 2:         # Code for the first power up
            pygame.draw.rect(gameDisplay, red, power_up1)
            if person.colliderect(power_up1):
                powerUpList.remove(power_up1)
                if level == 1:
                    speed = 300
                elif level == 2:                                        # Resets the speed
                    speed = 400
                elif level == 3:
                    speed = 550

        if 15 <= len(rectList) < 25:                                    # code for the second power up
            for item in powerUpList:
                if item == power_up2:
                    pygame.draw.rect(gameDisplay, purple, power_up2)
                    if person.colliderect(power_up2):
                        powerUpList.remove(power_up2)
                        img = pygame.transform.scale(img, (30, 30))            # Second power up makes character smaller
                        person = pygame.Rect(person.x, person.y, 30, 30)
                        if level == 1:
                            speed = 300
                        elif level == 2:
                            speed = 400
                        elif level == 3:
                            speed == 550
        #pygame.draw.rect(gameDisplay, green, person)
        gameDisplay.blit(img, person)
        text = font.render("Score: " + str((len(rectList)-1)), True, blue)          # Draws the score on the score
        gameDisplay.blit(text, (2, 2))
        pygame.display.update()
        clock.tick(speed)                                                           # Sets the speed of the game

    EndMenuExit = False
    while not EndMenuExit:                                                      # Game over loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    EndMenuExit = True
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        pygame.draw.rect(gameDisplay, black, pygame.Rect(0, 0, 250, 80))
        gameDisplay.blit(font1.render("Game Over", True, red), (190, 40))                             # Draws the text
        gameDisplay.blit(font2.render("Score: " + str((len(rectList)-1)), True, blue), (300, 200))
        gameDisplay.blit(font3.render("Press r to retry or q to quit", True, white), (210, 340))

        pygame.display.update()


pygame.quit()
quit()