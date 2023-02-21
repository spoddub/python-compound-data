from hexlet.pairs import car, cdr, cons


def make(numer, denom):
    return cons(numer, denom)


def numer(number):
    return car(number)


def denom(number):
    return cdr(number)


def to_string(number):
    num = numer(number)
    den = denom(number)
    return f'{num} / {den}'


def is_equal(num1, num2):
    a = car(num1)
    b = cdr(num1)
    c = car(num2)
    d = cdr(num2)
    if a * d == c * b:
        return True


def add(num1, num2):
    a = car(num1)
    b = cdr(num1)
    c = car(num2)
    d = cdr(num2)
    num = (a * d + b * c)
    den = (b * d)
    return cons(num, den)


def sub(num1, num2):
    a = car(num1)
    b = cdr(num1)
    c = car(num2)
    d = cdr(num2)
    num = (a * d - b * c)
    den = (b * d)
    return cons(num, den)


def mul(num1, num2):
    a = car(num1)
    b = cdr(num1)
    c = car(num2)
    d = cdr(num2)
    num = (a * c)
    den = (b * d)
    return cons(num, den)


def div(num1, num2):
    a = car(num1)
    b = cdr(num1)
    c = car(num2)
    d = cdr(num2)
    num = (a * d)
    den = (b * c)
    return cons(num, den)
