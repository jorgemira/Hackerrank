"""
https://www.hackerrank.com/challenges/ctci-big-o/
"""

import os
from math import sqrt

PRIME = 'Prime'
NOT_PRIME = 'Not prime'


def primality(n):
    """A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given p
    integers, determine the primality of each integer and print whether it is Prime or Not prime on a new line.

    :type n: int
    :rtype: str
    """
    if n == 1:
        return NOT_PRIME
    return PRIME if all(n % i for i in range(2, int(sqrt(n)) + 1)) else NOT_PRIME


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
