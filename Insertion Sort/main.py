list = [1,4,2,3,25,6,10,7,85,34]


        
for i in range(1,len(list)):
    key = list[i]
    item = i-1
    while item >= 0 and list[item] > key:
        list[item+1] = list[item]
        item -= 1
    list[item+1]=key
    print(list) 