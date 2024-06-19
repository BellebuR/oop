class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f'{self.name} sleeping now')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} get eat')
        self.power += 3

    def hit(self):
        print(f'{self.name} hitting somebody')
        self.endurance -=1

    def walk(self):
        print(f'{self.name} walking')

    def info(self):
        print(f'Name - {self.name}')
        print(f'power - {self.power}')
        print(f'endurance - {self.endurance}')
        print(f'hair_color - {self.hair_color}')

war1 = Warrior(name='Petro',power=50, endurance=70, hair_color='violet')
war2 = Warrior(name='ivan',power=51, endurance=69, hair_color='green')

print(war1.endurance)
war1.sleep()
print(war1.endurance)

print(war1.info())