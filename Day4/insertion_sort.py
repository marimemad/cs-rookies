def insertion_sort(arr):

    for i in range(1, len(arr)):
        
        key = arr[i]
        j = i-1
    
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key  
    arr=map(str,arr)
    arr=' '.join(arr)
    return(arr)


if __name__ == '__main__':
    
    arr =list( map(int, input('Enter number sperating by space : ').split()))
    print(insertion_sort(arr))
