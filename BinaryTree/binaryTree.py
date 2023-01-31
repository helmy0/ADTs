class node():
    
    def __init__(self, value = None) :
        
        self.left = None
        self.right = None
        self.value = value
    def insert(self,value):
        if self.value >

class Tree():
    def __init__(self) :
        self.root = None
    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = node(value)
            return True
        
    
t = Tree()

        