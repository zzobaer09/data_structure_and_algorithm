

def marge_sorte(list:list):

    """
    
    devided into the stublist ==> left and right

    marge them togather
    
    
    """



    if len(list) <= 1:
        return list

    left_half , right_half = split(list)

    left = marge_sorte(left_half)
    right = marge_sorte(right_half)

    return marge(left , right)


def split(list:list):
    
    """
    
    split the list into mid point

    """

    mid = len(list) // 2

    L = list[:mid]
    R = list[mid:]

    return L , R 



def marge(L:list , R:list):


    """
    
    marges the list into a new list
    
    
    """

    arr = []


    i = j = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr.append(L[i])
            i += 1

        else:
            arr.append(R[j])
            j += 1

    while i < len(L):
        arr.append(L[i])
        i += 1

    while j < len(R):
        arr.append(R[j])
        j += 1

    return arr





def varify(arr):



    n = len(arr)

    if n == 0 or n == 1:

        return True


    return arr[0] < arr[1] and varify(arr[1:])








LIst = [10 , 1 ,3 , 99 , 5 , 6 , 77]


margedList = marge_sorte(LIst)
print(margedList)
print(varify(margedList))
print(varify(LIst))


