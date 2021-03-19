#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    score={'max':scores[0],'min':scores[0],'break_max':0,'break_min':0}
    for game in scores:
        if game>score['max']:
            score['max']=game
            score['break_max']+=1
        elif game<score['min']:
            score['min']=game
            score['break_min']+=1
    return( [score['break_max'], score['break_min']])



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
