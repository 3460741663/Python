#-*-coding:GBK -*- 
import sys

import pygame

from time import sleep

from bullet import Bullet

from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets,aliens):
    """��Ӧ����"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    #W
    elif event.key == pygame.K_w:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'w' :
            fire_bullet(ai_settings,screen,ship,bullets)
            
            print(alien.word[0])
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #E
    elif event.key == pygame.K_e:
		
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'e' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #R
    elif event.key == pygame.K_r:
        alien = ai_settings.aliense.pop()
        
        if alien.word[0] == 'r' :
            fire_bullet(ai_settings,screen,ship,bullets)
            print(alien.word[0])
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #T
    elif event.key == pygame.K_t:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 't' :
            fire_bullet(ai_settings,screen,ship,bullets)
            print(alien.word[0])
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
                    
    #Y
    elif event.key == pygame.K_y:
        alien = ai_settings.aliense.pop()
        
        if alien.word[0] == 'y' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #U
    elif event.key == pygame.K_u:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'u' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #I
    elif event.key == pygame.K_i:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'i' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #O
    elif event.key == pygame.K_o:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'o' :
            fire_bullet(ai_settings,screen,ship,bullets)
            print(alien.word[0])
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #P
    elif event.key == pygame.K_p:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'p' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #A
    elif event.key == pygame.K_a:
        
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'a' :
            print(alien.word[0])
            
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
    #S
    elif event.key == pygame.K_s:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 's' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #D
    elif event.key == pygame.K_d:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'd' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #F
    elif event.key == pygame.K_f:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'f' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
            
    #G
    elif event.key == pygame.K_g:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'g' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #H
    elif event.key == pygame.K_h:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'h' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #J
    elif event.key == pygame.K_j:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'j' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
        
    #K
    elif event.key == pygame.K_k:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'k' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
    #L
    elif event.key == pygame.K_l:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'l' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
    #Z
    elif event.key == pygame.K_z:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'z' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
    #X
    elif event.key == pygame.K_x:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'x' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
    #C
    elif event.key == pygame.K_c:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'c' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
    #V
    elif event.key == pygame.K_v:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'v' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
    #B
    elif event.key == pygame.K_b:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'b' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
    #N
    elif event.key == pygame.K_n:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'n' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)
    #m
    elif event.key == pygame.K_m:
        alien = ai_settings.aliense.pop()
        if alien.word[0] == 'm' :
            print(alien.word[0])
            fire_bullet(ai_settings,screen,ship,bullets)
            alien.word = alien.word.lstrip(alien.word[0])
            ai_settings.aliense.append(alien)
            if alien.word.strip()=='':
                aliens.remove(alien)
                ai_settings.aliense.pop()
            print(alien.word)
        else:
            ai_settings.aliense.append(alien)                
    
def fire_bullet(ai_settings,screen,ship,bullets):
    """�����û�дﵽ���ƣ��ͷ���һ���ӵ�"""
    #����һ���ӵ�����������뵽����bullet��
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        

def check_keyup_events(event,ship):
    """��Ӧ�ɿ�"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
                    

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """��Ӧ����������¼�"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ai_settings,screen,ship,bullets,aliens)
                
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
                
                
                
                

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """����ҵ���Play��ťʱ��ʼ��Ϸ"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #������Ϸ����
        ai_settings.initialize_dynamic_settings()
        #���ع��
        pygame.mouse.set_visible(False)
        #������Ϸͳ����Ϣ
        stats.reset_stats()
        stats.game_active = True
        
        #���üǷ���ͼ��
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ship()
        
        #����������б���ӵ��б�
        aliens.empty()
        bullets.empty()
        
        #����һȺ�����ˣ����÷ɴ�����
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
            	
                
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
	#ÿ��ѭ���Ƕ��ػ���Ļ
    screen.fill(ai_settings.bg_color)
    #�ڷɴ��������˺����ػ������ӵ�
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    alien = Alien(ai_settings,screen)
    alien.change_img(ai_settings.aliense[len(ai_settings.aliense)-1].word)
    alien.rect.x = ai_settings.aliense[len(ai_settings.aliense)-1].rect.x 
    alien.rect.y = ai_settings.aliense[len(ai_settings.aliense)-1].rect.y
    
    
    alien.blitme()
    #��ʾ�÷�
    sb.show_score()
    #�����Ϸ���ڷǻ״̬���ͻ���Play��ť
    if not stats.game_active:
        play_button.draw_button()    		
	#��������Ƶ���Ļ�ɼ�
    pygame.display.flip()
    


