#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    test=(x1>x2 and v1>=v2 , x2>x1 and v2>=v1)
    
    if test[0] or test[1]:
        return('NO')
    #postion=start+(number of jums*distance)
    #x1+(v1*n)=x2+(v2*n)
    #x1-x2=n(v2-v1)
    elif (x1-x2)%(v2-v1)==0:
        return('YES')
    else:
        return('NO')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
