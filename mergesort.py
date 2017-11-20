def mergeSort(arr,p,q):

    if p >= q: 
        return

    m = (p+q)//2

    mergeSort(arr,p,m)
    mergeSort(arr,m+1,q)
    subSort(arr,p,m,q)

def subSort(arr,p,m,q):

    #temp1 = [0]*(m-p+1)
    #temp2 = [0]*(q-m)

    temp1 = arr[p:m+1]
    temp2 = arr[m+1:q+1]

    x=0
    y=0
    for i in range(p,q+1):
        if y != len(temp2) and x != len(temp1):
            if temp1[x] > temp2[y]:
                arr[i] = temp2[y]
                y +=1
            else: 
                arr[i] = temp1[x]
                x +=1
        
        elif y != len(temp2):
            arr[i] = temp2[y]
            y += 1

        elif x != len(temp1):
            arr[i] = temp1[x]
            x += 1

alist = [54,26,93,17,77,31,44,55]
mergeSort(alist,0,len(alist))
print(alist)