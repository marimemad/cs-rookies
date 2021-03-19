class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return " ".join(map(str,nodes))
    
    def list_element(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
    def add(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
            return
        
        last = self.head 
        while (last.next): 
            last = last.next
        
        last.next =  node 
        
    
    def delet_node(self,node):
        
        if node==self.head:
            self.head=self.head.next
            return
        
        pre_node=self.head
        while pre_node.next !=node:
            pre_node=pre_node.next
            
        pre_node.next=node.next
        
def delet_friends(friends,n,k):

    for i in range(k):
        frined=friends.head
        del_fri=False
        
        for i in range(int(n)-1):
            
            if frined.data<frined.next.data:
                friends.delet_node(frined)
                del_fri=True
                break
            
            else:
                frined=frined.next
                
                
        if del_fri==False:
            last_friend=friends.head
            while last_friend.next!=None:
                last_node=last_friend.next
            
            friends.delet_node(last_friend)
            
    return(friends)

    

if __name__=='__main__':
    
    t=int(input())
    
    for i in range(t):
        n,k=input().split()
        popularity=input().split()
        popularity=list(map(int,popularity))
    
        friends=LinkedList()
        for i in range(int(n)):
            friends.add(popularity[i])
            
        print(delet_friends( friends,int(n),int(k) ))
        
        
