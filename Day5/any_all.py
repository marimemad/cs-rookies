if __name__=='__main__':
    
    n=int(input())
    arr=input().split()
    palindromic=[i==i[::-1] for i in arr]
    positive=[int(i)>0 for i in arr]
    print(any(palindromic) and all(positive))


