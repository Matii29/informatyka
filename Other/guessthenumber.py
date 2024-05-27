import random

class GuessingGame:
    
    _min_number = 1
    _max_number = 100

    def __init__(self):
        self._target_number = random.randint(self._min_number, self._max_number)
        self._attempts = 0

    def guess(self, number):
        self._attempts += 1

        if number < self._target_number:
            return "Too low!"
        
        elif number > self._target_number:
            return "Too high!"
        
        else:
            return "Congratulations! You've guessed the number!"

    @classmethod

    def set_range(cls, min_number, max_number):
        cls._min_number = min_nubmber

        cls._max_number = max_numer

        print(f"Number range is now set from {cls._min_number} to {cls._max_number}")

    @staticmethod

    def validate_input(number):
        if not isinstance(number, int):

            raise ValueError("The guess must be an integer.")
        
        if number < GuessingGame._min_number or number > GuessingGame._max_number:

            raise ValueError(f"The guess must be between {GuessingGame._min_number} and {GuessingGame._max_number}.")

def play_game():
    game = GuessingGame()

    print("Welcome to the Guessing Game!")

    print(f"Guess the number between {GuessingGame._min_number} and {GuessingGame._max_number}")

    while True:

        try:

            user_input = input("Enter your guess: ")

            guess = int(user_input)

            GuessingGame.validate_input(guess)

            result = game.guess(guess)

            print(result)

            if result == "Congratulations! You've guessed the number!":

                print(f"It took you {game._attempts} attempts.")

                break

        except ValueError as e:

            print(e)

play_game()