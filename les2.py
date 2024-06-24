class Birds():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f'{self.name} is flying')

    def eat(self):
        print(f'{self.name} is eating')

    def sing(self):
        print(f'{self.name} is singing - {self.voice}')

    def info(self):
        print(f'{self.name} - name')
        print(f'{self.voice} - voice')
        print(f'{self.color} - color')

class Pegeon(Birds):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def walk(self):
        print(print(f'{self.name} - walking'))


bird1 = Pegeon('golub','kurlyk','grey','podnojnyi korm')

bird1.sing()
bird1.info()
bird1.walk()