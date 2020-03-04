"""
https://www.hackerrank.com/challenges/reduce-function/
"""

from fractions import Fraction
from functools import reduce
from operator import mul


def product(fracs):
    """Print only one line containing the numerator and denominator of the product of the numbers in the list in its
    simplest form, i.e. numerator and denominator have no common divisor other than 1.

    :type fracs: list[Fraction]
    :rtype: tuple[int, int]
    """
    t = reduce(mul, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
