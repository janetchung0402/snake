from typing import List
import pygame as pg
from Config import *
from Model import *
import random


def key_input(pressed_keys: List):
    """
    從 pygame 的鍵盤輸入判斷哪些按鍵被按下
    回傳方向
    """

    for key in pressed_keys:
        if key == pg.K_UP:
            movement = UP
            break
        if key == pg.K_DOWN:
            movement = DOWN
            break
        if key == pg.K_LEFT:
            movement = LEFT
            break
        if key == pg.K_RIGHT:
            movement = RIGHT
            break
        if key == pg.K_a:
            return "new"
    else:
        return None
    return movement


# 以下為大作業


def generate_wall(walls: List[Wall], player: Player, direction: int) -> None:
    """
    生成一個 `Wall` 的物件並加到 `walls` 裡面，不能與現有牆壁或玩家重疊
    新牆壁一定要與現有牆壁有接觸 (第一階段)，更好的話請讓牆壁朝著同個方向生長 (第二階段)
    無回傳值

    Keyword arguments:
    walls -- 牆壁物件的 list
    player -- 玩家物件
    direction -- 蛇的移動方向

    """
    # TODO
    repeat = True
    repeat_again = True
    while repeat == True:
        while repeat_again == True:
            if len(walls) >= 1:
                basic_x = random.randrange(-1, 2, 1)  # 決定新牆壁 x要 +25/-25/+0
                if basic_x == 0: #如果x不動的話 y要 +25/-25
                    basic_y = random.randrange(-1, 3, 2)
                else:
                    basic_y = 0
                x = walls[-1].pos_x+(basic_x * 25)
                y = walls[-1].pos_y+(basic_y * 25)
                if (x > 24*25) or (y > 22*25):
                    repeat_again = True  # 牆壁超過螢幕，repeat_again=True (重新決定y的生長方向)
                else:
                    repeat_again = False
                    new_wall_pos_x = x
                    new_wall_pos_y = y
            else:
                new_wall_pos_x = (random.randint(0, 27) * 25)
                new_wall_pos_y = (random.randint(0, 23) * 25)
                repeat_again = False
        # print(new_wall_pos_x,new_wall_pos_y)
        for block in player.snake_list: #如果與食物重疊
            if block[0] == new_wall_pos_x and block[1] == new_wall_pos_y:
                repeat = True
            else:
                repeat = False
        for brick in walls: #如果與蛇重疊
            if brick.pos_x == new_wall_pos_x and brick.pos_y == new_wall_pos_y:
                repeat = True
            else:
                repeat = False

    new_wall = Wall((new_wall_pos_x, new_wall_pos_y))
    walls.append(new_wall)
    return walls


def generate_food(foods: List[Food], walls: List[Wall], player: Player) -> None:
    """
    在隨機位置生成一個 `Food` 的物件並加到 `foods` 裡面，不能與現有牆壁或玩家重疊
    無回傳值

    Keyword arguments:
    foods -- 食物物件的 list
    walls -- 牆壁物件的 list
    player -- 玩家物件
    """
    # TODO
    repeat = True
    while repeat:
        new_food_pos_x = random.randint(0, 27) * 25
        new_food_pos_y = random.randint(0, 23) * 25
        for block in player.snake_list:  # 如果與蛇重疊
            if block[0] == new_food_pos_x or block[1] == new_food_pos_y:
                repeat = True
            else:
                repeat = False

        for brick in walls:  #如果與牆壁重疊
            if brick.pos_x == new_food_pos_x and brick.pos_y == new_food_pos_y:
                repeat = True
            else:  # 再找新的點
                repeat = False
    new_food = Food((new_food_pos_x, new_food_pos_y))
    foods.append(new_food)
    return


def generate_poison(walls: List[Wall], foods: List[Food], player: Player) -> None:
    """
    在隨機位置生成一個 `Poison` 的物件並回傳，不能與現有其他物件或玩家重疊

    Keyword arguments:
    walls -- 牆壁物件的 list
    foods -- 食物物件的 list
    player -- 玩家物件
    """
    # TODO
    repeat = True
    while repeat:
        new_poison_pos_x = random.randint(0, 27) * 25
        new_poison_pos_y = random.randint(0, 23) * 25
        for block in player.snake_list:  # 如果與蛇重疊
            if block[0] == new_poison_pos_x or block[1] == new_poison_pos_y:
                repeat = True# 再找新的點
            else:
                repeat = False

        for brick in walls: # 如果與牆壁重疊
            if brick.pos_x == new_poison_pos_x or brick.pos_y == new_poison_pos_y:
                repeat = True # 再找新的點
            else:  
                repeat = False
    new_poison = Poison((new_poison_pos_x, new_poison_pos_y))
    return new_poison


def calculate_time_interval(player: Player) -> int:
    """
    根據蛇的長度，計算並回傳每一秒有幾幀
    蛇的長度每增加 4 幀數就 +1，從小到大，最大為 `TIME_INTERVAL_MAX`，最小為 `TIME_INTERVAL_MIN`
    """
    # TODO
    x = len(player.snake_list)//4    # x=蛇的長度除以4，整數除法
    if (TIME_INTERVAL_MIN + x) > TIME_INTERVAL_MAX:
        return TIME_INTERVAL_MAX
    else:
        return (TIME_INTERVAL_MIN + x)
    # return TIME_INTERVAL_MIN
