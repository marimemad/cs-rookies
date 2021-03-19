class Max_Heap:
    def __init__(self):
        self.heap=[]
        
    def size(self):
        return(len(self.heap))
        
    def heapify(self,position):
        left_child=2*position+1
        right_child=2*position+2
        largest=position
        
        if left_child<=self.size()-1 and self.heap[position]<self.heap[left_child]:
            largest=left_child
            
        elif right_child<=self.size()-1 and self.heap[position]<self.heap[right_child]:
            largest=right_child
            
        if largest!=position:
            self.heap[position], self.heap[largest] = self.heap[largest], self.heap[position]
            self.heapify(largest)
            
            
    def insert(self,val):
        if self.size()==0:
            self.heap.append(val)
        else:
            self.heap.append(val)
            for level in range((self.size()//2), -1, -1):
                self.heapify(level)
                    
                    
                    
if __name__=='__main__':
    values=list(map(int,input().split()))
    my_heap=Max_Heap()
    for val in values:
        my_heap.insert(val)
        
    print(my_heap.heap)
