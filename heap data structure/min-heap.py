
# *
# ! min heap
# *


class Heap:
    def __init__(self):
        self.storage = []

    def __getParentIdx(self , i): return (i-1)//2
    def __getLCIdx(self , i): return (2*i)+1
    def __getRCIdx(self , i): return (2*i)+2

    def __hasLC(self , i): return len(self.storage) > self.__getLCIdx(i)
    def __hasRC(self , i): return len(self.storage) > self.__getRCIdx(i)

    def __swap(self , i , j): self.storage[i] , self.storage[j] = self.storage[j] , self.storage[i]

    def __heapifyUp(self):
        i = len(self.storage) - 1

        while i != 0 and self.storage[i] < self.storage[self.__getParentIdx(i)]:
            self.__swap(i , self.__getParentIdx(i))

            i = self.__getParentIdx(i)

    def __heapifyDown(self , i):
        


        while (self.__hasLC(i) and self.storage[i] > self.storage[self.__getLCIdx(i)]) or (self.__hasRC(i) and self.storage[i] > self.storage[self.__getRCIdx(i)]):
            small = self.__getLCIdx(i) if not self.__hasRC(i) or self.storage[self.__getLCIdx(i)] < self.storage[self.__getRCIdx(i)] else self.__getRCIdx(i)

            self.__swap(i , small)

            i = small





    def insert(self , val):
        # insert mathod always gonna be insert val in the least of the heap
        self.storage.append(val)
        self.__heapifyUp()
    
    def delete(self):
        data = self.storage[0]
        self.__swap(0 , -1)

        del self.storage[-1]

        self.__heapifyDown(0)

        return data

    def build(self , arr = None):
        if arr != None: self.storage = arr

        n = len(self.storage)//2 -1

        for i in range(n , -1 , -1):
            self.__heapifyDown(i)




        






t = Heap()


t.build([5,10,11,15,2,3,20])
print(t.storage)

# t.insert(10)
# t.insert(5)
# t.insert(20)
# t.insert(3)
# t.insert(6)
# t.insert(2)
# t.insert(9)

# print(t.storage)

# print(t.delete())


# # print
# print(t.storage)


