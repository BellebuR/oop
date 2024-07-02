import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Здоровье: {self.health}, Сила удара: {self.attack_power})"


class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра началась!")
        print(self.player)
        print(self.computer)
        print()

        turn = random.choice([self.player, self.computer])
        while self.player.is_alive() and self.computer.is_alive():
            if turn == self.player:
                self.player.attack(self.computer)
                turn = self.computer
            else:
                self.computer.attack(self.player)
                turn = self.player
            self.print_status()
            print()

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

    def print_status(self):
        print(self.player)
        print(self.computer)


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    computer_name = "Компьютерный герой"

    game = Game(player_name, computer_name)
    game.start()