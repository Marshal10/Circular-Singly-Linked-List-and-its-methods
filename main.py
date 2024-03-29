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
    
    def search(self,target):
        current=self.head
        index=0
        while current:
            if current.value==target:
                return index
            current=current.next
            index+=1
            if current==self.head:
                break
        return -1
    
    def get(self,index):
        if index==-1:
            return self.tail
        if index < -1 or index >=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    
    def set_value(self,index,value):
        # if index==-1:
        #     self.tail.value=value
        #     return True
        # elif index < -1 or index >=self.length:
        #     return None
        # current=self.head
        # for _ in range(index):
        #     current=current.next
        # current.value=value
        # return True
        
        update_node=self.get(index)
        if update_node:
            update_node.value=value
            return True
        return False
    
    def pop_first(self):
        popped_node=self.head
        if self.head is None:
            return None
        if self.length==1:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
            popped_node.next=None
        self.length-=1
        return popped_node
    
    def pop(self):
        popped_node=self.tail
        if self.head is None:
            return None
        if self.length==1:
            self.head=self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            popped_node.next=None
        self.length-=1
        return popped_node
    
    def remove(self,index):
        if self.head is None or index < -1 or index >= self.length:
            return None
        if index==-1 or index==self.length-1:
            return self.pop()
        elif index==0:
            return self.pop_first()
        prev_node=self.get(index-1)
        popped_node=prev_node.next
        prev_node.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node.value
    
    def delete_all(self):
        if self.length==0:
            return
        self.tail.next=None
        self.head=None
        self.tail=None
        self.length=0
        
    
cs_linked_list=CircularSinglyLinkedList()
cs_linked_list.prepend(50)
cs_linked_list.prepend(90)
cs_linked_list.append(100)
# cs_linked_list.insert(1,70)
print(cs_linked_list)
# print(cs_linked_list)
# cs_linked_list.traverse()
# print(cs_linked_list.set_value(2,200))
# print(cs_linked_list.remove(0))
print(cs_linked_list.length)
cs_linked_list.delete_all()
print(cs_linked_list)
print(cs_linked_list.length)