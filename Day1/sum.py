def sum_for_loop(n):
    result=0
    for i in n:
        result+=i
    return(result)

def sum_while_loop(n):
    
    index=0
    result=0
    while index!=len(n):
        result+=n[index]
        index+=1
    return (result)

def sum_recursion(n):
    
    if len(n)==0:
        return 0
    else:
        num=n[0]
        n.remove(num)
        return(num+sum_recursion(n))
        
if __name__ == '__main__':
    number=input('Enter number separating by space : ')
    number=number.split()
    number=[int(i) for i in number]
    
    print(sum_for_loop(number))
    print(sum_while_loop(number))
    print(sum_recursion(number))
    
    
    
