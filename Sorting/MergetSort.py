def mergeSort(array):
    if len(array) <= 1:
        return array
    left = array[:len(array) // 2]
    right = array[len(array) // 2:]

    # Recursion
    left = mergeSort(left)
    right = mergeSort(right)

    # Merge
    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            merged.append(left[i])
            i += 1
        else:

            merged.append(right[j])
            j += 1

    if len(left) > 0:
        merged += left[i:]

    if len(right) > 0:
        merged += right[j:]

    return merged


list = [5, 3, 2, 1, 5, 3, 2, 9, 10, 23]

result = mergeSort(list)

print(result)
