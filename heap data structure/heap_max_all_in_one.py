class MaxHeap:
	def __init__(self , arr):
		self.heap = arr

	# swap two node 
	def __swap(self , i , j): self.heap[i] , self.heap[j] = self.heap[j] , self.heap[i]

	# heapify the list
	def __heapifyDown(self , i , length = None):
		# parametar i is the starting point
		# parametar length is the sroping point
		if length is None: length = len(self.heap)
		
		left_child = (2*i)+1
		right_child = (2*i)+2
		max = i

		if left_child < length and self.heap[left_child] > self.heap[i]: max = left_child
		if right_child < length and self.heap[right_child] > self.heap[max]: max = right_child

		if i != max:
			if self.heap[max] > self.heap[i]:
				self.__swap(i , max)
				self.__heapifyDown(max , length)

	# build a unsorted arr
	def __build(self):
		for i in range((len(self.heap)//2) -1 , -1, -1):
			self.__heapifyDown(i)

	# sort the hole array
	def heap_sort(self):
		self.__build()
		for i in range(len(self.heap)-1 , 0, -1):
			self.__swap(i , 0)
			self.__heapifyDown(0 , i)


t = MaxHeap([5,10,11,15,2,3,20])
t.heap_sort()
print(t.heap)

