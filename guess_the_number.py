import random

class GuessNumber():
    def __init__(self, playerID : int):
        self.playerID = playerID
        self.number = 0
        self.tryCount = 0
        self.maxTry = 9

    def chooseNumber(self, difficulty : int) -> None:
        if difficulty <= 0 or 4 <= difficulty:
            return 

        self.number = random.randint(0, 500*difficulty)

    def guessTest(self, guess : int) -> bool:
        if guess < self.number:
            print("It's more !")
        elif guess > self.number:
            print("It's less")
        else:
            return True

        self.tryCount += 1
        return False

    def checkLose(self) -> bool:
        return self.tryCount == self.maxTry
        

def main():
    game = GuessNumber(0)

    testInput = False
    difficultyInput = 0
    guess = 0

    while not testInput:
        try:
            difficultyInput = int(input("Choose your difficulty \n1 : 0-500 \n2 : 0-1000 \n3 : 0-1500\n"))
            if 1 <= difficultyInput and difficultyInput <= 3:
                testInput = True
        except ValueError as _:
            pass

    game.chooseNumber(difficultyInput)

    while True:
        try:
            guess = int(input("Choose your guess : "))
        except ValueError as _:
            print("You must choose a number")
            continue

        if game.guessTest(guess):
            print(f"You won ! The number to guess was : {game.number}")
            print(game.tryCount)
            break
        
        elif game.checkLose():
            print(f"You lose ! The max try is {game.maxTry}... \nThe number to guess was {game.number}") 
            break

if __name__ == "__main__":
    main()