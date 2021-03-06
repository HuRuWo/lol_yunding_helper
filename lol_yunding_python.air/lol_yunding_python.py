# -*- encoding=utf8 -*-
__author__ = "Administrator"

import logging


from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Windows:///",])

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
auto_setup(__file__)

# script content
print("start...")

sleep(5.0)


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


def if_exist_touch(Template,right=False):
    try:
        if exists(Template):
            touch(Template,right_click=right)
            sleep(3.0)
            return True
        
    except Exception as e:
        logger.error('点击失败')
    
    return False
    

    



def open_game():
    
    # 进入云顶 寻找对局
    
    if_exist_touch(Template(r"tpl1615025332165.png", record_pos=(-0.248, -0.011), resolution=(3286, 1080)))
    if_exist_touch(Template(r"tpl1615028314129.png", record_pos=(-0.208, 0.091), resolution=(3286, 1080)))

    if_exist_touch(Template(r"tpl1615025589285.png", record_pos=(-0.244, -0.007), resolution=(3286, 1080)))
    if_exist_touch(Template(r"tpl1615018690154.png", record_pos=(-0.278, 0.075), resolution=(3286, 1080)))
    if_exist_touch(Template(r"tpl1615015496872.png", record_pos=(-0.409, -0.12), resolution=(3286, 1080)))
    
    if_exist_touch(Template(r"tpl1615025712630.png", record_pos=(-0.38, -0.086), resolution=(3286, 1080)))

    if_exist_touch(Template(r"tpl1615015901366.png", record_pos=(-0.311, -0.074), resolution=(3286, 1080)))
    if_exist_touch(Template(r"tpl1615015931324.png", record_pos=(-0.338, 0.07), resolution=(3286, 1080)))
    find = if_exist_touch(Template(r"tpl1615016023287.png", record_pos=(-0.337, 0.067), resolution=(3286, 1080)))
    
    if find:
        # 等待对局 如果出现 直接点击
        try:
             touch(wait(Template(r"tpl1615019468524.png", record_pos=(-0.25, 0.036), resolution=(3286, 1080))),timeout=30)
        except Exception as e:
            logger.error('等待开始失败')
        
      
    
def play_game():
    """
    进入游戏开始 游戏策略 只买斗士 
    """
    
    # 八总斗士图片 
    

    while True:
        
        # 通过图片判断自己在什么界面
        
        
        if exists(Template(r"tpl1615024590336.png", record_pos=(-0.336, 0.105), resolution=(3286, 1080))):

            

            logger.error('D牌界面')  

            if_exist_touch(Template(r"tpl1615026460737.png", record_pos=(-0.189, -0.068), resolution=(3286, 1080)),True)
            #if_exist_touch(Template(r"tpl1615024590336.png", record_pos=(-0.336, 0.105), resolution=(3286, 1080)))
            if_exist_touch(Template(r"tpl1615025077008.png", record_pos=(-0.101, 0.109), resolution=(3286, 1080)))
       
        elif exists(Template(r"tpl1615028039378.png", record_pos=(-0.21, 0.095), resolution=(3286, 1080))):
            
            
            logger.error('选人界面')  
            
        
        elif exists(Template(r"tpl1615017452243.png", record_pos=(-0.3, 0.004), resolution=(3286, 1080))):
            

            logger.error('游戏结束了')
            
            ## 点退出 再玩一次
            
            touch(Template(r"tpl1615017452243.png", record_pos=(-0.3, 0.004), resolution=(3286, 1080)))

            
            break # 算是完成一盘周期
        else:
            logger.error('不明界面')
            
        sleep(4.0)


while True:
    
    # 判断进入哪个分支
    #     open_game()
    sleep(4.0)
    
    if exists(Template(r"tpl1615023706547.png", record_pos=(-0.072, -0.104), resolution=(3286, 1080))):
        
        logger.error('开始新建游戏') 
        
        open_game()

    elif exists(Template(r"tpl1615022397690.png", record_pos=(-0.057, -0.088), resolution=(3286, 1080))):
        
        logger.error('开始新建游戏') 
        
        play_game()
        
    else:
        logger.error('不明的界面')
        
        if_exist_touch(Template(r"tpl1615028314129.png", record_pos=(-0.208, 0.091), resolution=(3286, 1080)))
                 



    




    



