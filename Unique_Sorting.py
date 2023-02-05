def insertionSort(arr):
    n = len(arr)
    for i in range(1, n): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
    return arr 
def uniqueElements(arr):
    n = len(arr)
    result = []
    for i in range(n): 
        if arr[i] not in result: 
            result.append(arr[i]) 
    return result 
arr = [5, 4, 7, 5, 1, 3, 4]
arr = insertionSort(arr)
result = uniqueElements(arr)
print(result)