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
        nodes.append("None")
        return " -> ".join(nodes)
    
    def list_element(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
    def add_first(self, data):
        node=Node(data)
        node.next=self.head
        self.head=node
    
    def add_end(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
            return
        
        last = self.head 
        while (last.next): 
            last = last.next
        
        last.next =  node 
        
        
    def insert_after(self,node,data):
        if node is None:  
            print( "The given previous node must inLinkedList")
            return
        new_node=Node(data)
        new_node.next=node.next
        node.next=new_node
        
        
        
    def insert_before(self,node,data):
        new_node=Node(data)
        pre_node=self.head
        while pre_node.next !=node:
            pre_node=pre_node.next
            
        pre_node.next=new_node
        new_node.next=node

    def delet_node(self,node):
        
        if node==self.head:
            self.head=self.head.next
            return
        
        pre_node=self.head
        while pre_node.next !=node:
            pre_node=pre_node.next
            
        pre_node.next=node.next
        
        
    def number_of_occurrences(self,data,start_node):
        
        if start_node==None:
            return(0)
        if start_node.data==data:
            return(1+self.number_of_occurrences(data, start_node.next))
        else:
            return self.number_of_occurrences(data, start_node.next)


node=Node('a')
llist = LinkedList()
llist.head=node
print(llist)

llist.add_first('b')
print(llist)

llist.add_end('c')
print(llist)

llist.insert_after(node,'e')
print(llist)

llist.insert_before(node,'e')
print(llist)

llist.delet_node(node)
print(llist)

print(llist.number_of_occurrences('e',llist.head))
