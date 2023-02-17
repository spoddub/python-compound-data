from hexlet.pairs import car, cdr, cons
from hexlet.points import get_quadrant, get_x, get_y
from hexlet.points import make as make_point


# BEGIN (write your solution here)
def make(point, width, height):
    return cons(point, cons(width, height))


def get_start_point(rectangle):
    return car(rectangle)


def get_height(rectangle):
    return cdr(cdr(rectangle))


def get_width(rectangle):
    return car(cdr(rectangle))


def get_square(rectangle):
    return get_height(rectangle) * get_width(rectangle)


def get_perimeter(rectangle):
    return 2 * (get_height(rectangle) + get_width(rectangle))


def contains_the_origin(rectangle):
    point1 = get_start_point(rectangle)
    x = get_x(point1) + get_width(rectangle)
    y = get_y(point1) - get_height(rectangle)
    point2 = make_point(x, y)

    return get_quadrant(point1) == 2 and get_quadrant(point2) == 4