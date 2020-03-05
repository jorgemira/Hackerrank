"""
https://www.hackerrank.com/challenges/recursive-digit-sum/
"""

import os


def superDigit(n, k):
    """We define super digit of an integer x using the following rules:
    Given an integer, we need to find the super digit of the integer.
    If x has only 1 digit, then its super digit is x.
    Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

    :type n: str
    :type k: int
    :rtype: int
    """
    tmp = str(sum(int(i) for i in n) * k)
    while len(tmp) > 1:
        tmp = str(sum(int(i) for i in tmp))

    return int(tmp)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
