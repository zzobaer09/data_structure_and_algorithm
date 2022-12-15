# we have to build sort an unsorted arr using heap sort
class HeapSort:
    def __init__(self , arr):
        self.arr = arr

    # swap function 
    def __swap(self , i , j): self.arr[i] , self.arr[j] = self.arr[j] , self.arr[i]

    # heapify the array
    def __heapify(self , i , length = None):
        if length is None: 
            length = len(self.arr)

        left_child = (2*i)+1
        right_child = (2*i)+2
        
        # max = i
        # if left_child < length and self.arr[left_child] > self.arr[i]: max = left_child
        # if right_child < length and self.arr[right_child] > self.arr[i]: max = right_child

        # if i != max:
        #     if self.arr[max] > self.arr[i]: 
        #         self.__swap(i , max)
        #         self.__heapify(max , length)



        while (left_child < length and self.arr[left_child] > self.arr[i]) or (right_child<length and self.arr[right_child] > self.arr[i]):
            max = left_child if not right_child < length or self.arr[left_child] > self.arr[right_child] else right_child
            self.__swap(max , i)
            i = max
            left_child = (i*2 )+1
            right_child = (i*2)+2





    # * this function gonna build a hole heap form a unsorted array
    def __build(self):
        st = (len(self.arr)//2)-1
        for i in range(st , -1 , -1):
            self.__heapify(i)

    def heap_sort(self):
        self.__build()
        for i in range(len(self.arr)-1,0,-1):
            self.__swap(i , 0)
            self.__heapify(0,i)







t = HeapSort([5,10,11,15,2,3,20])
t.heap_sort()
print(t.arr)

