
class Heap:

    def __init__(self):
        self.heap = []
    

    # all get
    def __getParentIdx(self , i): return (i-1)//2
    def __getLCIdx(self , i): return (2*i)+1
    def __getRCIdx(self , i): return (2*i)+2

    # all has
    def __hasParent(self , i): return self.__getParentIdx(i) >= 0
    def __hasLC(self , i): return self.__getLCIdx(i) < len(self.heap)
    def __hasRC(self , i): return self.__getRCIdx(i) < len(self.heap)


    # all element
    def __parent(self , i): return self.heap[self.__getParentIdx(i)]
    def __LC(self , i): return self.heap[self.__getLCIdx(i)]
    def __RC(self , i): return self.heap[self.__getRCIdx(i)]

    # swap
    def __swap(self , i , j): self.heap[i] , self.heap[j] = self.heap[j] , self.heap[i]

    # heapify mathods
    def __heapifyUp(self):
        i = len(self.heap) -1

        while self.__hasParent(i) and self.__parent(i) < self.heap[i]:
            self.__swap(self.__getParentIdx(i) , i)
            i = self.__getParentIdx(i)

    def __heapifyDown(self , i):

        # while (self.__hasLC(i) and self.heap[i] > self.heap[self.__getLCIdx(i)]) or (self.__hasRC(i) and self.heap[i] > self.heap[self.__getRCIdx(i)]):
        #     small = self.__getLCIdx(i) if not self.__hasRC(i) or self.heap[self.__getLCIdx(i)] < self.heap[self.__getRCIdx(i)] else self.__getRCIdx(i)

        #     self.__swap(i , small)

        #     i = small


        max = i
        if self.__hasLC(i) and self.__LC(i) > self.heap[i]: max = self.__getLCIdx(i)
        if self.__hasRC(i) and self.__RC(i) > self.heap[max]: max = self.__getRCIdx(i)

        if max != i:
            if self.heap[i] < self.heap[max]: 
                self.__swap(i , max)
                self.__heapifyDown(max)




    def build(self , arr = None):
        if arr != None: self.heap = arr

        n = len(self.heap)
        start = (n//2)-1
        for i in range(start , -1 , -1):
            self.__heapifyDown(i)


    # main mathods
    def insert(self , val):
        self.heap.append(val)
        self.__heapifyUp()
        
    # delete tha max value
    def delete(self): 
        data = self.heap[0]
        self.__swap(0 , len(self.heap)-1)
        del self.heap[len(self.heap)-1]
        self.__heapifyDown(0)


        return data





t = Heap()
t.build([5,10,11,15,2,3,20])
print(t.heap)


