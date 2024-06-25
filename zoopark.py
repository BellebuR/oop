import json


# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def eat(self):
        return f"{self.name} is eating."


# Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says 'Chirp!'"


class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} says 'Roar!'"


class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} says 'Hiss!'"


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    sounds = []
    for animal in animals:
        sounds.append(animal.make_sound())
    return sounds


# Классы сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"ZooKeeper {self.name} is feeding {animal.name}."


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"Veterinarian {self.name} is healing {animal.name}."


# Класс Zoo с композицией
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise ValueError("Invalid animal object")

    def add_staff(self, staff_member):
        if isinstance(staff_member, (ZooKeeper, Veterinarian)):
            self.staff.append(staff_member)
        else:
            raise ValueError("Invalid staff member object")

    def save_to_file(self, filename):
        data = {
            "animals": [{"type": type(an).__name__, "name": an.name, "age": an.age} for an in self.animals],
            "staff": [{"type": type(st).__name__, "name": st.name} for st in self.staff]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.animals = []
            self.staff = []
            for an in data['animals']:
                if an['type'] == 'Bird':
                    self.animals.append(Bird(an['name'], an['age']))
                elif an['type'] == 'Mammal':
                    self.animals.append(Mammal(an['name'], an['age']))
                elif an['type'] == 'Reptile':
                    self.animals.append(Reptile(an['name'], an['age']))
            for st in data['staff']:
                if st['type'] == 'ZooKeeper':
                    self.staff.append(ZooKeeper(st['name']))
                elif st['type'] == 'Veterinarian':
                    self.staff.append(Veterinarian(st['name']))

# Пример использования
if __name__ == "__main__":
    # Создание животных
    bird = Bird("Tweety", 2)
    mammal = Mammal("Simba", 5)
    reptile = Reptile("Slinky", 3)

    # Демонстрация полиморфизма
    print(animal_sound([bird, mammal, reptile]))

    # Создание сотрудников
    keeper = ZooKeeper("John")
    vet = Veterinarian("Dr. Smith")

    # Создание зоопарка и добавление животных и сотрудников
    zoo = Zoo()
    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Сохранение состояния зоопарка в файл
    zoo.save_to_file("zoo_data.json")

    # Создание нового зоопарка и загрузка данных из файла
    new_zoo = Zoo()
    new_zoo.load_from_file("zoo_data.json")

    # Проверка загруженных данных
    for animal in new_zoo.animals:
        print(f"Loaded animal: {animal.name}, Age: {animal.age}, Sound: {animal.make_sound()}")
    for staff in new_zoo.staff:
        print(f"Loaded staff: {staff.name}, Type: {type(staff).__name__}")