def update_bullets(ai_settings,screen,stats,sb,ship, aliens, bullets):
    """�����ӵ���λ�ã���ɾ������ʧ���ӵ�"""
    #�����ӵ���λ��
    bullets.update()
    #ɾ������ʧ���ӵ�
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 :
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship, aliens, bullets)
     

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """��Ӧ�ӵ��������˵���ײ"""
    #ɾ��������ײ���ӵ���������
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,False)
    if collisions:
        stats.score += ai_settings.alien_points
        sb.prep_score()
        check_high_score(stats,sb)
        
    
    if len(aliens) == 0 :
		#�����Ⱥ�����˶��������ˣ������һ���ȼ�
        
        bullets.empty()
        ai_settings.increse_speed()
        #��ߵȼ�
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """����ÿ�п����ɶ���������"""
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return 3

def get_number_rows(ai_settings,ship_height,alien_height):
    """������Ļ�����ɶ�����������"""
    available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return 3
    

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """����һ�������˲�������ڵ�ǰ��"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = 2 * alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    ai_settings.aliense.append(alien)
    print(ai_settings.aliense.index(alien))


def create_fleet(ai_settings,screen,ship,aliens):
    """����һ��������Ⱥ"""
    #����һ�������ˣ�������һ�п����ɶ���������
    #�����˼��Ϊ�����˿��
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height, alien.rect.height)
    #����������Ⱥ
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
        
def check_fleet_edges(ai_settings,aliens):
    """�������˵����Եʱ��ȡ��Ӧ�Ĵ�ʩ"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break 

def change_fleet_direction(ai_settings,aliens):
    """���������������ƣ����ı����ǵķ���"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings,stats,screen,ship,sb,aliens,bullets):
    """��Ӧ��������ײ���ķɴ�"""
    if stats.ships_left > 0:
        #��ship_left��һ
        stats.ships_left -= 1
        
        #���¼Ƿ���
        sb.prep_ship()
    
        #��������˶��к��ӵ�����
        aliens.empty()
        bullets.empty()
    
        #����һȺ�����ˣ������ɴ��ŵ���Ļ�׶�����
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
     
        #��ͣ
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    
  
def update_aliens(ai_settings,stats,screen,ship,sb, aliens,bullets):
    """
    ����Ƿ���������λ����Ļ��Ե��������������Ⱥ�����������˵�λ��
    """
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #��������˺ͷɴ�֮�����ײ
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,sb,aliens,bullets)
    
    #����Ƿ��������˵�����Ļ�׶�
    check_aliens_bottom(ai_settings,stats,screen,ship,sb,aliens,bullets)


def check_aliens_bottom(ai_settings,stats,screen,ship,sb,aliens,bullets):
    """����Ƿ��������˵�������Ļ�׶�"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #��ɴ���ײ��һ�����д���
            ship_hit(ai_settings,stats,screen,ship,sb,aliens,bullets)
            break
  
def check_high_score(stats,sb):
    """����Ƿ������µ���ߵ÷�"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()    
  
def Autoshot(ship,ai_settings):
	"""ʵ���Զ�������ܣ��������ӵ���ˮƽ�ٶ�"""
	#�ҵ�Ŀ�������˷ɴ�
	alien = ai_settings.aliense.pop()
	print(alien.word)
	ai_settings.aliense.append(alien)
	#�ó�ˮƽ�ٶ�
	print("ˮƽ������:"+ str(ship.rect.x - alien.rect.x))
	print("��ֱ�����ǣ�"+ str(ship.rect.y - alien.rect.y))
	vv = (ship.rect.x - alien.rect.x) * 10 / (ship.rect.y - alien.rect.y)
	print(str(vv))
	ai_settings.horizontal_v = vv
	
