#-*-coding:GBK -*- 

import pygame
import random

from pygame.sprite import Sprite

class Alien(Sprite):
    """��ʾ���������˵���"""
    
    def __init__(self,ai_settings,screen):
        """��ʼ�������˲��������ʼλ��"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #����������ͼ�񣬲�������rect����
        self.image = pygame.image.load('images/alien0.png')
        #������ͼƬ�����ڣ�ֱ�����ɵ���
        #�洢�����˵ĵ���
        self.word = self.ai_settings.vocabulary[random.randint(0,19)]
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        self.image = self.font.render(self.word,True,self.text_color,self.ai_settings.bg_color)
        self.rect = self.image.get_rect()
        self.rect.height = 60
        self.rect.width = 120
        
        #ÿ�����������������Ļ�����ϽǸ���
        self.rect.x  = self.rect.width
        self.rect.y  = self.rect.height
        
        #�洢�����˵�׼ȷλ��
        self.x = float(self.rect.x)
        
    def blitme(self):
        """��ָ����λ�û���������"""
        self.screen.blit(self.image,self.rect)    

    def check_edges(self):
        """���������λ����Ļ��Ե���ͷ���True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """������������ƶ�������"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
