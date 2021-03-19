#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count=[ [arr.count(i),i] for i in set(arr)]
    m=max(count)
    for c,i in count:
        if c==m[0]:
            if m[1]>i:
                m[1]=i
    return(m[1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
