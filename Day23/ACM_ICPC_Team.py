#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topics):
    known_topic=[]
    counts=[]
    for i in range(len(topics)):
        topic=[j+1 for j in range(len(topics[i])) if topics[i][j]=='1']
        known_topic.append(topic)
        s=1
        n=len(known_topic)
        while n>s:
            val=len(set(known_topic[s-1]+known_topic[n-1]))
            counts.append(val)
            s+=1
    result=max(counts)
    return(result,counts.count(result))
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
