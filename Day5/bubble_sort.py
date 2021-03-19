def bubble_sort(arr):
    
    size=len(arr)
    
    for i in range(size):
        for j in range(size-i-1):
            
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1],arr[j]
    
    arr=map(str,arr)
    return (' '.join(arr)) 

if __name__ == '__main__':
    
    arr=list(map(int,input().split()))
    print(bubble_sort(arr))
