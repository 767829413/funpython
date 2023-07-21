import pygame
from config import *


class Tank:
    def __init__(self):
        """
        构造函数: 坦克初始化
        """
        self.tank_img = pygame.image.load("")
        self.tank_pos_x, self.tank_pos_y = TANK_INIT_POS
        self.tank_x_change = 0

    def draw(self, screen):
        """
        绘制坦克
        :param screen: 游戏屏幕对象
        :return:
        """
        screen.blit(self.tank_img, (self.tank_pos_x, self.tank_pos_y))

    def update(self):
        """
        更新坦克位置
        :retur:
        """
        self.tank_pos_x += self.tank_x_change

    def update_x_change(self, x_delta):
        """
        更新坦克移动增量
        :param x_delta:
        :return:
        """
        self.tank_x_change += x_delta

    def check_boundary(self):
        """
        检查坦克边界位置
        :return:
        """
        if self.tank_pos_x <= 0:
            self.tank_pos_x = 0
        elif self.tank_pos_x >= WINDOW_WIDTH - self.tank_img.get_rect().width:
            self.tank_pos_x = WINDOW_WIDTH - self.tank_img.get_rect().width

    def zero_change(self):
        self.tank_x_change = 0
