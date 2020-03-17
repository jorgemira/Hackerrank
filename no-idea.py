"""
https://www.hackerrank.com/challenges/no-idea/
"""


def happiness(array, A, B):
    """There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like
    all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each integer i in
    the array A, if i in A, you add 1 to your happiness. If i in B, you add -1 to your happiness. Otherwise, your
    happiness does not change. Output your final happiness at the end.

    :type array: list
    :type A: set
    :type B: set
    :rtype: int
    """
    return sum(a in A for a in array) - sum(a in B for a in array)


if __name__ == '__main__':
    _ = input()
    array = input().split()
    A = set(input().split())
    B = set(input().split())
    print(happiness(array, A, B))
