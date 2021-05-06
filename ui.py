from bll import GameCoreController
from model import Direction
import copy
import os


class GameView:
    """
        界面视图类
    """
    def __init__(self):
        self.__controller = GameCoreController()

    def __print_map(self):
        """
            显示二维列表
        :return:
        """
        # os.system("clear")
        for r in range(len(self.__controller.map)):
            for c in range(len(self.__controller.map[r])):
                print(self.__controller.map[r][c], end="\t")
            print()
            print()

    def __move_map(self):
        """
            移动二维列表
        :return:
        """
        direction = input("请输入移动方向（提示：wasd）：")
        if direction == "w":
            self.__controller.move(Direction.up)
        if direction == "s":
            self.__controller.move(Direction.down)
        if direction == "a":
            self.__controller.move(Direction.left)
        if direction == "d":
            self.__controller.move(Direction.right)

    def start(self):
        """
            开始游戏，随机生成两个新数字，打印二维列表
        :return:
        """
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__print_map()

    def update(self):
        """
            更新地图,判定游戏是否结束
        :return:
        """
        while True:
            self.__move_map()
            if self.__controller.is_change:
                self.__controller.generate_new_number()
                self.__print_map()
            if self.__controller.is_game_over():
                print("游戏结束")
                break





