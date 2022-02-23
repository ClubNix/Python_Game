import random
import math

class GuessNumber():
    def __init__(self, playerID : int):
        self.playerID = playerID
        self.number = 0
        self.tryCount = 0

    def chooseNumber(self, difficulty : int) -> None:
        if difficulty <= 0 or 4 <= difficulty:
            return

        self.number = random.randint(0, math.pow(10, difficulty+1))
        print(self.number)

    def guessTest(self, guess : int) -> None:
        if guess < self.number:
            print("It's more !")
        elif guess > self.number:
            print("It's less")
        else:
            return True

        self.tryCount -= 1
        return False
        

def main():
    game = GuessNumber(0)

    testInput = False
    hasWon = False
    difficultyInput = 0
    guess = 0

    while not testInput:
        try:
            difficultyInput = int(input("Choose your difficulty (1 / 2 / 3) : "))
            if 1 <= difficultyInput and difficultyInput <= 3:
                testInput = True
        except ValueError as _:
            pass

    game.chooseNumber(difficultyInput)

    while not hasWon:
        try:
            guess = int(input("Choose your guess : "))
        except ValueError as _:
            print("You must choose a number")
            continue

        if game.guessTest(guess):
            print(f"You won ! The number to guess was : {game.number}")
            break

if __name__ == "__main__":
    main()
