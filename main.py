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


def find_pic(pic_path):
    location_ = pyautogui.locateOnScreen(pic_path)
    if location_:
        return location_
    else:
        return None


def game_left_click(local):
    # 游戏里面的左键点击判定有问题 需要自己写逻辑
    pyautogui.mouseDown(local, button='left')
    time.sleep(1)
    pyautogui.mouseUp(local, button='left')


def wait_jieshouduiju_click():
    i = 1
    while True:
        if i > 60 * 20:
            break
        print(f'等待接受对局中... 已经等待{i}次')
        home_jieshouduiju_location = find_pic('pic/home_jie_shou_dui_ju.png')
        if home_jieshouduiju_location:
            pyautogui.click(home_jieshouduiju_location)
            time.sleep(5)
            break
        else:
            time.sleep(3)
        i = i + 1


def into_game():
    home_zaiwanyici_location = find_pic('pic/home_zai_wan_yi_ci.png')
    if home_zaiwanyici_location:
        pyautogui.click(home_zaiwanyici_location)
        time.sleep(5)

    home_xunzhaoduiju_location = find_pic('pic/home_xun_zhao_dui_ju.png')
    if home_xunzhaoduiju_location:
        pyautogui.click(home_xunzhaoduiju_location)
        time.sleep(5)
        wait_jieshouduiju_click()


def play_game():
    ## 随便操作 买牌 D卡 不要什么都不做

    location_1 = pyautogui.locateOnScreen('pic/ka/haikesi.png')

    if location_1:
        game_left_click(location_1)

    location_2 = pyautogui.locateOnScreen('pic/ka/gedoujia.png')
    if location_2:
        game_left_click(location_2)

    if location_1 or location_2:
        print('寻找图片成功 点击')
    else:
        location_haikesi = pyautogui.locateOnScreen('pic/game_haikesi.png')
        if location_haikesi:
            print('点击海克斯')
            game_left_click(location_haikesi)

        location_zhuangbei = pyautogui.locateOnScreen('pic/game_zhuangbei.png')
        if location_zhuangbei:
            print('点击装备')
            game_left_click(location_zhuangbei)

        print('寻找图片失败 开D')
        location_d = pyautogui.locateOnScreen('pic/game_d.png')
        if location_d:
            print('DDDDD')
            game_left_click(location_d)

        #time.sleep(3)
        #pyautogui.keyUp('d')

        time.sleep(2)


def exit_game():
    game_exit_location = find_pic('pic/game_exit.png')
    if game_exit_location:
        print('点击左键结束游戏')
        game_left_click(game_exit_location)


## 根据固定的图片判断当前处于什么环境
def game_state():
    game_tag_location_1 = find_pic('pic/game_clock_1.png')
    game_tag_location_2 = find_pic('pic/game_clock_2.png')

    game_tag_location_3 = find_pic('pic/game_clock_3.png')
    game_tag_location_4 = find_pic('pic/game_clock_4.png')

    find_location = None

    if game_tag_location_1:
        find_location = game_tag_location_1
        print('在游戏界面中 game_tag_location_1')
    if game_tag_location_2:
        find_location = game_tag_location_2
        print('在游戏界面中 game_tag_location_2')
    if game_tag_location_3:
        find_location = game_tag_location_3
        print('在游戏界面中 game_tag_location_3')
    if game_tag_location_4:
        find_location = game_tag_location_4
        print('在游戏界面中 game_tag_location_4')

    if find_location:
        pyautogui.rightClick(find_location)
        return 1

    home_tag_location = find_pic('pic/home_we_tag.png')
    if home_tag_location:
        print('在游戏主界面中')
        pyautogui.moveTo(home_tag_location)
        return 3
    return - 1


if __name__ == '__main__':

    print('请先将游戏界面切换到云顶准备进入界面[界面上有寻找对局 选择狂暴模式]')
    print('记得先将游戏分辨率调节为1440x900的窗口化')
    time.sleep(5)
    #
    # print('按下')
    # pyautogui.press('d')
    # pyautogui.keyUp('d')

    while True:
        try:
            state = game_state()
            if state == 1:
                play_game()
                exit_game()
            elif state == 3:
                into_game()
            else:
                print('我不知道我现在在哪我再等等吧')
            time.sleep(3)
        except Exception as e:
            print('异常' + str(e))
