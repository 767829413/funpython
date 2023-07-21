import pygame
import math
from config import *


class Utility:
    pygame.init()

    score_value = 0
    font = pygame.font.Font(None, 32)
    text_x = 10
    text_y = 10
    over_font = pygame.font.Font(None, 64)

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("坦克飞机大战")
    icon = pygame.image.load("")
    pygame.display.set_icon(icon)
    background = pygame.image.load("")
    pygame.mixer.music.load("")
    pygame.mixer.music.play(-1)

    @classmethod
    def show_core(cls, x, y):
        """
        展示游戏分数
        :param x: 分数显示位置 x
        :param y:
        :return:
        """
        score = cls.font.render(
            f"Score : {cls.score_value}", True, BLACK_COLOR, cls.background)
        cls.screen.blit(score, (x, y))

    @classmethod
    def game_over(cls):
        """
        展示游戏结束画面
        :return:
        """
        over_text = cls.font.render(
            "GAME OVER", True, (255, 255, 255), cls.background)
        cls.screen.blit(over_text, (200, 250))

    @staticmethod
    def is_collision(enemy_x, enemy_y, bullet_x, bullet_y) -> bool:
        """
        判断enemy和bullet是否碰撞,计算两者距离
        :param enemy_x: 敌人位置x
        :param enemy_y:
        :param bullet_x: 子弹位置x 
        :param bullet_y:
        :return: Boolean 
        """
        distance = math.sqrt(
            math.pow(enemy_x - bullet_x, 2)+math.pow(enemy_y - bullet_y, 2))
        
        return distance < COLL_DIST_PLANE_BULLET
