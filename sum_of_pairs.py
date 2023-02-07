from hexlet.pairs import car, cdr, cons, is_pair, to_string


# BEGIN (write your solution here)
def sum_of_pairs(pair1, pair2):
    new_car = int(car(pair1)) + int(car(pair2))
    new_cdr = int(cdr(pair1)) + int(cdr(pair2))
    new_pair = cons(new_car, new_cdr)
    return new_pair

# END
