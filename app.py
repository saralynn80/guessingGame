from random import randint

def guessingGame():
	guessesTaken = 0

	yourName = raw_input("What is your name?")

	number = randint(1,20)
	print 'Well, ' + yourName + ', I am thinking of a number between 1 and 20.'

	while guessesTaken < 6:
		yourGuess = raw_input("Take a guess!")
		yourGuess = int(yourGuess)
		guessesTaken = guessesTaken + 1

		if yourGuess > number:
			print "Too high, guess again!"
		elif yourGuess < number:
			print "Too low, guess again!"
		elif yourGuess == number:
			break
		else:
			print "Error! You should be here."


	if yourGuess == number:
		guessesTaken = str(guessesTaken)
		print "Great job, " + yourName + " you picked the number I was thinking in " + guessesTaken + " guesses!"
	elif yourGuess != number:
		number = str(number)
		print "Nope, You lose! The number I was thinking of was " + number

guessingGame()
