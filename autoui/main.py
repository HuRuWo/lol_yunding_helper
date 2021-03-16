import time
import traceback

import pyautogui


def game_state():
    """
    判断游戏界面属于什么状态
    """
    if pic_exits('pic/游戏未开判断0.png', '未开标志图片0'):
        print('游戏未开状态')
        return 0
    elif pic_exits('pic/游戏中判断1.png', '游戏中图片1'):
        print('云顶游戏中状态')
        return 1
    else:
        print('没找到对应的状态图片')
        return 3


def wait_pic_load(pic_path, tag, max_wait):
    wait_count = 0
    while True:
        if wait_count >= max_wait:
            print("未找到" + tag + "图片坐标")
            return False, None, None
        buttonx, buttony = find_pic(pic_path, tag)
        if buttonx and buttony:
            print("找到" + tag + "图片坐标", buttonx, buttony)
            return True, buttonx, buttony
        else:
            time.sleep(1)
            wait_count += 1


def pic_exits(pic_path, tag):
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(pic_path)
        if buttonx and buttony:
            print("找到" + tag + "图片坐标", buttonx, buttony)
            return True
        else:
            print("寻找" + tag + "图片失败", buttonx, buttony)
            return False
    except Exception as e:
        # print(str(e))
        print("寻找" + tag + "图片失败")
        return False


def find_pic(pic_path, tag):
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(pic_path)
        print("找到" + tag + "图片坐标", buttonx, buttony)
        return buttonx, buttony
    except Exception as e:
        # print(traceback.print_exc())
        print("找到" + tag + "图片失败")
        return None, None


def find_pic_play(pic_path, tag, sleep=3, duration=0.1):
    try:
        buttonx, buttony = find_pic(pic_path, tag)
        if buttonx and buttony:
            pyautogui.click(buttonx, buttony, duration=duration)
            pyautogui.sleep(sleep)
            return True
    except Exception as e:
        # print(traceback.print_exc())
        print(str(e))
        return False


def find_pic_move_to(pic_path, tag, sleep=3):
    try:
        buttonx, buttony = find_pic(pic_path, tag)
        if buttonx and buttony:
            pyautogui.moveTo(buttonx, buttony)
            time.sleep(sleep)
            return True
    except Exception as e:
        # print(traceback.print_exc())
        print(str(e))
        return False


def find_click_pick_lol(pic_path, tag):
    try:
        x, y = find_pic(pic_path, tag)
        if x and y:
            pyautogui.moveTo(x, y)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            return True
        return False
    except Exception as e:
        print(str(e))
        return False


def open_lol_game():
    find_pic_play('pic/再玩一次.png', '再玩一次')
    find_pic_play('pic/首页play.png', '首页play')
    find_pic_play('pic/玩家对战.png', '玩家对战')
    find_pic_play('pic/选择云顶游戏模式.png', '点开进入云顶模式')
    find_pic_play('pic/确认创建对局.png', '创建对局')
    find_pic_move_to('pic/移动鼠标_更改模式.png', '移动鼠标到其他位置')
    if find_pic_play('pic/确认寻找对局.png', '寻找对局') or find_pic_play('pic/确认寻找对局2.png', '寻找对局2'):
        isfind, bx, by = wait_pic_load('pic/接受对局.png', '接受对局', 60)
        if isfind:
            pyautogui.click(bx, by)


def play_game_ing():
    while True:
        find_click_pick_lol('pic/1费卡.png', '1费卡')
        find_click_pick_lol('pic/2费卡.png', '2费卡')
        find_click_pick_lol('pic/刷新牌.png', '刷新牌')
        #find_click_pick_lol('pic/3费卡.png', '3费卡')
        if find_click_pick_lol('pic/游戏结束退出.png', '游戏退出'):
            print('游戏结束')
            break
        time.sleep(3)


if __name__ == '__main__':
    time.sleep(5)


    while True:
        state = game_state()
        if state == 0:
            open_lol_game()
        elif state == 1:
            play_game_ing()
        else:
            pass
        time.sleep(5)
