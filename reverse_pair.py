from hexlet.pairs import car, cdr, cons, is_pair, to_string


# BEGIN (write your solution here)
def reverse_pair(pair):
    new_car = cdr(pair)
    new_cdr = car(pair)
    new_pair = cons(new_car, new_cdr)
    return new_pair
# END
