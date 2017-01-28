
class Hero:
    def __init__(self, name, health=100):
        self.name = name # the property that the class have.
        self.health = health

    def __str__(self):
        return "Hero {}, health at {}.".format(self.name, self.health)

    def eat(self, food):
        if food == 'apple':
            self.health += 20
        elif food == "fried chicken":
            self.health -= 50

    def __add__(self, other):
        return self.health + other.health

class Fruit:
    def __init__(self):
        pass

superman = Hero("Superman")
print(superman)
superman.eat("apple")
print(superman)

batman = Hero("Batman")
batman.eat("fried chicken")
print(batman)

print("abc" + "def")
print(superman + batman)
print(type(batman))

heros = [superman, batman] #creating a list of Hero objects
print(heros)

for hero in heros:
    hero.eat("apple")
    print(hero)