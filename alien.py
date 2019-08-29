import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载外星人图像，并设置边缘 
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人的初始位置
        
        self.rect.x  =self.rect.width               
        self.rect.y = self.rect.height

        #储存外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #获取屏幕信息
        self.screen_rect =self.screen.get_rect()
    def blitme(self):
         self.screen.blit(self.image,self.rect)
    def update(self,screen_rect):
        x = random.randint(0,100)
        y = random.randint(0,100)
        if x < 35 and self.rect.right < (self.screen_rect.right-self.rect.width):
            self.x += 12        
        elif x > 65:
            self.x -= 12
        if y > 50:
            self.y += self.ai_settings.alien_speed
        
        if self.x > self.rect.width :    
            self.rect.x = self.x
        self.rect.y = self.y
        
