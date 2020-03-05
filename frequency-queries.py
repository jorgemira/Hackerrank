"""
https://www.hackerrank.com/challenges/frequency-queries/
"""

import os
from collections import defaultdict


def freqQuery(queries):
    """You are given q queries. Each query is of the form two integers described below:
    -1 x : Insert x in your data structure.
    -2 y : Delete one occurence of y from your data structure, if present.
    -3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

    :type queries: list[list[int]]
    :rtype: list[str]
    """
    items = defaultdict(int)
    freqs = defaultdict(int)
    result = []

    for op, v in queries:
        if op == 1:
            freqs[items[v]] -= 1
            items[v] += 1
            freqs[items[v]] += 1
        elif op == 2:
            if items[v] > 0:
                freqs[items[v]] -= 1
                items[v] -= 1
                freqs[items[v]] += 1
        elif op == 3:
            result.append(1 if freqs[v] else 0)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
