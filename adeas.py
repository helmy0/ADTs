
arr = [1,6,3,2,8,5,32,2]

def bubblesort():
    global arr
    sorted = False 
    while not sorted:
        sorted  = True
        for i in range(len(arr)- 1):
            if arr[i]> arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)
    
bubblesort()