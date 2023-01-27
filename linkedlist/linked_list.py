class Node():
    def __init__(self, value = None ):
        self.value = value
        self.next = None
    
class linked_List():   
    def __init__(self) -> None:
        self.head = Node()
    
    def insert(self,value):
        new_Node = Node(value)
        curr = self.head
        while curr.next != None:
            curr = curr.next 
        curr.next = new_Node

    def print(self):
        curr = self.head
        list = []
        while curr.next != None:
            curr = curr.next
            list.append(curr.value)
             
        print(list)
        
l1 = linked_List()

l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)
l1.insert(6)
l1.print()
