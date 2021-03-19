# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    n,x=input().split()
    subject=[list(map(float,input().split())) for _ in range(int(float(x)))]
    subject=zip(*subject)
    avg=[(sum (list(sub))/(len(list(sub)))) for sub in subject]

    avg=map(str,avg)
    avg='\n'.join(avg)
    print(avg)

