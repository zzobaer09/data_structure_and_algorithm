class Hashing:
	
	def __init__(self , size) -> None:
		self.size = size
		self.arr = [None]*self.size
	
	def hash(self , key):
		# * the hash function

		#! think easy :) 
		key = str(key)
		
		h1 = ""
		h2 = ""

		j = 0
		for i in key:
			if j < 2:
				h1 += str(ord(i))
				j+=1
		
		j = 0
		for i in reversed(key):
			if j < 2:
				h2 += str(ord(i))
				j+=1
		h1 = int(h1) % self.size
		h2 = int(h2) % self.size
		sumh = (h1 + h2) % self.size
		return sumh


	
	def append(self , key , val):
		# * add a value with key

		indx = self.hash(key)

		if self.arr[indx] == None: self.arr[indx] = [[key , val]]
		else:
			for i in self.arr[indx]:
				if i[0] == key: 
					i[1] = val
					return
			
			self.arr[indx].append([key , val])
	
	def pop(self , key):
		# * delete a value
		
		key = str(key)
		indx = self.hash(key)

		if len(self.arr[indx]) == 1:
			del self.arr[indx][0]
			self.arr[indx] = None
		else:
			for i in range(len(self.arr[indx])):
				if self.arr[indx][i][0] == str(key):
					
					del self.arr[indx][i]
					break
	
	def get(self , key):
		key = str(key)
		indx = self.hash(key)

		try:
			if len(self.arr[indx]) == 1: return self.arr[indx][0][1]
			else:
					for i in range(len(self.arr[indx])):
						if self.arr[indx][i][0] == key: return self.arr[indx][i][1]
		except: return None

		 


	

				



		



h = Hashing(10)
# print(h.arr)

h.append("1" , "zobaer")
h.append("11" , "world")
h.append("111" , "hello")
h.append("2" , "Sumu")

# print(h.arr)

print(h.get(111))

