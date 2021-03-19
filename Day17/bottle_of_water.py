if __name__=='__main__':
    
    n=int(input())
    bottel=[ input().split() for _ in range(n)]
    
    if n==2:
        print('Yes')
        
    else:
        v=list()
        c=set()
        for i in bottel:
            v.append(int(i[0]))
            c.add(int(i[1]))
            
        c=sorted(c)
        
        if sum(v)<=(c[-1]+c[-2]):
            print('Yes')
        
        else:
            print('No')
                    
