items = [0]
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        items.append(max(nums[1], items[-1]))
    elif nums[0] == 2:
        items.pop()
    else:
        print(items[-1])
        
        
        
        
        
        
        
        
        
        
        
        
        
## Enter your code here. Read input from STDIN. Print output to STDOUT
#if __name__=='__main__':
    #stack=[]
    #for i in range(int(input())):
        #x = list(map(int, input().split()))
        #if x[0]==1:
            #stack.append(x[1])
        #elif x[0]==2:
            #stack.pop()
        #else:
            #print(max(stack))
