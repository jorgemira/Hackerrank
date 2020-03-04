"""
https://www.hackerrank.com/challenges/write-a-function/
"""


def is_leap(year):
    """You are given the year, and you have to write a function to check if the year is leap or not.
    Note that you have to complete the function and remaining code is given as template.

    :type year: int
    :rtype: bool
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
