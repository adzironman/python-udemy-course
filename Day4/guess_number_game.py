from random import randint

class GuessingGame:
    def __init__(self, attempts=8):
        self.attempts = attempts
        self.number_to_guess = randint(0, 100)
        self.user_name = ""
        print(f"DEBUGGING: number_to_guess: {self.number_to_guess}")  # For debugging

    def greet_user(self):
        self.user_name = input("Hello there! What's your name? ")
        print(f"""Nice to meet you, {self.user_name}.
Let's play a game!
Your task is to guess the number from 0 to 100. You have {self.attempts} attempts.""")

    def check_number(self, number):
        number = int(number)
        if number > 100 or number < 0:
            print("Your number is out of play. Try again!")
        elif number < self.number_to_guess:
            print("Your number is smaller than the number to guess.")
        elif number > self.number_to_guess:
            print("Your number is higher than the number to guess.")
        elif number == self.number_to_guess:
            print(f"Congratulations {self.user_name}, you guessed the number!")
            return True
        return False

    def play(self):
        self.greet_user()
        while self.attempts > 0:
            try:
                user_guess = int(input(f"What is your guess? You have {self.attempts} attempts left: "))
                if self.check_number(user_guess):
                    break
                self.attempts -= 1
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print(f"Sorry {self.user_name}, you lost! The number was {self.number_to_guess}.")

# Run the game
if __name__ == "__main__":
    game = GuessingGame()
    game.play()