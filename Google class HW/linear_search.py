#DECLARE array as ARRAY[0:9]


def linear_search(search_num):
    found = False
    array = [10,5,6,7,1,12,13,15,21,8]
    for i in range(len(array)):
        if array[i] == search_num:
            print(f'{search_num} has been found')
            found = True
    if not(found):
        print("Number was not found")


linear_search(int(input("Please input a number")))
