'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
if __name__=='__main__':
    t=int(input())
    
    for _ in range(t):
        
        n,m=list(map(int,input().split()))
        student=input().split()
        
        n_student=[i for i in student[:n]]      
        m_student=[i for i in student[n:m+n]]
        
        for i in m_student:
        
            if i in n_student:
                print('YES')
                
            else:
                n_student.append(i)
                print('NO')
 



