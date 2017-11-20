def shellSort(arr,subNo):
    startpos = 0
    while startpos < subNo:
        subSort(arr,startpos,subNo)
        startpos+=1

    subSort(arr,0,1)   


def subSort(arr,startpos,subNo):
    for i in range(startpos+subNo, len(arr), subNo):
        pos = i
        currdata = arr[i]

        while pos > startpos and arr[pos-subNo] > currdata:
            arr[pos] = arr[pos-subNo]
            pos-=subNo

        arr[pos] = currdata

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist,2)
print(alist)