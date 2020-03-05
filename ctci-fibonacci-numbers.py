"""
https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/
"""


def fibonacci(n):
    """The Fibonacci sequence appears in nature all around us, in the arrangement of seeds in a sunflower and the spiral
    of a nautilus for example.
    The Fibonacci sequence begins with fib(0) = 0 and fib(1) = 1 as its first and second terms. After these first two
    elements, each subsequent element is equal to the sum of the previous two elements.
    Given n, return the nth number in the sequence.

    :type n: int
    :rtype: int
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


n = int(input())
print(fibonacci(n))
