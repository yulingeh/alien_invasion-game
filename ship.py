import pygame
class Ship():
    def __init__(self,screen,ai_settings):
        self.screen = screen

        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect =self.screen.get_rect()
        self.ai_settings = ai_settings
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
       
       #将每艘飞船放在屏幕底部或者中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left> 0:
                self.rect.centerx -= self.ai_settings.ship_speed
        if self.moving_up and self.rect.top >= self.screen_rect.top:
                self.rect.centery -= self.ai_settings.ship_speed
        if self.moving_down and self.rect.bottom <self.screen_rect.bottom :
                self.rect.centery += self.ai_settings.ship_speed


        

    def blitme(self):
        #在指定位置放置飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
