import random

random_number = random.randint(1,10)

# guess = input("Pick a number from 1-10! ")
# guess = int(guess)

# if guess == random_number:
# 	print("You win! Have a cookie :)")

# elif (guess) > random_number:
# 	print("Too high, try again")

# else:
# 	print("Too low, try again")

# print(random_number)

guess = None

while True:
	guess = input("Pick a number from 1-10! ")
	guess = int(guess)
	if guess < random_number:
		print("Too low :(")
	elif guess > random_number: 
		print("Too high :(")
	else: 
		print("You win! Have a cookie :)")
		play_again = input("Do you want to play again? y/n ")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thanks for playing!")
			break
	
