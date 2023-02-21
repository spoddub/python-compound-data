import math


def make(numer, denom):
    gcd = math.gcd(numer, denom)
    return {
        "numer": int(numer / gcd),
        "denom": int(denom / gcd),
    }


def get_numer(rat):
    return rat["numer"]


def get_denom(rat):
    return rat["denom"]


def add(rat1, rat2):
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 + numer2 * denom1,
        denom1 * denom2,
    )


def sub(rat1, rat2):
    numer1 = get_numer(rat1)
    denom1 = get_denom(rat1)
    numer2 = get_numer(rat2)
    denom2 = get_denom(rat2)

    return make(
        numer1 * denom2 - numer2 * denom1,
        denom1 * denom2,
    )


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"