from typing import List
from Config import *
import pygame as pg


class Food:
    """
    食物物件，初始化方法為 `Food((左上角 x, 左上角 y))`
    `self.pos_x` 及 `self.pos_y` 為食物的座標
    """

    def __init__(self, pos):
        # self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        # self.surf.fill(FOOD_COLOR)
        # self.rect = self.surf.get_rect(topleft=pos)

        self.cake = pg.image.load("template/image/cake.jpg").convert_alpha()
        self.cake = pg.transform.scale(self.cake, (25, 25))
        self.rect = self.cake.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]


class Poison:
    """
    毒藥物件，初始化方法為 `Poison((左上角 x, 左上角 y))`
    `self.pos_x` 及 `self.pos_y` 為毒藥的座標
    """

    def __init__(self, pos):
        # self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        # self.surf.fill(POISON_COLOR)
        # self.rect = self.surf.get_rect(topleft=pos)

        self.image = pg.image.load("template/image/樹莓.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]


class Wall:

    """
    牆壁物件，初始化方法為 `Wall((左上角 x, 左上角 y))`
    `self.pos_x` 及 `self.pos_y` 為牆壁的座標
    """

    def __init__(self, pos):
        #     self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        #     self.surf.fill(WALL_COLOR)
        #     self.rect = self.surf.get_rect(topleft=pos)

        self.brick = pg.image.load("template/image/brick2.jpg").convert_alpha()
        self.brick = pg.transform.scale(self.brick, (25, 25))
        self.rect = self.brick.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]


