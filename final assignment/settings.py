#-*-coding:GBK -*- 


class Settings():
    """�洢�����������֡����������õ���"""
    
    def __init__(self):
        """��ʼ����Ϸ�ľ�̬����"""
        
        
        #��Ļ����
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color=(230,230,230)
        #�ɴ�������
        self.ship_speed_factor = 4
        self.ship_limit = 3
        #�ӵ�����
        self.bullet_speed_factor = 10
        self.horizontal_v = 0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10
        #����������
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 8
        #Ūһ����������˵�list
        self.aliense = []
        
        #fleet_directionΪ1��ʾ���ƣ�Ϊ-1��ʾ����
        self.fleet_direction = 1
        #��ʾ����Ļ�ϵĴ���
        #��ʾ����Ļ�ϵĴ���
        self.vocabulary = ['simple','hard','test','reliance','gleam','enforce','accuse',
              'sergeant','rating','hinge','cite','advocate','formidable',
              'gloom','shed','beyond','virtue','bizarre','draft','coupon','king','white','was','and','perception','lunch','some','they',
              'until','food','low','school','year','student','to','have','deprives','also']

        #��ʲô�����ٶȼӿ���Ϸ����
        self.speedup_scale = 1
        
        self.initialize_dynamic_settings()
        #�����˵���������ٶ�
        self.score_scale = 1.5
        
        #�Ƿ�
        self.alien_points = 50
        self.flag = False
        self.alien_word = ''
        


    def initialize_dynamic_settings(self):
        """��ʼ������Ϸ���ж��仯������"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        #fleet_directionΪ1��ʾ���ң�Ϊ-1��ʾ����
        self.fleet_direction = 1

    def increse_speed(self):
        """����ٶ����ú������˵���"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        
        
        
