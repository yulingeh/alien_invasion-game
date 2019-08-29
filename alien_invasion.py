from ship import Ship
from settings import Settings
import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien
from time import sleep
from game_status import Game_status
from button import Button
from scoreboard import Scoreboard,Lifeboard
import os



def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #所有正常设定
    ai_settings = Settings()
    #只是大子弹设定不同,宽度很大
    ai_settings2 = Settings()
    ai_settings2.bullet_width =500
    #screen作为储存屏幕的变量
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #设置名字
    pygame.display.set_caption("Alien Invasion")
    #创建play按钮
    play_button = Button(ai_settings,screen,"play")
    #创建一艘飞船，传入screen参量是因为飞船的初始化位置在screen的底部中心
    ship1 = Ship(screen,ai_settings)
    #创建用于储存子弹的编组
    bullets= Group()
    #创建一个外星人
    alien1 = Alien(ai_settings,screen)
    #创建一个外星人群
    aliens = Group()
    gf.creat_fleet(ai_settings,screen,aliens)
    i=0
    #创建一个统计游戏信息地实例
    status = Game_status(ai_settings)
    #创建一个记分牌
    sb = Scoreboard(ai_settings,screen,status)
    #创建一个飞船生命牌
    life = Lifeboard(ai_settings,screen,status)

    #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship1,bullets,ai_settings2,status,play_button)
        
        #飞船数目不为0,才能游戏
        if status.game_active:
        #更新飞船位置
            ship1.update()
        #更新子弹
            gf.update_bullets(aliens,bullets,status,ai_settings,sb)
        #更新外星人位置
            gf.update_aliens(aliens,screen)
        #不断增加外星人
            i += 1
            if i == 400:
                i = 0
                gf.creat_fleet(ai_settings,screen,aliens)
        
        #如果飞船和外星人相撞，游戏暂停1s
            if gf.check_coll(ship1,aliens,status,bullets,screen,ai_settings):
                sleep(1)
        #如果有外星人到达最底端，游戏暂停1s
            if gf.check_bottom_aliens(ship1,aliens,status,bullets,screen):
                sleep(1)
        
       
        #更新屏幕
        gf.update_screen(ai_settings,screen,ship1,bullets,aliens,status,play_button,sb,life)
        sleep(0.005)  #秒

run_game()



