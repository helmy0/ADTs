
class stack():
    
    def __init__(self):
        self.length = 0
        self.arr = [None for i in range(10)]
        self.currPointer = 0
    def add(self, value):
    
        if self.arr[len(self.arr) - 1] != None:
            print(f'The stack is full... \n {self.arr}')
            return self.arr           
        else:
            self.arr[self.currPointer] = value
            self.currPointer = self.currPointer + 1
            print(self.arr)
    def pop(self):
        self.currPointer = self.currPointer - 1 
        if self.arr[0] == None:
            print('The stack is empty... \n {self.arr}')
        else:
            self.arr[self.currPointer] = None
            print(self.arr) 
q= stack()

q.add(8)
q.add(2)
q.add(3)
q.pop()
q.pop()
q.pop()
q.pop()



