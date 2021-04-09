import random
import math


def cnt_can_paint_wall(height, width):
    area_can_coverage = 5.0
    return math.ceil(height * width / area_can_coverage)


if __name__ == "__main__":
    y = random.randint(1, 10)
    x = random.randint(1, 20)

    print(f'You are painting a wall\n1 can of paint can cover 5 square meters of wall')
    print(f'Height: {x}, Width: {y} --> Area: {x*y}')

    print(f'You need {cnt_can_paint_wall(height=y, width=x)} at least for painting a wall')
