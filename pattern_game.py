import numpy as np
import random

class PatternGame():
	def __init__(self, playerID : int):
		self.playerID = playerID
		self.tab = [[0,0,0],[0,0,0],[0,0,0]]
		self.generatePattern()

	def __str__(self) -> str:
		res = "|-----------|\n"
		for i in range(3):
			for j in range(3):
				res+= f"| {self.tab[i][j]} "
			res += "|\n"
			res += "|-----------|\n"
		return res

	def generatePattern(self):
		while self.hasWon():
			for _ in range(random.randint(10, 15)):
				self.chooseSquare(random.randint(0, 2), random.randint(0, 2))

	def hasWon(self):
		for i in range(3):
			for j in range(3):
				if self.tab[i][j] == 1:
					return False
		return True

	def chooseSquare(self, x : int, y : int):
		if (x < 0 or 2 < x) or (y < 0 or 2 < y):
			return

		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if (i < 0 or 2 < i) or (j < 0 or 2 < j):
					continue

				if self.tab[i][j] == 0:
					self.tab[i][j] = 1
				else:
					self.tab[i][j] = 0

	def toTuple(self, index : int) -> tuple:
		if index == 1:
			return (0,0)
		if index == 2:
			return (0,1)
		if index == 3:
			return (0,2)
		if index == 4:
			return (1,0)	
		if index == 5:
			return (1,1)
		if index == 6:
			return (1,2)
		if index == 7:
			return (2,0)
		if index == 8:
			return (2,1)
		if index == 9:
			return (2,2)
		return (-1,-1)

def main():
	exemple = "1 2 3\n4 5 6\n7 8 9\n"
	inputUser = 0
	testInput = False
	game = PatternGame(0)
	
	while not game.hasWon():
		print(game)
		print(exemple)

		while not testInput:
			try:
				inputUser = int(input("Choose a number between 1 and 9 : "))
				if 1 <= inputUser and inputUser <= 9:
					testInput = True
			except ValueError as _:
				pass

		choice = game.toTuple(inputUser)
		game.chooseSquare(choice[0], choice[1])
		testInput = False
	
	print(game)
	print("\nCongratulations, you won !")

if __name__ == "__main__":
	main()