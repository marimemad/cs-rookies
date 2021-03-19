if __name__=='__main__':
    num=input()
    counter=0
    while num!='6174':
        
        ascending=''.join(sorted([i for i in num]))
        descending=''.join(sorted([i for i in num],reverse=True))
        num= str (int(descending)-int(ascending))
        
        while len(num)!=4:
            num+='0'
        counter+=1
        
    print(counter)
