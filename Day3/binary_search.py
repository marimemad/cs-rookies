def binary_seach(elements,item,start,end):
    
    middel=(start+end)//2
    
    if elements[middel]==item:
        return(middel)
    
    elif elements[middel]>item:
        return(binary_seach(elements,item,0,middel-1))
    
    else:
        return(binary_seach(elements,item,middel+1,end))






if __name__=='__main__': 
    
    lis=list(map(int,input('Enter number sepetaring by space : ').split()))
    item=int(input('Enter number : '))
    print('The index is : {}'.format(binary_seach(lis,int(item),0,len(lis))))
    
    
    
    
    
    
    
    
    
