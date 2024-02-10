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
        
cs_linked_list=CircularSinglyLinkedList()
print(cs_linked_list)
cs_linked_list.append(10)
cs_linked_list.append(20)
cs_linked_list.append(30)

print(cs_linked_list)