import pygame
import random

def generateEnemy():
    enemyImg.append(pygame.image.load(random.choice(enemyImgList)))
    enemyX.append(random.randint(50,830))
    enemyY.append(random.randint(0,100))
    enemyChangeX.append(6)

def showScore(X, Y):
    score = Scorefont.render('Score: '+str(scoreValue),True, (98, 232, 202))
    screen.blit(score, (X,Y))


def player(X,Y):
    screen.blit(playerImg,(X,Y))

def enemy(X,Y, i):
    screen.blit(enemyImg[i], (X,Y))

def fireBullet(X,Y):
    global BulletState
    BulletState = "fired"
    screen.blit(BulletImg, (X+16,Y+16))

def isCollision(X1, X2, Y1, Y2):
    distance = (((X1 - X2)**2) + ((Y1 - Y2)**2))**(1/2)
    if distance <= 25:
        return True
    else:
        return False

def gameOver():
    global enemyChangeY
    global BulletChangeY
    text = GameOverFont.render("GameOver",True, (98, 232, 202))
    screen.blit(text, (55,250))
    for xChange in range(len(enemyChangeX)):
        enemyChangeX[xChange] = 0
    enemyChangeY = 0
    BulletChangeY = 0


pygame.init()#initiation of pygame

enemyImgList = ["enemy1.png", "enemy2.png", "enemy3.png"]

screen = pygame.display.set_mode((900, 700))

pygame.display.set_caption("space invador")
icone = pygame.image.load("spaceship.png")
pygame.display.set_icon(icone)



backGround = pygame.image.load("back_Ground.png")


playerImg = pygame.image.load("spaceship.png")
playerX = 300
playerY = 500
changePlayerPosition = 0



enemyY = []
enemyX = []
enemyImg = []
enemyChangeY = 25
enemyChangeX = []
numberOfEnemies = 5

for i in range(numberOfEnemies):
    generateEnemy()




BulletImg = pygame.image.load("bullet.png")
BulletX = 0
BulletY = 500
BulletChangeY = 15
BulletState = "Loaded"


scoreValue = 0
scoreX = 20
scoreY = 600
Scorefont = pygame.font.Font("freesansbold.ttf", 32)

GameOverFont = pygame.font.Font("freesansbold.ttf", 150)



running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(backGround, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                changePlayerPosition -= 15
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                changePlayerPosition += 15
            elif event.key == pygame.K_SPACE:
                if BulletState == "Loaded":
                    BulletX = playerX
                    fireBullet(BulletX, BulletY)

        elif event.type == pygame.KEYUP:
            changePlayerPosition = 0

    if BulletY <= 0:
        BulletY = 500
        BulletState = "Loaded"


    if playerX <=2:
            playerX = 2
    elif playerX >= 834:
            playerX = 834

    for i in range(numberOfEnemies):
        enemyX[i] += enemyChangeX[i]
        if enemyX[i] <=0:
                enemyChangeX[i] = 6
                enemyY[i] += enemyChangeY
        elif enemyX[i] >= 836:
                enemyChangeX[i] = -6
                enemyY[i] += enemyChangeY

        collision = isCollision(enemyX[i], BulletX, enemyY[i], BulletY)
        if  collision and BulletState == "fired":
            BulletY = 500
            BulletState = "Loaded"
            scoreValue += 1
            enemyX[i] = random.randint(50, 830)
            enemyY[i] = random.randint(0,100)

        enemy(enemyX[i], enemyY[i], i)
        enemyX[i] += enemyChangeX[i]

        if enemyY[i] > 470:
            gameOver()



    if BulletState == "fired":
        fireBullet(BulletX, BulletY)
        BulletY -= BulletChangeY


    
    playerX += changePlayerPosition
    player(playerX, playerY)
 
    showScore(scoreX, scoreY)
    
    
    pygame.display.update()
