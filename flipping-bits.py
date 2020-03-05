"""
https://www.hackerrank.com/challenges/flipping-bits/
"""

import ctypes
import os


def flippingBits(n):
    """You will be given a list of 32 bit unsigned integers. Flip all the bits (1->0 and 0->1) and print the result as
    an unsigned integer.

    :type n: int
    :rtype: int
    """
    return ctypes.c_uint32(~n).value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
