class Settings():
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1080
        self.screen_height = 720
        self.bg_color = (230,230,230)

        #子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.num_big = 3
        #外星人设置
        self.alien_speed = 1
        self.alien_points = 20
        #飞船设置
        self.ship_speed = 2
        self.ship_limit = 3