import random

if __name__=='__main__':

    num=''.join([str(random.randint(0,9)) for _ in range(3)])
    temp_num=num

    n=input('Enter a 3-digit number:')
    
    countars={'attempts':1 ,'hit':0 ,'miss':0}
    
    while num!=n:
        countars['attempts']+=1
        
        for i in range(3):
            if n[i]==num[i]:
                countars['hit']+=1
                temp_num=num.replace(num[i],'')
                
        for i in range(3):
            if n[i]in temp_num:
                countars['miss']+=1
                
                
        print('{} hit {} miss'.format(countars['hit'],countars['miss']))
        
        countars['hit']=0
        countars['miss']=0
        temp_num=num
        n=input()
        
    print(countars['attempts'])
