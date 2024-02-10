class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
cs_linked_list=CircularSinglyLinkedList()
print(cs_linked_list)