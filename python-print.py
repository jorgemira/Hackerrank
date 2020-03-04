"""
https://www.hackerrank.com/challenges/python-print/
"""


def print_to_n(n):
    """Read an integer n.
    Without using any string methods, try to print the following:
        123..N
    Note that "..." represents the values in between.
    :type n: int
    :rtype: str
    """
    return ''.join(str(i) for i in range(1, n + 1))


if __name__ == '__main__':
    n = int(input())
    print(print_to_n(n))
