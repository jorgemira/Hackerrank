"""
https://www.hackerrank.com/challenges/python-division/
"""


def division(a, b):
    """Read two integers and print two lines.
    The first line should contain integer division, a//b.
    The second line should contain float division, a/b.
    You don't need to perform any rounding or formatting operations.

    :type a: int
    :type b: int
    :rtype: tuple[int, int]
    """
    return a // b, a / b


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print('\n'.join(str(i) for i in division(a, b)))
