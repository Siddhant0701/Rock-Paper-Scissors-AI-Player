import itertools
from model import Model


class Transitions:
    def __init__(self, name, decay):
        self.name = name
        
        self.total = 0
        self.decay = decay

        self.transitions = {"R" : {"prob": 1/3, "total":0}, 
                            "P" : {"prob": 1/3, "total":0}, 
                            "S" : {"prob": 1/3, "total":0}}
    
    def __str__(self):
        s = ""
        for i in self.transitions:
            s += self.name + i + ": " + str(self.transitions[i]["prob"]) + "\n"
        return s

    def choose_transition(self):
        return max(self.transitions, key = lambda x : self.transitions[x]["prob"])
    
    def update(self, choice):

        for i in self.transitions:
            self.transitions[i]["total"] *= self.decay
        self.total *= self.decay
        self.transitions[choice]["total"] += 1
        self.total += 1

        for i in self.transitions:
            if (self.transitions[i]["total"] != 0):
                self.transitions[i]["prob"] = self.transitions[i]["total"] / self.total
    

class MarkovModel(Model):
    def __init__(self, length, decay=1.0, history_limit=20):
        super().__init__(history_limit)
        
        self.length = length
        self.decay = decay
        self.states = [''.join(i) for i in itertools.product('RPS', repeat=length)]
        self.transitions = {}
        self.currentState = ""

        for i in self.states:
            self.transitions[i] = Transitions(i, decay)
    
    def __str__(self):
        s = "Current State: " + self.currentState + "\n"
        for i in self.transitions:
            s += i + ": " + str(self.transitions[i]) + "\n"
        return s
    
    def predict(self):
        return self.transitions[self.currentState].choose_transition()
    
    def update(self, choice):
        super().update(choice)

        if(len(self.history) <= self.length):
            self.currentState = ''.join(self.history)
        else:
            self.transitions[self.currentState].update(choice)
            self.currentState = ''.join(self.history[-self.length:])




