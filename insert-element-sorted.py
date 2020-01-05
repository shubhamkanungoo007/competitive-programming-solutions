

def insert(list, n): 
	
	# Searching for the position 
	for i in range(len(list)): 
		if list[i] > n: 
			index = i 
			break
	
	# Inserting n in the list 
	list = list[:i] + [n] + list[i:] 
	return list

# Driver function 
list = [1, 2, 4,5,7] 
n = int(input())

print(insert(list, n)) 

