queue = [None for i in range(10)]
head  = 0 
tail = -1
queue_length = 0
item = 0

def equeue(item):
    global tail, queue_length
    if queue_length < 10 and tail !=9:
        queue[tail+1] = item
        queue_length +=1
        tail +=1
    elif tail == 9 and queue_length<10:
        tail = -1
        queue[tail+1] = item
        queue_length +=1
        tail +=1
    else:
        print("Queue is full!!!")
def dqueue():
    global head, queue_length
    if queue_length != 0 and head != len(queue)-1:
        queue[head] = None
        head += 1
        queue_length -=1
    elif queue_length != 0 and head == len(queue) -1:
        head = 0
        queue[head] = None
        head+=1
    elif queue_length == 0:
        print("Queue is empty!!!")
while item != -1:
    
    if input('p or i') == 'i':
        item = int(input("Please enter a number"))
        equeue(item)
    else:
        dqueue()
    
    print(queue,queue_length,tail)
    
    
    # if input("pop or in") == 'pop':
        
    #     print(head,tail,'\n' ,queue)
    # else:
    #     item = int(input("Please enter a number"))
        
    #     print(head,tail,'\n' ,queue)