"""
https://www.hackerrank.com/challenges/python-division/
"""


def loops(n):
    """Read an integer N. For all non-negative integers i<N, print i^2 . See the sample for details.
    :type n: int
    :rtype: list[int]
    """
    return [i**2 for i in range(0, n)]


if __name__ == '__main__':
    n = int(input())

    print('\n'.join(str(i) for i in loops(n)))
