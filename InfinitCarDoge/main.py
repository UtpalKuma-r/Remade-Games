import pygame
import sys
import random
import os
from pygame import mixer

pygame.init()

#Game Constants------------------------------------------------------------
SIZE = WIDTH, HEIGHT = 600, 700
SCALE = (90, 100)
Font = pygame.font.Font("freesansbold.ttf", 50)
small_font = pygame.font.Font("freesansbold.ttf", 40)
#---------------------------------------------------------------------------

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('InfinitCarDodger')

class obstecal:
    def __init__(self, image, x_coordinate, scale):
        self.image = pygame.transform.scale(pygame.image.load(image), scale)
        self.x_coordinate = x_coordinate
        self.y_coordinate = 0
        self.rect = self.image.get_rect()


    def move(self, y_velocity):
        if self.y_coordinate <= 700:
            self.y_coordinate += y_velocity

class backgroundclass(obstecal):

    def move(self, y_velocity):
        if self.y_coordinate >= 0:
            self.y_coordinate = -700
            
        else:
            self.y_coordinate += y_velocity
        
class playerclass:

    def __init__(self, image):
        self.spawn_location = [5, 105, 205, 305]
        self.image = pygame.transform.scale(pygame.image.load(image), SCALE)
        self.x_coordinate = random.choice(self.spawn_location)
        self.rect = self.image.get_rect()
        self.y_coordinate = HEIGHT-self.rect.height
        self.move_right = False
        self.move_left = False

    def move(self, x_velocity):
        if self.move_left and self.x_coordinate - x_velocity > 0:
            self.x_coordinate -= x_velocity
        elif self.move_right and self.x_coordinate + x_velocity < 400-self.rect.width:
            self.x_coordinate += x_velocity
        
def display(image, coordinates):
    screen.blit(image, coordinates)

def collision(object1, object2):
    x1, y1, x2, y2 = object1.x_coordinate + (object1.rect.width/2), object1.y_coordinate + (object1.rect.height/2), object2.x_coordinate + (object2.rect.width/2), object2.y_coordinate + (object2.rect.height/2)
    
    distance = ((x1-x2)**2+(y1-y2)**2)**0.5
    if distance < 80:
        return True
    
    return False

class game_flow:

    def __init__(self) -> None:
        #Game variables-------------------------------------------------------------
        self.game_state = "intro"
        self.spawn_location = [5, 105, 205, 305]
        self.y_velocity = 1
        self.x_velocity = 1.5
        self.obstecal_list = []
        self.score = 0
        self.enemy_spawn = 1
        self.explosion_played = False
        self.background = backgroundclass("images/background/background.png", 0, (400, 1400))
        self.gameover = False
        self.player = playerclass("images/player/car6.png")
        #---------------------------------------------------------------------------
    
    def intro(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game_state = "main"
                self.restart()

        screen.fill((0,0,0))

        self.background.move(self.y_velocity)
        display(self.background.image, (self.background.x_coordinate, self.background.y_coordinate))     

        last_enemy = self.obstecal_list[-1]
        if last_enemy.y_coordinate > (self.enemy_spawn + 1)*self.player.rect.height:
            selected_location = random.sample(self.spawn_location, self.enemy_spawn)
            for _ in range(self.enemy_spawn):
                enemy_image = random.choice(os.listdir("images/obstecale"))
                enemy_obj = obstecal(f"images/obstecale/{enemy_image}", selected_location[_], SCALE)
                self.obstecal_list.append(enemy_obj) 

        for enemy in self.obstecal_list:
            enemy.move(self.y_velocity)
            display(enemy.image, (enemy.x_coordinate, enemy.y_coordinate))

        pygame.display.flip()

    def main(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_a, pygame.K_LEFT):
                    self.player.move_left = True
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    self.player.move_right = True

                elif event.key == pygame.K_r and self.gameover:
                    self.restart()

            
            elif event.type == pygame.KEYUP:

                if event.key in (pygame.K_a, pygame.K_LEFT):
                    self.player.move_left = False
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    self.player.move_right = False
            
        screen.fill((0,0,0))

        self.background.move(self.y_velocity)
        display(self.background.image, (self.background.x_coordinate, self.background.y_coordinate))
        display(Font.render(str(round(self.score)), True, (0,0,255)), (475,0))


        last_enemy = self.obstecal_list[-1]
        if last_enemy.y_coordinate > (self.enemy_spawn + 1)*self.player.rect.height:
            selected_location = random.sample(self.spawn_location, self.enemy_spawn)
            for _ in range(self.enemy_spawn):
                enemy_image = random.choice(os.listdir("images/obstecale"))
                enemy_obj = obstecal(f"images/obstecale/{enemy_image}", selected_location[_], SCALE)
                self.obstecal_list.append(enemy_obj)   


        for enemy in self.obstecal_list:

            if enemy.y_coordinate > 700:
                self.obstecal_list.remove(enemy)
                del enemy
                if self.enemy_spawn == 1:
                    self.score += 1
                elif self.enemy_spawn == 2:
                    self.score += 0.5
                else:
                    self.score += 0.3
                
                if self.score == 10:
                    self.y_velocity = 1.5
                    self.x_velocity = 2
                elif self.score == 20:
                    self.enemy_spawn = 2
                elif self.score == 30:
                    self.y_velocity = 2
                    self.x_velocity = 2.5
                elif self.score == 40:
                    self.enemy_spawn = 3
                elif self.score == 50:
                    self.y_velocity = 2.5
                    self.x_velocity = 3
                    
    #----------------------------------Colision Detection-------------------------------------------
            elif collision(self.player, enemy):

                display(Font.render("Game",True, (98, 232, 202)), (400,150))
                display(Font.render("Over",True, (98, 232, 202)), (400,200))
                display(small_font.render("To restart", True, (255,0,255)), (400, 350))
                display(small_font.render("press R", True, (255,0,255)), (400, 400))

                self.x_velocity = self.y_velocity = 0
                self.gameover = True
                mixer.music.stop()    #stop the self.background music
                if not self.explosion_played:
                    explosion_sound = mixer.Sound("music/explosion.ogg")
                    explosion_sound.play()
                    self.explosion_played = True
                    


            else:
                enemy.move(self.y_velocity)
                display(enemy.image, (enemy.x_coordinate, enemy.y_coordinate))

        self.player.move(self.x_velocity)
        display(self.player.image, (self.player.x_coordinate, self.player.y_coordinate))


        pygame.display.flip()
    
    #------------------------------Restart Function-----------------------------------
    def restart(self):

        self.y_velocity = 1
        self.x_velocity = 1.5
        self.obstecal_list = []
        self.score = 0
        self.enemy_spawn = 1
        # self.explosion_played = False


        self.background = backgroundclass("images/background/background.png", 0, (400, 1400))

        self.player = playerclass("images/player/car6.png")


        enemy_image = random.choice(os.listdir("images/obstecale"))
        enemy_obj = obstecal(f"images/obstecale/{enemy_image}", random.choice(self.spawn_location), SCALE)
        self.obstecal_list.append(enemy_obj)

        mixer.init()
        mixer.music.load('music/background.ogg')
        mixer.music.play(-1)


    def manager(self):
        
        if self.game_state == "main":
            self.main()

        elif self.game_state == "intro":
            self.intro()

game_play = game_flow()

playing = True
game_play.restart()
while playing:
    game_play.manager()


'''
self.background music:- Music: https://www.chosic.com/free-music/all/ 
'''