from random import randint


class Player:
    def __init__(self, name, strategy='random'):
        self.name = name
        self.strategy = strategy

    def play(self):
        choice = randint(0, 2)
        return choice

    def __str__(self):
        return f'{self.name}'
