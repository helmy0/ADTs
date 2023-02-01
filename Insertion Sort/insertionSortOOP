class insertionSort():
    def __init__(self, arr):
        self.arr = arr
        
    def sort(self):
        
        for i in range(1, len(self.arr) ):
            key = self.arr[i]
            while self.arr[i-1] > key and i>0:
                self.arr[i], self.arr[i-1] = self.arr[i-1],self.arr[i]
                i -= 1
        print(self.arr)
s = insertionSort([4,3,5,8,2,3,23,52,3,2,7,0,1])
s.sort()