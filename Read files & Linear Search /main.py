def check_Num(num):
    with open('gang.txt','r') as file:
        lines = [line.rstrip() for line in file]
        ints = [round(float(s)) for s in lines]
        print(ints)
        for i in range(len(ints)):
            if ints[i] == num:
                print(f'{num} was found at {i} ')

num = int(input("please enter a number"))
check_Num(num)
