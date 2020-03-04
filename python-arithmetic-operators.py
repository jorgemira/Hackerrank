"""
https://www.hackerrank.com/challenges/python-arithmetic-operators/
"""


def arithmetic_operators(a, b):
    """Read two integers from STDIN and print three lines where:

    The first line contains the sum of the two numbers.
    The second line contains the difference of the two numbers (first - second).
    The third line contains the product of the two numbers.
    :type a: int
    :type b: int
    :rtype: tuple[int, int, int]
    """
    return a + b, a - b, a * b


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print('\n'.join(str(i) for i in arithmetic_operators(a, b)))
