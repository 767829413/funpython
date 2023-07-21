# 游戏的宽高
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
# 坦克的初始位置
TANK_INIT_POS = [370, 480]
# 坦克每次移动量(只在x方向移动)
TANK_MOVE_DELTA = 5
# 飞机每次移动量(x方向 3 像素, y方向 10 像素)
PLANE_MOVE_DELTA = (3, 10)
# 飞机和坦克的边界线(飞机越过就胜利)
PLANE_GOAL_POS_Y = 440
# 初始飞机出现的Y向区域
PLANE_OCCUR_RANGE_Y = (50, 150)
# 飞机与子弹距离27像素认为已发生碰撞
COLL_DIST_PLANE_BULLET = 27
# 坦克发射子弹时与坦克的相对位置 (x, y)
BULLET_FIRE_RELA_TANK = (16, 10)
# 黑色
BLACK_COLOR = (0, 0, 0)
