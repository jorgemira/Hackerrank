"""
https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/

Let's dive into decorators! You are given N mobile numbers. Sort them in ascending order then print them in the standard
format shown below:
    +91 xxxxx xxxxx
The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not
be any prefix at all.
"""


def fix_number(n):
    if len(n) == 12:
        n = f"+{n}"
    elif len(n) == 11:
        n = f"+91{n[1:]}"
    elif len(n) == 10:
        n = f"+91{n}"

    return f"{n[:3]} {n[3:8]} {n[8:13]}"


def wrapper(f):
    def fun(l):
        f([fix_number(n) for n in l])

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
