list = [y for y in range(100)]



def binary_search(search_item):
    lb = 0
    ub = len(list) - 1
    failed_search = False
    found = False
    while not(found) and not(failed_search):
        mid = round((lb + ub) / 2)
        if mid == search_item:
            print(f'{search_item} was found')
            found = True
        if search_item > mid:
            lb = mid + 1
        elif search_item < mid:
            ub = mid - 1
        if ub == lb:
            print(f"{search_item} wasnt found")
            failed_search = True        
            
binary_search(int(input("please enter a number")))




    

    


    