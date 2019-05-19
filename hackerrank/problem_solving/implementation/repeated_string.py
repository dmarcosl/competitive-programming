import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) > n:
        return len(re.sub(r'[^a]', '', s[:n]))

    e = int(n / len(s))
    c = e * len(re.sub(r'[^a]', '', s))

    if n % len(s) != 0:
        for i in s[: n - e*(len(s))]:
            if i == 'a':
                c += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
