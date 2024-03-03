class Node():

    def __init__(self,data=None):
        self.data = data
        self.right = None
        self.left = None
class Tree():

    def __init__(self):
        self.head = None


    def add(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            currNode = self.head
            if newNode.data < currNode.data:

                if currNode.left is None:
                    currNode.left = currNode
                else:
                    currNode = currNode.left

            else:
                if currNode.right is None:
                    currNode.right = currNode
                else:
                    currNode = currNode.right

    def traversal(self):

        if self.head is None:
            print("The tree is empty")
            return False
        else:


tree = Tree()
tree.add(5)
tree.add(8)
tree.add(4)
tree.add(2)