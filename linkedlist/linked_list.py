class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.count = 0

class linked_list:
    def __init__(self):
        self.head=None
        self.count=0

    def insertEnd(self, newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode

    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode         
        self.head.next = tempNode        
        #del tempNode


    def insertAt(self, newNode, position):
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition == position:
                previousNode.next=newNode
                newNode.next=currentNode
                break
            previousNode=currentNode
            currentNode=currentNode.next
            currentPosition += 1

    def deleteEnd(self):
        lastNode=self.head
        while lastNode.next is not None:
            prevNode=lastNode
            lastNode=lastNode.next
        prevNode.next=None

    

    def deleteAt(self, position):
        
        if self.head is None:
            print("The linked list is empty ")
            return False

        elif position > self.count or position < 0:
            print("The postion entered is not avalible/incorrect")
            return False
        else:
        
            currentNode=self.head
            currentPosition=0
            while True:
                if currentPosition == position:
                    prevNode.next=currentNode.next
                    currentNode.next=None
                    break
                prevNode=currentNode
                currentNode=currentNode.next
                currentPosition +=1
    def deleteNodes(self):
        self.head = None

          
            

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def traversal(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.data, "->", end=" ")
            currentNode=currentNode.next
    

    def deleteHead(self):
        if self.isEmpty() is False:
            prevHead=self.head
            self.head=self.head.next
            prevHead.next=None
            print("The first item is deleted successfully")
        else:
            print("Linked List is empty, Delete Failed")
    
    def countNodes(self):
        if self.head is None:
            return 0
        else:
            curr = self.head
            while True:
                self.count += 1
                if curr.next is None:
                    return self.count
                else:
                    curr = curr.next
                

    def deleteNegative(self):
        if self.head is None:
            return False, "Empty list"
        else:
            curr = self.head
            size = self.countNodes()
            negative_positions = []
            currPosition = 0
            while curr:
                if curr.data < 0:
                    negative_positions.append(currPosition)
                curr = curr.next
                currPosition += 1

            for position in reversed(negative_positions):
                self.deleteAt(position)

            return True, "Negative nodes deleted"
    def sumNodes(self):
        if self.head is None:
            return 0
        else:
            curr = self.head
            total = 0
            while curr:
                total += curr.data
                curr = curr.next
            return total

ls = linked_list()

ls.insertEnd(Node(3))
ls.insertEnd(Node(-3))
ls.insertEnd(Node(-3))
ls.insertEnd(Node(-5))
ls.insertEnd(Node(5))

ls.deleteNegative()
ls.traversal()
