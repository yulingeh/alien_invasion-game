import sys
import pygame
from bullet import Bullet
import random
from alien import Alien


def check_event_keydown(event,ai_settings,screen,ship,bullets,ai_settings2): #只要飞船移动或者按空格就会发射子弹
    if event.key == pygame.K_RIGHT:
                    #向右移动飞船
        ship.moving_right = True
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_LEFT:
                     #向左移动飞船
        ship.moving_left = True
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_UP:
        ship.moving_up = True
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key ==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    #num_big限定发射大招的数目为num_big
    elif event.key == pygame.K_a and ai_settings2.num_big > 0:
        fire_bullet(ai_settings2,screen,ship,bullets)
        ai_settings2.num_big -= 1

        

def check_event_keyup(event,ship):
     if event.key == pygame.K_RIGHT:
             ship.moving_right = False
     elif event.key == pygame.K_LEFT:
             ship.moving_left = False
     elif event.key ==  pygame.K_UP:
             ship.moving_up = False
     elif event.key ==  pygame.K_DOWN:
             ship.moving_down = False
def check_events(ai_settings,screen,ship,bullets,ai_settings2,status,play_button):
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.quit
            elif event.type == pygame.KEYDOWN:
                check_event_keydown(event,ai_settings,screen,ship,bullets,ai_settings2)
            elif event.type == pygame.KEYUP:
                check_event_keyup(event,ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_button(status,play_button,mouse_x,mouse_y)

def check_play_button(status,play_button,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not status.game_active:
        status.game_active = True
       
            

def update_screen(ai_settings,screen,ship,bullets,aliens,status,play_button,sb,life):
     #每次循环都重新绘制屏幕
        screen.fill(ai_settings.bg_color)
        #在飞船和外星人后面绘制所有子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        #alien.blitme()
        aliens.draw(screen)

        if not status.game_active:
            play_button.draw_button()
        #更新当前分数和最高分显示
        sb.show_score()
        #更新飞船剩余生命值
        life.show_life(status)
        
        #让最近绘制的屏幕可见
        pygame.display.flip()

def update_bullets(aliens,bullets,status,ai_settings,sb):
        #更新子弹位置
        bullets.update()
        #删除跑出屏幕的子弹
        for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
        #有子弹击中敌人，子弹和外星人消失
        collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
        if collisions:
            status.score += ai_settings.alien_points
            sb.prep_score()
        check_high_score(status,sb)
                    
       
def fire_bullet(ai_settings,screen,ship,bullets):
    #增加子弹数目
     new_bullet =Bullet(ai_settings,screen,ship)
     bullets.add(new_bullet)

def update_aliens(aliens,screen):
    screen_rect = screen.get_rect()
    aliens.update(screen_rect)

def creat_fleet(ai_settings,screen,aliens):
    x1 = random.randint(1,3)
    cache = 0
    while x1>0:
        alien = Alien(ai_settings,screen)
        alien.rect.left =random.randint(0,1080) #每个外星人x位置随机
        #防止位置重叠     
        #while alien.rect.x - cache < alien.rect.width:
         #   alien.rect.x =random.randint(0,1080)
        #cache =  alien.rect.x
        aliens.add(alien)        
        x1 -= 1

def check_coll(ship,aliens,status,bullets,screen,ai_settings):
    if pygame.sprite.spritecollideany(ship,aliens):
        status.ships_left -= 1
        aliens.empty()
        bullets.empty()
        screen_rect =screen.get_rect()
        ship.rect.centerx = screen_rect.centerx
        ship.rect.bottom = screen_rect.bottom
        
       
        if status.ships_left >0:
            return True
        else:
            status.game_active = False
            return False

def check_bottom_aliens(ship,aliens,status,bullets,screen):
    screen_rect =screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            status.ships_left -= 1
            aliens.empty()
            bullets.empty()          
            ship.rect.centerx = screen_rect.centerx
            ship.rect.bottom = screen_rect.bottom
            if status.ships_left >0:
                return True
            else:
                status.game_active = False
                return False
        
def check_high_score(status,sb):
    if status.score > status.high_score:
        status.high_score =status.score
        sb.prep_highscore()
        #filename = "G:/python project/alien_invasion/alien_invasion/highscore.txt"
        with open('highscore.txt','w+')as file_object:
            file_object.write(str(status.high_score))
            file_object.close()