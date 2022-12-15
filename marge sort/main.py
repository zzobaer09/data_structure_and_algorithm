def marge(arr):

    """
    this function sort an unsorted list

    ##################################

    devite list into smollest sublist which are assigned here as - Left(L) and Right(R)

    then marge all sublist together
    
    """


    if len(arr) > 1:

        mid_point = len(arr)//2

        L = arr[:mid_point]
        R = arr[mid_point:]

        marge(L)
        marge(R)
        
        i = j = k = 0

        while i<len(L) and j<len(R):

            if L[i] < R[j]:

                arr[k] = L[i]
                i+=1
                k+=1
            else:
                arr[k] = R[j]
                j+=1
                k+=1

        while i < len(L):

            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):

            arr[k] = R[j]
            j+=1
            k+=1


    return arr







Mlist = [10 , 9 , 2 , 100 , 12 , 3 , 66 , 8 , 9 , 101]


print(marge(Mlist))