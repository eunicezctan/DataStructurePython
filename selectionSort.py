def selectionSort(arr):
    for pos in range(len(arr)-1,0,-1):
        index = 0
        for i in range(1,pos+1):
            if arr[i] > arr[index]:
                index = i
        if index != pos:
            arr[index],arr[pos] = arr[pos],arr[index]

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)