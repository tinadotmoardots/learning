msg = input("What's the secret password? ")
while msg != "bananas":
	print("WRONG!")
	msg = input("What's the secret password? ")
print("CORRECT")

num = 1
while num < 11:
	print(num)
	num += 2