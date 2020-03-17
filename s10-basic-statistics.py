"""
https://www.hackerrank.com/challenges/s10-basic-statistics/
"""

from statistics import mean, median
from collections import Counter

if __name__ == '__main__':
    _ = input()
    array = [int(i) for i in input().split()]
    print(mean(array))
    print(median(array))
    c = Counter(array)
    m_c = max(c.values())
    print(min(k for k, v in c.items() if v == m_c))
