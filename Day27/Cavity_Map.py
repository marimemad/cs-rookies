 
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(n,grid):
    for row in range(1,n-1):
        
        row_=[i for i in grid[row]]
        cols=len(row_)
        
        for col in range(1,cols-1):
            right=grid[row][col+1]
            left=grid[row][col-1]
            up=grid[row-1][col]
            down=grid[row+1][col]
    
            if (grid[row][col]> right and grid[row][col] >left and grid[row][col]>up and grid[row][col] >down) :
                
                row_[col]='X'
                grid[row]=''.join(row_)
        
    return(grid)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(n,grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
