"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/
"""


def second_maximum(arr):
    """Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
     You are given n scores. Store them in a list and find the score of the runner-up.

    :type arr: list[int]
    :rtype: int
    """
    return sorted(set(arr), reverse=True)[1]


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(second_maximum(arr))
