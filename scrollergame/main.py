import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
background = pygame.image.load("galaxy.jpg")
pygame.display.set_icon(icon)

#player
playerImage = pygame.image.load("spaceship64.png")
enemyImage = pygame.image.load("ufo.png")
bulletImage = pygame.image.load("bullet.png")
playerX = 380
playerY = 510

enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 5

for i in range(no_of_enemies):
    enemyX.append(random.randint(5,795))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(5)
    enemyY_change.append(5)

bulletX=0
bulletY=510
bulletX_change=playerX
bulletY_change=playerY
#ready means you can't see the bullet. fire means you can see it
bullet_state="ready"

#draw your player
def player():
    screen.blit(playerImage, (playerX, playerY))

#draw your enemy
def enemy(x,y):
    screen.blit(enemyImage, (x, y))

def bullet_fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x+30, y))

def collision_detect(x1, x2, y1, y2):
    x = math.pow((x1-x2),2)
    y = math.pow((y1-y2),2)
    distance = math.sqrt(x+y)
    if distance < 27:
        return True
    else:
        return False

#show score
def show_show(x,y):
    rendered_score = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(rendered_score, (x,y))



running = True
playerX_change=0


def updateScore(score):
    screen.blit(score, (10,10))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change=10
            if event.key == pygame.K_LEFT:
                playerX_change=-10
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=playerX
                    bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
               playerX_change=0


    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    playerX+=playerX_change

    if playerX <=0:
        playerX=0
    if playerX >= 736:
        playerX=736



    for i in range(no_of_enemies):
        enemyY_change[i] = 30
        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]


        if enemyX[i] >= 736:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]




        # collision detection
        collision = collision_detect(enemyX[i], bulletX, enemyY[i], bulletY)
        if collision:
            bulletY = 510
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(5, 795)
            enemyY[i] = random.randint(50, 100)

        #enemyY[i] += enemyY_change[i]
        enemyX[i] += enemyX_change[i]
        enemy(enemyX[i]+enemyX_change[i], enemyY[i])

    if bulletY <= 0:
        bulletY = 510
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet_fire(bulletX,bulletY)
        bulletY-=20


    player()
    show_show(textX, textY)

    pygame.display.update()


pygame.quit()