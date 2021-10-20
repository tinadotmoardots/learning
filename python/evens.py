def generate_evens():
	result = []
	for i in range(50):
		if i % 2 == 0:
			result.append(i)
	return result