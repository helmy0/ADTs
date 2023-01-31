class queue():
    
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.noItems = 0
        self.arr = [None for i in range(10)]
        
    def enqueue(self,value):
        
        if self.noItems == 10:
            print(f'The queue is full \n {self.arr} ')
            return 
        else:
            self.noItems += 1
            self.arr[self.tail] = value
            self.tail += 1
            print( f'The updated queue is  \n {self.arr} ' )
    def unqueue(self):
        if self.noItems == 0:
            print(f'The queue is empty \n {self.arr}')
            return
        else:
            self.noItems -= 1
            self.arr[self.head] = None
            if self.head == len(self.arr) - 1:
                self.head = 0
            else:
                self.head += 1
            print(f'The updated queue is  \n {self.arr}')
    
      




    