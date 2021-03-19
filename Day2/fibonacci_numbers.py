if __name__ == '__main__':

    num=input('How many numbers : ')
    x=0
    y=1
    numbers=[0,1]
    for i in range(int(num)-2):
        z=x+y
        numbers.append(z)
        x,y=y,z
        
    numbers=map(str,numbers)
    numbers=' '.join(numbers)
    
    print(numbers)
