def countFreq(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in freq:
        print("The frequency of", i, "is :", freq[i])

arr = [2, 3, 1, 2, 5, 7, 2, 3, 5]
countFreq(arr)