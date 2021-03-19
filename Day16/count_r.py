if __name__=='__main__':
    s=input()
    n=int(input())
    
    counter1=n//len(s)
    counter2=s.count('r')*counter1
    
    counter1=n-counter1*len(s)
    
    counter2+=s[0:counter1].count('r')
    print(counter2)
    
    
    #memory error
    #sequence=input()
    #n=int(input())
    
    #string=sequence
    #counter=(n-len(string))//len(string)
    
    #string+=(sequence*counter)
    
    #counter=n-len(string)
    
    #for i in range(counter):
         #string+=sequence[i]
         
    
    #print(string.count('r'))
    
