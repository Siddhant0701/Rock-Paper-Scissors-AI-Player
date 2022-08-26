from model import Model
import random

class RandomModel(Model):
    def __init__(self, historyLimit=20):
        super().__init__(historyLimit)
    
    def __str__(self):
        return "Random Model"
    
    def predict(self):
        return random.choice(["R", "P", "S"])
    
    def update(self, choice):
        super().update(choice)
