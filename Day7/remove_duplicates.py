if __name__=='__main__':
    lis=list(map(int,input().split()))
    lis=map(str,set(lis))
    lis=' '.join(lis)
    print(lis)
