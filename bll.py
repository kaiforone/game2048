import random
from random import choice
from model import Location,Direction
import copy


class GameCoreController:
    """
        游戏核心控制器
    """

    def __init__(self):
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_location = []
        self.__is_change = False

    @property
    def map(self):
        return self.__map

    @property
    def list_location(self):
        return self.__list_location

    @property
    def is_change(self):
        return self.__is_change


    def __zero_to_end(self,list_target):
        for i in range(len(list_target) - 1, -1, -1):
            if list_target[i] == 0:
                del list_target[i]
                list_target.append(0)

    def __merge(self,list_target):
        self.__zero_to_end(list_target)
        for i in range(0, len(list_target) - 1):
            if list_target[i] == list_target[i + 1]:
                list_target[i], list_target[i + 1] = list_target[i] * 2, 0
        self.__zero_to_end(list_target)

    def __move_left(self):
        for r in range(len(self.__map)):
            self.__merge(self.__map[r])

    def __move_right(self):
        for r in range(len(self.__map)):
            list_merge = self.__map[r][::-1]
            self.__merge(list_merge)
            self.__map[r][::-1] = list_merge

    def __move_down(self):
        for c in range(len(self.__map[0])):
            list_merge = []
            for r in range(len(self.__map) - 1, -1, -1):
                list_merge.append(self.__map[r][c])
            self.__merge(list_merge)
            for i in range(len(list_merge)):
                self.__map[i][c] = list_merge[len(list_merge) - 1 - i]

    def __move_up(self):
        for c in range(len(self.__map[0])):
            list_merge = []
            for r in range(len(self.__map)):
                list_merge.append(self.__map[r][c])
            self.__merge(list_merge)
            for i in range(len(list_merge)):
                self.__map[i][c] = list_merge[i]

    def move(self,dir):
        """
            根据传递的参数判断方向，调用具体的方法移动二维列表
        :param dir: 方向
                    Direction类对象数据类型
        :return:
        """
        list_original = copy.deepcopy(self.__map)
        if dir == Direction.up:
            self.__move_up()
        if dir == Direction.down:
            self.__move_down()
        if dir == Direction.left:
            self.__move_left()
        if dir == Direction.right:
            self.__move_right()
        self.__is_change = list_original != self.__map

    def __find_zero_loc(self):
        self.list_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0 :
                    loc = Location(r,c)
                    self.list_location.append(loc)

    def generate_new_number(self):
        """
            在空白位置随机生成一个新数字
        :return:
        """
        self.__find_zero_loc()
        if len(self.list_location) == 0:
            return
        location = choice(self.list_location)
        self.__map[location.r_index][location.c_index] = 4 if random.randint(1, 10) == 1 else 2
        self.list_location.remove(location)

    def is_game_over(self):
        """
            判定游戏是否结束
        :return: True/False
        """
        if self.list_location == [] and not self.__is_change :
            return True
        return False


