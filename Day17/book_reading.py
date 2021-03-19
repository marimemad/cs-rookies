if __name__=='__main__':
    
    n=int(input())
    t=int(input())
    
    ai=[ int(input()) for _ in range(n)]
    
    days=0
    for i in ai:
        if t >0:
            t=t-(86400-i)
            days+=1
            
    print(days)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
