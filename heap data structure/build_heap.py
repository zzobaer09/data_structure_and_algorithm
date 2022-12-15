arr = [5,10,11,15,2,3,20]

def swap(arr , i , j): arr[i] , arr[j] = arr[j] , arr[i]

def heapify(arr , i):

    l = len(arr)
    lc = (2*i)+1
    rc = (2*i)+2

    # max = i
    # if lc < len(arr) and arr[lc] > arr[i]: max = lc

    # if rc < len(arr) and arr[rc] > arr[max]: max = rc
    
    # if i != max:
    #     if arr[i] < arr[max]: 
    #     swap(arr , i , max)
    #     heapify(arr , max)

    while (lc < l and arr[lc] > arr[i]) or (rc < l and arr[rc] > arr[i]):
        max = lc if not (rc < l) or (arr[lc] > arr[rc]) else rc 
        swap(arr , i , max)

        i = max
        lc = (2*i)+1
        rc = (2*i)+2




def build(arr , stop = -1):
    n = len(arr)
    start = n//2 -1
    
    for i in range(start , stop, -1):
        heapify(arr , i)
        



def delete(arr): 
    data = arr[0]
    swap(arr, 0 , len(arr)-1)
    del arr[len(arr)-1]
    build(arr)


    return data


def heapSort(arr):
    build(arr)
    for i in range(len(arr)-1 , -1 ,-1):
        swap(arr , 0 , i)
        build(arr ,  i)



    return arr


print(heapSort(arr))
print(arr)

# build(arr)
# print(arr)

# print(heapSort(arr))
# print(arr)






    