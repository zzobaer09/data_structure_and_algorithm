def bubble(arr):


	len_of = len(arr) - 1
	bool_F = False


	while not bool_F:
		bool_F = True

		for i in range(0 , len_of):

			if arr[i] > arr[i+1]:
				bool_F = False
				arr[i] , arr[i+1] = arr[i+1] , arr[i]


	return arr





print(bubble([10 , 5 , 3 ,6 , 4 , 6]))