from hexlet.pairs import car, cdr, cons, to_string as pair_to_string
from hexlet.points import get_x, get_y
from hexlet.points import make as make_point, to_string as point_to_string


# BEGIN (write your solution here)
def make(point1, point2):
    return cons(point1, point2)


def get_begin(segment):
    return car(segment)


def get_end(segment):
    return cdr(segment)


def to_string(segment):
    return f'[{point_to_string(get_begin(segment))}, {point_to_string(get_end(segment))}]'

def middle_point(segment):
    start_point = get_begin(segment)
    end_point = get_end(segment)
    x = (get_x(start_point) + get_x(end_point)) / 2
    y = (get_y(start_point) + get_y(end_point)) / 2

    return make_point(x, y)