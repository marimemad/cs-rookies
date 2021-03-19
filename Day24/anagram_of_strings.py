def anagram(s,t):
    
    if len(s)!=len(t):
        return

    
    s_hash_table={i:0 for i in range(26)}
    t_hash_table={i:0 for i in range(26)}
    
    n=len(s)
    
    ascii_s=[ord(i) for i in s]
    ascii_t=[ord(i) for i in t]
    
    count=0
    a=ord('a')
    
    for i in range(n):
        s_hash_table[ ascii_s[i]-a ]+=1
        t_hash_table[ ascii_t[i]-a ]+=1
        
    ascii_s=list(set(ascii_s))
    for i in range(len(ascii_s)):
        x=s_hash_table[ ascii_s[i]-a ]
        y=t_hash_table[ ascii_s[i]-a ]
        
        if x>y:
            count=count+(x-y)
    return(count)
    
    
    
    
if __name__=='__main__':
    s=input()
    t=input()
    print(anagram(s,t))
    
