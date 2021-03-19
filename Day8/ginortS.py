# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    s=input()
    lower=sorted([i for i in s if i.islower()])
    upper=sorted([i for i in s if i.isupper()])
    even=sorted([i for i in s if i.isdigit()and int(i)%2==0])
    odd=sorted([i for i in s if i.isdigit()and int(i)%2!=0])
    s=''.join(lower)+''.join(upper)+''.join(odd)+''.join(even)

    print(s)
