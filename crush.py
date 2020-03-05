"""
https://www.hackerrank.com/challenges/crush/
"""

import os


def arrayManipulation(n, queries):
    """Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the
    array element between two given indices, inclusive. Once all operations have been performed, return the maximum
    value in your array.

    :type n:int
    :type queries: list[list[int]]
    :rtype: int
    """
    array = [0] * (n + 1)
    result = 0

    s = 0
    for start, end, value in queries:
        array[start - 1] += value
        array[end] -= value

    for i in array:
        s += i
        result = max(result, s)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
