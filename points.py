import math

from hexlet import points

# В модуле point определены функции:
# points.make(x, y):   создаёт точку
# points.get_x(point): возвращает координату x точки
# points.get_y(point): возвращает координату y точки


# BEGIN (write your solution here)
def get_quadrant(point):
    if points.get_x(point) > 0 and points.get_y(point) > 0:
        return 1
    elif points.get_x(point) > 0 > points.get_y(point):
        return 4
    elif points.get_x(point) < 0 < points.get_y(point):
        return 2
    elif points.get_x(point) < 0 and points.get_y(point) < 0:
        return 3
    else:
        return None


def get_symmetrical_point(point):
    return points.make(-points.get_x(point), -points.get_y(point))


def calculate_distance(point1, point2):
    x1 = points.get_x(point1)
    x2 = points.get_x(point2)
    y1 = points.get_y(point1)
    y2 = points.get_y(point2)
    distance = math.sqrt(((x2 - x1) ** 2) + ((y1 - y2) ** 2))
    return distance
