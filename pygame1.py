# Pygame
# Image - Trình bày nhân vật + nền + hoạt cảnh
# Logic - Điều khiển nhân vật

import random
from numpy import char
import pygame
import math

class installation:

    def __init__(self):
        self.loop = True
        self.title_screen = "Pong"
        self.width_screen = 800
        self.height_screen = 600
        self.background_screen = (70,70,70)
        self.clock = pygame.time.Clock()
        self.pygame = pygame
        

    def event(self):
        self.events = self.pygame.event.get()

        for e in self.events:
            if e.type == pygame.QUIT:
                self.loop = False

        self.player_one.event()
        self.player_two.event()
        if self.player_one.rect.colliderect(self.ball.rect) or self.player_two.rect.colliderect(self.ball.rect):
            self.ball.eventbounce()
        else :
            self.ball.eventnormal()

    def render(self):
        self.canvas.fill(self.background_screen)
        ###
        self.player_one.render()
        self.player_two.render()
        self.ball.render()

        ###
        self.clock.tick(60)
        self.pygame.display.flip()

    def start(self):
        self.pygame.init()
        self.pygame.display.set_caption(self.title_screen)
        self.canvas = self.pygame.display.set_mode((self.width_screen,self.height_screen))
        # Init
        self.player_one = Player(self,1)
        self.player_two = Player(self,2)
        self.ball = Ball(self)
        while self.loop:
            # Handle Event
            self.event()
            # Handle Render
            self.render()
            
class Player:
    def __init__(self,game,player):
        self.game = game

        self.width = 30
        self.height = 120

        self.player = player
        self.speed_y = 10
        # 
        self.x = 0
        if self.player != 1:
            self.x = self.game.width_screen - self.width
        self.y = self.game.height_screen/2 - self.height/2
        #
        self.pygame = self.game.pygame
        self.canvas = self.game.canvas
        self.image = self.pygame.image.load("D:/.vscode/assets/paddle.png")
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
    def event(self):
        pressed = self.game.pygame.key.get_pressed()

        keyUp = None
        keyDown = None

        if self.player == 1:
            keyUp = pygame.K_w
            keyDown = pygame.K_s
        else:
            keyUp = pygame.K_UP
            keyDown = pygame.K_DOWN


        if pressed[keyUp]:
            if self.rect.y <= 0:
                self.rect.y = 0
            else:
                self.rect.y -= self.speed_y
        elif pressed[keyDown]:
            if self.rect.y >= self.game.height_screen - self.height:
                self.rect.y = self.game.height_screen - self.height
            else:
                self.rect.y += self.speed_y


    def render(self):
        self.canvas.blit(self.image, self.rect)

class Ball:
    def __init__(self,game):
        # game = Pong
        self.game = game

        self.point1 = 0
        self.point2 = 0
        self.speed_y = 5
        self.speed_x = 5

        self.width = 20
        self.height = 20
        
        self.x = (self.game.width_screen / 2) - (self.width / 2)
        self.y = random.randint((self.height / 2),self.game.height_screen  - (self.height / 2))
        #
        self.pygame = self.game.pygame
        self.canvas = self.game.canvas
        self.image = self.pygame.image.load("D:/.vscode/assets/ball.png")
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
    def eventnormal(self):

        # Va chạm vào tường phải - trái
        if self.rect.x >= self.game.width_screen - self.width:
            self.rect.x = self.game.width_screen /2
            self.rect.y = self.game.height_screen /2
            self.speed_x *= -1
            self.point1+=1

        if self.rect.x <= 0:
            self.rect.x = self.game.width_screen /2
            self.rect.y = self.game.height_screen /2
            self.speed_x *= -1
            self.point2+=1

        # Va chạm vào tường trên - dưới
        if self.rect.y >= self.game.height_screen - self.height:
            self.rect.y = self.game.height_screen - self.height
            self.speed_y *= -1

        if self.rect.y <= 0:
            self.rect.y = 0
            self.speed_y *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.text1 = self.font.render(str(self.point1), True, (255,255,255))
        self.text2 = self.font.render(str(self.point2), True, (255,255,255))
    def eventbounce(self):
        self.speed_x *= -1
        self.speed_y *=-1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def render(self):
        self.canvas.blit(self.image, self.rect)
        self.canvas.blit(self.text1, (30, 30))
        self.canvas.blit(self.text2, (750, 30))
game = installation()
game.start()