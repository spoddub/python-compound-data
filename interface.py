import math


def make_point(x: int, y: int) -> dict:
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


def get_x(point: dict) -> int:
    return int(point["radius"] * math.cos(point["angle"]))


def get_y(point: dict) -> int:
    return int(point["radius"] * math.sin(point["angle"]))
