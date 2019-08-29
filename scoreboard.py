import pygame
class Scoreboard():
    def __init__(self,ai_settings,screen,status):
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.status =status

        #字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #准备初始得分图像
        self.prep_score()
        self.prep_highscore()

    def prep_score(self):
        score_str = "score:"+str(self.status.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #放在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highscore(self):
        high_score_str = "highscore:"+str(self.status.high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        #放在正中间
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)


class Lifeboard():
    def __init__(self,ai_settings,screen,status):
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.status =status

        #字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #准备生命图像
        self.prep_life()

    def prep_life(self):
        life_str = str(self.status.ships_left)
        self.life_image = self.font.render(life_str,True,self.text_color,self.ai_settings.bg_color)
        #放在右上角
        self.score_rect = self.life_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def show_life(self,status):
        self.status = status
        life_str = "ship:"+str(self.status.ships_left)
        self.life_image = self.font.render(life_str,True,self.text_color,self.ai_settings.bg_color)
        self.screen.blit(self.life_image,self.score_rect)
