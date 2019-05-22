import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    lvl = 0
    valleys = 0
    down = False

    for i in s:
        if i == 'D':
            lvl -= 1
        else:
            lvl += 1

        if lvl < 0 and not down:
            down = True
            valleys += 1
        elif lvl >= 0:
            down = False
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
