def binary_search(list:list , target:int , start = 0 , end = None):


    if end is None: end = len(list) - 1
    if start > end: return -1

    mid_point = (start + end) // 2

    if list[mid_point] == target: return mid_point
    elif list[mid_point] > target: return binary_search(list , target , start , mid_point-1)
    else: return binary_search(list , target , mid_point+1 , end)








l1 = list()

for i in range(1 , 1000 + 1):
    l1.append(i)


# print(l1)


result = binary_search(l1 , 1000)
varify(result)
