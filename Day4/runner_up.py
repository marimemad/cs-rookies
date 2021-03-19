 
if __name__ == '__main__':
    arr =list( map(int, input('Enter number sperating by space : ').split()))
    arr.sort()
    x=-2
    while arr[-1]==arr[x]:
        x-=1
        

    print(arr[x])
    
