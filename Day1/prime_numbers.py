
if __name__ == '__main__':
    n=input('Enter number : ')
    prime_n=str()
    counter=0
    for num in range(2,int(n)):
        for i in range (1,num):
            if num%i==0:
                counter+=1
        
        if counter ==1:
            prime_n=prime_n+str(num)+' '
        counter=0
            
    print(prime_n)
