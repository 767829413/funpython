from oop.tank import *
from oop.bullet import *
from oop.planes import *
from oop.utility import *
from config import *
import pygame


def main():
    tank = Tank()
    planes = Planes()
    bullet = Bullet()

    runnuing = True
    while runnuing:
        Utility.screen.fill(BLACK_COLOR)
        Utility.screen.blit(Utility.background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 游戏结束
                runnuing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tank.update_x_change(-TANK_MOVE_DELTA)
                if event.key == pygame.K_RIGHT:
                    tank.update_x_change(TANK_MOVE_DELTA)
                if event.key == pygame.K_SPACE:
                    bullet.do_ready(
                        Utility.screen, tank.tank_pox_x, tank.tank_pox_y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tank.zero_change()

            tank.update()
            tank.check_boundary()
            over = do_plane_bullet(planes, bullet, tank)
            if over:
                runnuing = False
            bullet.check_boundary()
            bullet.update(Utility.screen)
            tank.draw(Utility.screen)
            Utility.show_core(Utility.text_x, Utility.text_y)
            pygame.display.update()


def do_plane_bullet(planes, bullet, tank) -> bool:
    for i in range(planes.num_of_planes):
        if planes.is_over(i):
            Utility.game_over()
            return True
        planes.update_i(i)
        planes.check_boundary_i(i)
        collision = Utility.is_collision(
            planes.plane_x[i], planes.plane_y[i], bullet.bullet_x, bullet.bullet_y)

        if collision:
            explosion_sound = pygame.mixer.Sound("")
            explosion_sound.play()
            bullet.set_ready()
            bullet.set_pos_by_tank(tank.tank_pos_x, TANK_INIT_POS[1])
            Utility.score_value += 1
            planes.plane_x[i] = random.randint(
                0, WINDOW_WIDTH-planes.plane_img.get_rect().width)
            planes.plane_y[i] = random.randint(
                PLANE_OCCUR_RANGE_Y[0], PLANE_OCCUR_RANGE_Y[1])

        planes.draw_i(Utility.screen, i)

    return False


if __name__ == "__main__":
    main()
