class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
    
    def search(self, data):
        if self.root is None:
            return None
        else:
            return self._search(data, self.root)
        
    def _search(self, data, node):
        if data == node.data:
            return node
        elif data < node.data and node.left is not None:
            return self._search(data, node.left)
        elif data > node.data and node.right is not None:
            return self._search(data, node.right)
        else:
            return None
    
    def display(self):
        if self.root is not None:
            self._display(self.root)
            
    def _display(self, node):
        if node is not None:
            self._display(node.left)
            print(node.data)
            self._display(node.right)


# The Node class defines a single node in the tree, with data to store the data for the node,
# and left and right pointers to refer to its left and right child nodes
# 
# 
# 
# The Tree class defines the tree structure and its operations. The insert method takes a data value and inserts it into the binary tree. 
# If the tree is empty, a new Node with the data is created as the root of the tree. If the tree is not empty, the _insert method is called to insert the node in the correct place in the tree.
# The _insert method compares the data to the data stored in the current node, and if the data is less, it moves to the left child node. 
# If the data is greater, it moves to the right child node. If there is no child node, it creates a new Node with the data as the child node.

# The search method takes a data value and returns the node containing that data. If the tree is empty, it returns None. 
# If the tree is not empty, it calls the _search method to search the tree. 
# The _search method compares the data to the data stored in the current node, and if the data is equal, it returns the node.
# If the data is less, it moves to the left child node. If the data is greater, it moves to the right child node. If there is no child node, it