class Player:
    """
    玩家物件
    `self.snake_list` 紀錄每一段蛇的資訊 `(左上 x, 左上 y, 寬, 高)`
    `self.head_x` 及 `self.head_y` 為蛇頭的座標
    `self.length` 為蛇的長度
    """

    def __init__(self):
        self.snake_list = [[200, 100, SNAKE_SIZE, SNAKE_SIZE]]

    @property
    def head_x(self):
        return self.snake_list[0][0]

    @property
    def head_y(self):
        return self.snake_list[0][1]

    @property
    def length(self):
        return len(self.snake_list)

    # 以下為大作業

    def new_block(self, new_pos) -> None:
        """
        將新一節蛇身的資訊加到 `snake_list` 最後面，無回傳值

        Keyword arguments:
        new_pos -- 新一節蛇身的座標 (左上 x, 左上 y)
        """
        # TODO
        new_pos = [self.snake_list[-1][0]+25, self.snake_list[-1][1]]
        self.snake_list.append(
            [new_pos[0], new_pos[1], SNAKE_SIZE, SNAKE_SIZE])
        #print("self.snake_list", self.snake_list)
        pass

    def draw_snake(self, screen) -> None:
        """
        畫出蛇，顏色要黃藍相間，無回傳值
        顏色可以用 `SNAKE_COLOR_YELLOW` 及 `SNAKE_COLOR_BLUE`
        可以用 `pg.draw.rect(screen 物件, 顏色, (座標 x, 座標 y, 寬, 高))`

        Keyword arguments:
        screen -- pygame 螢幕物件
        """
        # TODO
        if len(self.snake_list) > 0:
            block = self.snake_list[0]
        pg.draw.rect(screen, SNAKE_COLOR_HEAD, block)
        for i in range(1, len(self.snake_list)):
            if i % 2 == 0:
                block = self.snake_list[i]
                pg.draw.rect(screen, SNAKE_COLOR_YELLOW, block)
            else:
                block = self.snake_list[i]
                pg.draw.rect(screen, SNAKE_COLOR_BLUE, block)
        pass

    def check_border(self) -> bool:
        """
        判斷蛇的頭有沒有超出螢幕範圍
        有超出就回傳 `True`
        沒有超出回傳 `False`

        Return:
        bool -- 蛇的頭有沒有超出螢幕範圍
        """
        # TODO #accomplish
        for block in self.snake_list:
            # print("block",block[0],block[1])
            if 0 <= block[0] <= 675 and 0 <= block[1] <= 575:
                return False
            else:
                return True

        return False

    def move(self, direction) -> None:
        """
        根據 `direction` 移動蛇的座標，無回傳值，`direction` 為哪個按鍵被按到
        -1: 其他
        0: 上
        1: 右
        2: 下
        3: 左
        方向的代號也可以直接使用 `UP`, `RIGHT`, `DOWN`, `LEFT`，在 `Config.py` 裡面定義好了
        (左上 x, 左上 y, 寬, 高)`
        Keyword arguments:
        direction -- 蛇的移動方向
        """
        # TODO
        if direction == UP:  # 上   #把頭複製起來且x座標+25，把尾巴pop掉，再把頭放回去
            head = self.snake_list[0].copy()
            self.snake_list.insert(
                0, [head[0], head[1]-25, SNAKE_SIZE, SNAKE_SIZE])
            self.snake_list.pop()

        if direction == RIGHT:  # 右
            head = self.snake_list[0].copy()
            self.snake_list.insert(
                0, [head[0]+25, head[1], SNAKE_SIZE, SNAKE_SIZE])
            self.snake_list.pop()

        if direction == DOWN:  # 下
            head = self.snake_list[0].copy()
            self.snake_list.insert(
                0, [head[0], head[1]+25, SNAKE_SIZE, SNAKE_SIZE])
            self.snake_list.pop()

        if direction == LEFT:  # 左
            head = self.snake_list[0].copy()
            self.snake_list.insert(
                0, [head[0]-25, head[1], SNAKE_SIZE, SNAKE_SIZE])
            self.snake_list.pop()

        pass

    def detect_player_collision(self) -> bool:
        """
        判斷蛇的頭是否碰到蛇的其他段
        有碰到就回傳 `True`
        沒有碰到回傳 `False`

        Return:
        bool -- 是否碰到蛇 (自己) 的其他段
        """
        # TODO
        head = self.snake_list[0]  # 蛇頭
        for i in range(1, len(self.snake_list), 1):
            block = self.snake_list[i]
            if head[0] == block[0]:
                if head[1] == block[1]:
                    return True
        return False

    def detect_wall_collision(self, walls: List[Wall]) -> bool:
        """
        判斷蛇的頭是否碰到牆壁
        有碰到就回傳 `True`
        沒有碰到回傳 `False`

        Keyword arguments:
        walls -- 牆壁物件的 list

        Return:
        bool -- 是否碰到牆壁
        牆壁物件，初始化方法為 `Wall((左上角 x, 左上角 y))`
        """
        # TODO
        head = self.snake_list[0]  # 舌頭
        for brick in walls:
            # print("brick", brick.pos_x, brick.pos_y)
            if head[0] == brick.pos_x:
                if head[1] == brick.pos_y:
                    return True
        return False

    def detect_food_collision(self, foods: List[Food]) -> bool:
        """
        判斷蛇的頭是否碰到食物
        有碰到就回傳 `True`
        沒有碰到回傳 `False`

        Keyword arguments:
        foods -- 食物物件的 list

        Return:
        bool -- 是否碰到食物
        """
        # TODO
        head = self.snake_list[0]  # 舌頭
        # print("food", foods[0].pos_x, foods[0].pos_y)
        for piece in foods:
            if head[0] == piece.pos_x:
                if head[1] == piece.pos_y:
                    return True
        return False

    def detect_poison_collision(self, poison: Poison) -> bool:
        """
        判斷蛇的頭是否碰到毒藥
        有碰到就回傳 `True`
        沒有碰到回傳 `False`

        Keyword arguments:
        poison -- 毒藥物件

        Return:
        bool -- 是否碰到毒藥
        """
        # TODO
        # print("poison", poison.pos_x, poison.pos_x)
        head = self.snake_list[0]
        if head[0] == poison.pos_x:
            if head[1] == poison.pos_y:
                return True
        return False
