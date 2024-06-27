from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


### Шаг 2: Реализация конкретных типов оружия


class Sword(Weapon):
    def attack(self):
        return "удар мечом"


class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"


### Шаг 3: Модификация класса Fighter


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon = weapon
        else:
            raise ValueError("Invalid weapon type")

    def attack(self):
        if self.weapon:
            return f"{self.name} наносит {self.weapon.attack()}."
        else:
            return f"{self.name} не вооружен."


### Шаг 4: Реализация боя


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} побежден!"
        else:
            return f"У {self.name} осталось {self.health} здоровья."


# Пример использования

if __name__ == "__main__":
    # Создание бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster("Монстр", 10)

    # Выбор меча для бойца
    sword = Sword()
    fighter.changeWeapon(sword)
    print(fighter.attack())
    print(monster.take_damage(10))

    # Выбор лука для бойца
    bow = Bow()
    fighter.changeWeapon(bow)
    print(fighter.attack())
    print(monster.take_damage(10))