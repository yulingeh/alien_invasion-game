import os
class Game_status():
    """跟踪统计游戏信息"""
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        #self.reset_status()
        self.game_active = False #让游戏一开始处于停止状态
        self.score = 0
        self.ships_left = self.ai_settings.ship_limit 
        
        #从文件中读取最高分记录
        try:
            with open('highscore.txt','r+')as file_object:
                if not os.path.getsize('highscore.txt'):                           
                    file_object.write("0")  #如果文件存在但没有内容，写入0 
        except FileNotFoundError:           #如果文件不存在，创建一个文件写入0
            with open('highscore.txt','w')as file_object:
                file_object.write("0")
        file_object.close()
        with open('highscore.txt','r')as file_object:       #此时肯定有个有内容的文件，读取数据
            contents = file_object.read()
            self.high_score = int(contents)
        file_object.close()