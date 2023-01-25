stack = [None for i in range(10)]
item = 0 
head = -1




def instack(item):
    global head
    if stack[len(stack)-1] ==None:
        stack[head+1] = item
        head += 1
    elif stack[9] != None:
        print("The stack is Full!!!")
def popstack():
    global head
    if stack[0] == None:
        print("Stack is empty!!!")
    else:
        stack[head] = None
        head -=1
while item != -1:
    if input("i or p") == 'i':
        instack(int(input("Please enter a number")))
        print(stack)
    else: 
        popstack()
        print(stack)