#-*-coding:GBK -*- 

import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """һ���Էɴ�������ӵ����й������"""
    
    def __init__(self,ai_settings,screen,ship):
        """�ڷɴ����ڵ�λ�ô���һ���ӵ�����"""
        super(Bullet,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        
        #�ڣ�0��0)������һ����ʾ�ӵ��ľ��Σ���������ȷ��λ��
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #�洢��С����ʾ���ӵ�λ��
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        #���ô�ֱ�ٶȺ�ˮƽ�ٶ�
        self.speed_factor = ai_settings.bullet_speed_factor
        self.horizontal_v = ai_settings.horizontal_v

    def update(self):
        """�����ƶ��ӵ�"""
        #���±�ʾ�ӵ�λ�õ�С��ֵ
        self.y -= 13
        #���±�ʾ�ӵ���rect��λ��
        self.rect.y = self.y
        self.rect.x += self.horizontal_v
       
    def draw_bullet(self):
        """����Ļ�ϻ����ӵ�"""
        pygame.draw.rect(self.screen,self.color,self.rect)
    def change_speed():
        self.speed = 12
