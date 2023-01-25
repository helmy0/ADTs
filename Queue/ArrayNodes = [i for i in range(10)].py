#QUESTION 1

RootPointer = -1 #DECLARE RootPointer AS INTEGER
ArrayNodes = [[[0]*3] for i in range(10)] # DECLARE ArrayNodes 0:19 AS INTEGER
FreeNode = -1 #DECLARE FreeNode AS INTEGER


ArrayNodes[0][0][2] = 5
print(ArrayNodes)