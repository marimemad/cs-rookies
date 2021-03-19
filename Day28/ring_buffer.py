from os import system, name 
from time import sleep 

class CircularQueue:
    
    def __init__(self, size):
        self.size=size
        self.queue=[None]*size
        self.n_elements=0
        self.head=0
        self.rear=self.size-1
        
    def __str__(self):
        return(' '.join(list(filter(None,self.queue))))
        
        
    def is_full(self):
        return(self.n_elements==self.size)
    
    def is_empty(self):
        return(self.n_elements==0)
    
    
    def enqueue(self,element):
        
        if self.is_full():
            return('The Queue Full')
        
        self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=element
        self.n_elements+=1
        
    def dequeue(self):
        
        if self.is_empty():
            return('The Queu Empty')
        
        self.queue.pop(self.head)
        self.head=(self.head+1)%self.size
        self.n_elements-=1
        
    
def clear():
    system('cls')  if name == 'nt' else system('clear')
    

def menue():
    sleep(2)
    clear()
    print(' 1)Push Element','\n','2)Pop Element','\n','3)Exit','\n')
    n=int(input('Enter nember : '))
    clear()
    return(n)
    
    
if __name__=='__main__':
    
    size=int(input('enter size of Queu : '))
    ring=CircularQueue(size)
    clear()
    
    option=menue()
    while option!=3:
        
        if option==1:
            ring.enqueue(input('enter element : '))
            option=menue()
            
        elif option==2:
            ring.dequeue()
            option=menue()
            
    print('Elements : ',ring)
            
            
