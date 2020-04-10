import random

flag = True
while flag:
	number = input("Type a number for an upper bound: ")

	if number.isdigit():
		print("Let's play!")
		number = int(number)
		flag = False
	else:
		print("Invalid input! Try Again!")

secret = random.randint(1,number)


#######################

guess = None
#count = 1
loop = True
while loop:
	guess = input('Please type a integer between 1 and ' + str(number) + ": ")
	if guess.isdigit():
		guess = int(guess)
		loop = False
	else:
		print("Invalid input! Try Again!")

while guess != secret:
#	guess = input('Please type a number between 1 and ' + str(number) + ": ")
#	if guess.isdigit():
#		guess = int(guess)
	if guess < secret:
		guess = input('Too low! Guess again: ')
		if guess.isdigit():
			guess = int(guess)
		else:
			print("Invalid input! Try Again!")
	elif guess > secret:
		guess = input('Too high! Guess again: ')
		if guess.isdigit():
			guess = int(guess)
		else:
			print("Invalid input! Try Again!")
	if guess == secret:
		print('You got it!')

#	else:
#		print('Please try again!')
#		count += 1

print("That's it! Would you like to play again? (yes/no)")