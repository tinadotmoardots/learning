# This is a version of rock, paper, scissors that you can plan against a computer opponent
import random


print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Make your move: ")

rand_num = random.randint(0,2)

if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"




p = "You win!"

t = "It's a tie!"

c = "Computer wins!"

if player == computer:
	print(t)
elif player == "rock":
	if computer == "scissors":
		print(p)
	elif computer == "paper":
		print(c)
elif player == "paper":
	if computer == "rock":
		print(p)
	elif computer == "scissors":
		print(c)
elif player == "scissors":
	if computer == "rock":
	 	print(c)
	elif computer == "paper":
 		print(p)
else:
	print("Something went wrong")

