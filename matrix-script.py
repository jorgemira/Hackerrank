"""
https://www.hackerrank.com/challenges/matrix-script/
"""
import re


def matrix_script(matrix):
    """Neo has a complex matrix script. The matrix script is a NxM grid of strings. It consists of alphanumeric
    characters, spaces and symbols (!,@,#,$,%,&).
    To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them.
    Neo reads the column from top to bottom and starts reading from the leftmost column.
    If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them
    with a single space '' for better readability.
    Neo feels that there is no need to use 'if' conditions for decoding.
    Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

    :type matrix: list[str]
    :rtype: str
    """
    txt = ''.join(matrix[j][i] for i in range(len(matrix[0])) for j in range(len(matrix)))
    return re.sub(r'(\w)\W+(\w)', r'\1 \2', txt)


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print(matrix_script(matrix))
