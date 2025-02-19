import random


class GuessNumberGame:
    def __init__(self):
        self.player1_name = ""
        self.player2_name = ""
        self.upper_limit = 0
        self.secret_number = 0

    def start_game(self):
        self.get_player_names()
        self.set_upper_limit()
        self.generate_secret_number()
        self.play()

    def get_player_names(self):
        self.player1_name = input("Гравець 1, введіть ваше ім'я: ")
        self.player2_name = input("Гравець 2, введіть ваше ім'я: ")

    def set_upper_limit(self):
        while True:
            try:
                self.upper_limit = int(input("Введіть верхню межу (число більше 0): "))
                if self.upper_limit <= 0:
                    raise ValueError("Число повинно бути більше 0.")
                break
            except ValueError as e:
                print(f"Помилка: {e}. Спробуйте ще раз.")

    def generate_secret_number(self):
        self.secret_number = random.randint(0, self.upper_limit)
        print(f"Число загадане в діапазоні від 0 до {self.upper_limit}. Починаємо гру!")

    def play(self):
        players = [self.player1_name, self.player2_name]
        turn = 0
        while True:
            print(f"Хід гравця {players[turn]}.")
            guess = self.get_guess_input()
            if guess == self.secret_number:
                print(f"Вітаю, {players[turn]}! Ви вгадали число!")
                break
            elif guess < self.secret_number:
                print("Моє число більше.")
            else:
                print("Моє число менше.")
            turn = 1 - turn

    def get_guess_input(self):
        while True:
            try:
                guess = int(input("Введіть ваше припущення: "))
                if guess < 0 or guess > self.upper_limit:
                    raise ValueError(f"Число повинно бути в діапазоні від 0 до {self.upper_limit}.")
                return guess
            except ValueError as e:
                print(f"Помилка: {e}. Спробуйте ще раз.")


if __name__ == "__main__":
    game = GuessNumberGame()
    game.start_game()