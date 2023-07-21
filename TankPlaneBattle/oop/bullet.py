import pygame
from config import *


class Bullet:
    def __init__(self):
        """
        子弹初始化相关
        """
        self.bullet_img = pygame.image.load("")
        self.bullet_x = 0
        self.bullet_y = TANK_INIT_POS[1]

        self.bullet_y_change = 10
        self.bullet_state = "ready"

    def set_pos_by_tank(self, x, y):
        self.bullet_x = x + BULLET_FIRE_RELA_TANK[0]
        self.bullet_y = y + BULLET_FIRE_RELA_TANK[1]

    def draw_bullet(self, screen):
        """
        设置位置绘制子弹
        :param screen: 游戏屏幕
        :return:
        """
        screen.blit(self.bullet_img, (self.bullet_x, self.bullet_y))

    def set_fire(self):
        self.bullet_state = "fire"

    def set_ready(self):
        self.bullet_state = "ready"

    def draw_fire(self, screen):
        self.set_fire()
        self.draw_bullet(screen)

    def check_boundary(self):
        if self.bullet_y <= 0:
            self.bullet_y = TANK_INIT_POS[1]
            self.bullet_state = "ready"

    def update(self, screen):
        if self.bullet_state == "fire":
            self.draw_fire(screen)
            self.bullet_y -= self.bullet_y_change

    def do_ready(self, screen, x, y):
        if self.bullet_state == "ready":
            self.set_pos_by_tank(x, y)
            pygame.mixer.Sound("").play()
            self.draw_fire(screen)
