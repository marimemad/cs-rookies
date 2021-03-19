#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    kaprekar_n=[]
    
    for i in range(p,q+1):
        sqr=str(i*i)
        d=len(sqr)//2
        
        if len(sqr)==1:
            if i==1:
                kaprekar_n.append(i)
            continue
        
        l=int(sqr[:d])
        r=int(sqr[d:])
        
        if l+r==i:
            kaprekar_n.append(i)
    kaprekar_n=' '.join(map(str,kaprekar_n))
    if kaprekar_n:
        return(kaprekar_n)
    else:
        return('INVALID RANGE')


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    print(kaprekarNumbers(p, q))
