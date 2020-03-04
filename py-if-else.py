"""
https://www.hackerrank.com/challenges/py-if-else/
"""

WEIRD = 'Weird'
NOT_WEIRD = 'Not Weird'


def is_weird(n):
    """Given an integer, perform the following conditional actions:
    If n is odd, print Weird
    If n is even and in the inclusive range of 2 to 5, print Not Weird
    If n is even and in the inclusive range of 6 to 20, print Weird
    If n is even and greater than 20, print Not Weird
    :param n: The number
    :type n: int
    :return: Weird/Not weird
    :rtype str:
    """
    if n % 2:
        return WEIRD
    elif 2 <= n <= 5:
        return NOT_WEIRD
    elif 6 <= n <= 20:
        return WEIRD
    else:
        return NOT_WEIRD


if __name__ == '__main__':
    n = int(input().strip())
    print(is_weird(n))
