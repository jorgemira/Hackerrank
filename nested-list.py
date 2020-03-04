"""
https://www.hackerrank.com/challenges/nested-list/
"""


def second_lowest():
    """Given the names and grades for each student in a Physics class of N students, store them in a nested list and
    print the name(s) of any student(s) having the second lowest grade.

    :rtype: list[str]
    """
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))
    lowest = sorted(set(s for _, s in students))[1]

    return sorted(n for n, s in students if s == lowest)


if __name__ == '__main__':
    print('\n'.join(second_lowest()))
