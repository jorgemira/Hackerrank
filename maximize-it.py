"""
https://www.hackerrank.com/challenges/maximize-it/
"""


def maximize_it(elements, m, count=0):
    """You are given a function f(x) = X^2. You are also given K lists. The i^th list consists of Ni elements.
    You have to pick one element from each list so that the value from the equation below is maximized:
    S = (f(X1) + f(X2) + ... f(Xn)) % M
    Xi denotes the element picked from the i^th list. Find the maximized value Smax obtained.
    % denotes the modulo operator.
    Note that you need to take exactly one element from each list, not necessarily the largest element. You add the
    squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the
    answer to the problem.

    :type elements: list[set[int]]
    :type m: int
    :type count: int
    :rtype: int
    """
    if not elements:
        return count % m
    else:
        return max(maximize_it(elements[1:], m, count + i) for i in elements[0])


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    elements = []
    for _ in range(n):
        line = input()
        elements.append(set(int(i) ** 2 for i in line.split()[:1]))

print(maximize_it(elements, m))
