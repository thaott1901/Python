
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colorset = {}
    count = 0
    for i in ar:
        if i in colorset:
            colorset[i] += 1;
        else:
            colorset[i] = 1;
    for sock in colorset.values():
        count += sock // 2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()