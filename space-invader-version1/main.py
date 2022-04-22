import random

import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

# set title
pygame.display.set_caption("Space Invader")

# set icon
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

background = pygame.image.load("5509862.jpg")

playerImg = pygame.image.load("space-invaders.png")
playerImgX = 370
playerImgY = 480
playerX_changed = 0
playerY_changed = 0

monsterImg = []
monsterImgX = []
monsterImgY = []
monsterX_changed = []
monsterY_changed = []

for i in range (6):

    monsterImg.append (pygame.image.load("monster.png") )
    monsterImgX.append( random.randint(0, 800) )
    monsterImgY.append( random.randint(0, 150) )
    monsterX_changed.append(1)
    monsterY_changed.append(30)

bulletImg = pygame.image.load("bullet.png")
bulletImgX = 370
bulletImgY = 480
bulletX_changed = 0
bulletY_changed = 4
bullet_state = "ready"

score = 0
font = pygame.font.Font("space_invaders.ttf",32)
textX = 10
textY = 10

over = pygame.font.Font("space_invaders.ttf",32)

def game_over():
    text = font.render("GAME OVER",True,(255,0,0))
    screen.blit(text, (200, 250))

def show_score(x,y):
    score_val = font.render("Score: "+ str(score), True, (255,0,0))
    screen.blit(score_val, (x,y))


def monster(x, y, i):
    screen.blit(monsterImg[i], (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(monsterX, monsterY, bulletX, bulletY):
    distance = math.sqrt(math.pow(monsterX - bulletX, 2) + math.pow(monsterY - bulletY, 2))
    if distance<20:
        return True
    else:
        return False


down = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_changed -= 4
            if event.key == pygame.K_RIGHT:
                playerX_changed += 4
            if event.key == pygame.K_UP:
                playerY_changed -= 4
            if event.key == pygame.K_DOWN:
                playerY_changed += 4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerImgX
                    fire_bullet(bulletX, bulletImgY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_changed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_changed = 0

    playerImgX += playerX_changed
    playerImgY += playerY_changed

    if playerImgX <= 0:
        playerImgX = 0
    elif playerImgX >= 736:
        playerImgX = 736

    if playerImgY <= 0:
        playerImgY = 0
    elif playerImgY >= 536:
        playerImgY = 536

    for i in range(6):

        if monsterImgY[i]>500:
            for j in range(6):
                monsterImg[j] = 2000
            game_over()
            break
        monsterImgX[i] += monsterX_changed[i]

        if monsterImgX[i] <= 0:
            monsterX_changed[i] = 0.5
            monsterImgY[i] += monsterY_changed[i]

        elif monsterImgX[i] >= 736:
            monsterX_changed[i] = -0.5
            monsterImgY[i] += monsterY_changed[i]

        if monsterImgY[i] >= 536:
            monsterImgY[i] = 0

        collision = isCollision(monsterImgX[i], monsterImgY[i], bulletImgX, bulletImgY)

        if collision:
            bulletImgY = 480
            bullet_status = "ready"
            score += 1
            print(score)
            monsterImgX[i] = random.randint(0, 800)
            monsterImgY[i] = random.randint(0, 150)

        monster(monsterImgX[i], monsterImgY[i],i)

    if bulletImgY <= 0:
        bulletImgY = 480
        bullet_state = "ready"

    if bullet_state == "fired":
        fire_bullet(bulletX, bulletImgY)
        bulletImgY -= bulletY_changed

    show_score(textX, textY )
    player(playerImgX, playerImgY)
    pygame.display.update()
