def mergeLists(A, B, merged):
    i,j=0,0 #initialize i and j to 0
    # repeat until reaches the end of at least one list
    while i < len(A) and j < len(B):
       # insert the smaller element in merged and increment pointer
       if A[i] < B[j]:
           merged.append(A[i])
           i=i+1
       else:
           merged.append(B[j])
           j=j+1
    # if A/B is unfinished, add remaining elements to merged

    if i < len(A):
        merged += A[i:]
    if j < len(B):
        merged += B[j:]
A = [1,5,6] # example from previous slide
B = [3,4,7,8]
merged = []
mergeLists(A,B,merged)
print(merged)