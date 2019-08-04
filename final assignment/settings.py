#-*-coding:GBK -*- 


class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的静态设置"""
        
        
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color=(230,230,230)
        #飞船的设置
        self.ship_speed_factor = 4
        self.ship_limit = 3
        #子弹设置
        self.bullet_speed_factor = 10
        self.horizontal_v = 0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 8
        #弄一个存放外星人的list
        self.aliense = []
        
        #fleet_direction为1表示右移，为-1表示左移
        self.fleet_direction = 1
        #显示在屏幕上的词语
        #显示在屏幕上的词语
        self.vocabulary = ['simple','hard','test','reliance','gleam','enforce','accuse',
              'sergeant','rating','hinge','cite','advocate','formidable',
              'gloom','shed','beyond','virtue','bizarre','draft','coupon','king','white','was','and','perception','lunch','some','they',
              'until','food','low','school','year','student','to','have','deprives','also']

        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1
        
        self.initialize_dynamic_settings()
        #外星人点数的提高速度
        self.score_scale = 1.5
        
        #记分
        self.alien_points = 50
        self.flag = False
        self.alien_word = ''
        


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        #fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

    def increse_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        
        
        
