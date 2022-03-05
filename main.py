import time

import pyautogui


def move_to_18():
    # 移开鼠标 避免放在按钮上导致样式变化找不到
    move_pic('pic/home_18_yun_ding.png')
    time.sleep(3)


def move_pic(pic_path):
    location_ = pyautogui.locateOnScreen(pic_path)
    if location_:
        print(f'find {pic_path} success')
        x, y = pyautogui.center(location_)
        if x and y:
            pyautogui.moveTo(x, y)
            return True


def click_pic(pic_path):
    location_ = pyautogui.locateOnScreen(pic_path)
    if location_:
        print(f'find {pic_path} success')
        x, y = pyautogui.center(location_)
        if x and y:
            pyautogui.click(x, y)
            return True
    else:
        print(f'find {pic_path} fail')
    return False


def into_game():
    pass


def play_game():
    pass


## 根据固定的图片判断当前处于什么环境
def game_state():



if __name__ == '__main__':
    print('请先将游戏界面切换到云顶准备进入界面[界面上有寻找对局]')
    print('记得先将游戏分辨率调节为1440x900的窗口化')
    time.sleep(5)
    while True:
        move_to_18()
        if click_pic('pic/home_xun_zhao_dui_ju.png'):
            time.sleep(5)
            # 等待启动页面 最多等待100s
            i = 0
            while True:
                move_to_18()
                if click_pic('pic/home_jie_shou_dui_ju.png'):
                    print('找到对局 接受对局')
                    break
                if i > 100:
                    print('100s没找到对局 确实有点问题')
                    break
                i = i + 1
        else:
            print('不在等待对局开始界面')
