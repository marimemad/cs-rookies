 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player, player_count):
    ranked = sorted(set(ranked), reverse = True)
    j = len(ranked)
    indexs=list()
    for i in player:
        while (j > 0) and (i >= ranked[j-1]):
            j -= 1
        indexs.append(j+1)
    return(indexs)

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player, player_count)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()







##!/bin/python3

#import math
#import os
#import random
#import re
#import sys

##
## Complete the 'climbingLeaderboard' function below.
##
## The function is expected to return an INTEGER_ARRAY.
## The function accepts following parameters:
##  1. INTEGER_ARRAY ranked
##  2. INTEGER_ARRAY player
##

#def climbingLeaderboard(ranked, player, player_count):
    #ranked_=sorted(list(set(ranked)),reverse=True)
    #indexs=list()    
    #ranked_.append(ranked_[-1]-10)

    #print(ranked_)
    #for i in range(player_count):
        #for j in range(len(ranked_)):
            #print(player[i],ranked_[j])
            #if player[i]>=ranked_[j]:
                #indexs.append(ranked_.index(ranked_[j])+1)
                #break
        
    
    #return(indexs)

    ## Write your code here

#if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #ranked_count = int(input().strip())

    #ranked = list(map(int, input().rstrip().split()))

    #player_count = int(input().strip())

    #player = list(map(int, input().rstrip().split()))

    #result = climbingLeaderboard(ranked, player, player_count)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
