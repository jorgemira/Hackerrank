"""
https://www.hackerrank.com/challenges/python-time-delta
"""

import datetime
import os


def parse_date(dt):
    result = datetime.datetime.strptime(dt[:-6], '%a %d %b %Y %H:%M:%S')
    tz = datetime.timedelta(hours=int(dt[-4:-2]), minutes=int(dt[-2:])) * (1 if dt[-5] == '-' else -1)
    return result + tz


# Complete the time_delta function below.
def time_delta(t1, t2):
    """When users post an update on social media,such as a URL, image, status update etc., other users in their network
    are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e,
    how many hours, minutes or seconds ago.
    Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two
    timestamps of one such post that a user can see on his newsfeed in the following format:
        Day dd Mon yyyy hh:mm:ss +xxxx
    Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

    :type t1: str
    :type t2: str
    :rtype: str
    """
    dt1 = parse_date(t1)
    dt2 = parse_date(t2)
    return str(abs(int((dt1 - dt2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
