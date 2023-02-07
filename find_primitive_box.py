from hexlet.pairs import car, cdr, is_pair, to_string


# BEGIN (write your solution here)
def find_primitive_box(pair):
    first = car(pair)
    last = cdr(pair)

    if not is_pair(first) and not is_pair(last):
        return pair

    next_box = first if is_pair(first) else last

    return find_primitive_box(next_box)

# END
