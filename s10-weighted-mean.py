"""
https://www.hackerrank.com/challenges/s10-weighted-mean/
"""

if __name__ == '__main__':
    n = int(input())
    X = [int(i) for i in input().split()]
    W = [int(i) for i in input().split()]
    print(f"{sum(X[i] * W[i] for i in range(n)) / sum(W):.1f}")
