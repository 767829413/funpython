import pygame
import random
from config import *

class Planes:
    def __init__(self):
        """
        飞机初始化相关方法
        """
        self.plane_imgs = []
        self.plane_x = []
        self.plane_y = []
        self.plane_x_change = []
        self.plane_y_change = []
        self.num_of_planes = 6

        self.__create_planes()

    def __create_planes(self):
        for i in range(self.num_of_planes):
            self.plane_img = pygame.image.load("")
            self.plane_imgs.append(self.plane_img)
            self.plane_x.append(random.randint(
                0, WINDOW_WIDTH - self.plane_img.get_rect().width))
            self.plane_y.append(random.randint(
                WINDOW_HEIGHT // 12, WINDOW_HEIGHT//12))
            self.plane_x_change.append(PLANE_MOVE_DELTA[0])
            self.plane_y_change.append(PLANE_MOVE_DELTA[1])

    def draw_i(self, screen, i):
        """
        绘制第 i 个飞机
        :param screen: 游戏屏幕
        :param i:
        :return:
        """
        screen.blit(self.plane_imgs[i], (self.plane_x[i], self.plane_y[i]))

    def update_i(self, i):
        self.plane_x[i] += self.plane_x_change[i]

    def check_boundary_i(self, i):
        if self.plane_x[i] <= 0:
            self.plane_x_change[i] = PLANE_MOVE_DELTA[0]
            self.plane_y[i] += self.plane_y_change[i]
        elif self.plane_x[i] >= WINDOW_WIDTH - self.plane_img[i].get_rect().width:
            self.plane_x_change[i] = PLANE_MOVE_DELTA[0]
            self.plane_y[i] += self.plane_y_change[i]

    def is_over(self, i):
        if self.plane_y[i] > PLANE_GOAL_POS_Y:
            self.plane_y = [2000 for _ in range(self.num_of_planes)]
            return True
        return False
