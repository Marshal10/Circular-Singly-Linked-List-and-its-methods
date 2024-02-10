class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def __str__(self):
        temp=self.head
        result=""
        while temp:
            result+=str(temp.value)
            temp=temp.next
            if temp==self.head:
                break
            result+=" -> "
        return result
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1
        
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        self.length+=1
        
    def insert(self,index,value):
        new_node=Node(value)
        if index < -1  or index > self.length:
            raise Exception("Index out of range")
        if index==0:  
            if self.head is None:
                self.head=new_node
                self.tail=new_node
                new_node.next=new_node
            else:
                new_node.next=self.head
                self.head=new_node
                self.tail.next=new_node
        elif index==self.length or index==-1:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
        self.length+=1
        
    def traverse(self):
        current=self.head
        while current:
            print(current.value)
            current=current.next
            if current==self.head:
                break
        
cs_linked_list=CircularSinglyLinkedList()
cs_linked_list.prepend(50)
cs_linked_list.prepend(90)
cs_linked_list.append(100)
print(cs_linked_list)
cs_linked_list.insert(1,70)
print(cs_linked_list)
cs_linked_list.traverse()