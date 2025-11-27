arthur = lambda x: x.join('a')
print(arthur('Jonas.'))


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

def soma(x, y):
    print(x + y)

soma(1, 2)