import random

if __name__ == '__main__':

    num=input('Enter number between 1 to 10 ')
    ran=random.randint(1, 10)
    counter=1
    while int(num)!=ran:
        num=input('Wrong! try again ')
        counter+=1
    print(counter)
