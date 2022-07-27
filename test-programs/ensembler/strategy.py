from os import lstat
from random import randint
from keras.utils import to_categorical
import numpy as np

# Calculates the winner against 'n'
def win(n):
    return (n+1)%3

# Calculates the loser against 'n'
def lose(n):
    return (n+2)%3


class Strategy:
    def __init__(self, player_history=[], computer_history=[], results_history=[], memory_size=50):
        self.player_history = player_history
        self.computer_history = computer_history
        self.results_history = results_history
        self.memory_size = memory_size

    def predict(self):
        pass
    
    def update(self, player_choice, computer_choice, result):
        self.player_history.append(player_choice)
        self.computer_history.append(computer_choice)
        self.results_history.append(result)
        if len(self.player_history) > self.memory_size:
            self.player_history.pop(0)
            self.computer_history.pop(0)
            self.results_history.pop(0)


# Model 0: Random
'''Randomly chooses between rock, paper, or scissors.'''
class Random(Strategy):
    def __init__(self, player_history=[], computer_history=[], results_history=[]):
        super().__init__(player_history, computer_history, results_history)

    def predict(self):
        return randint(0, 2)
    
    

# Model 1: Last Move
'''Chooses the move that beats the last move. This is the most common strategy without too many parameters.'''
class LastMove(Strategy):
    def __init__(self, player_history=[], computer_history=[], results_history=[]):
        super().__init__(player_history, computer_history, results_history)

    def predict(self):
        return lose(self.player_history[-1])


# Model 2: Frequency
'''Chooses the move that beats the least frequent move of the opponent.'''
class Frequency(Strategy):
    def __init__(self, player_history=[], computer_history=[], results_history=[], moves=5):
        super().__init__(player_history, computer_history, results_history)
        self.moves = moves

    def predict(self):
        bins = np.array([0, 0, 0])
        
        for i in range(len(self.player_history[-self.moves:])):
            bins[self.player_history[i]] += 1

        return win(np.argmax(bins))
        

# Model 3: Sequence
'''Chooses a move if the opponent is displaying a certain sequence of moves.'''
class Sequence(Strategy):
    def __init__(self, player_history=[], computer_history=[], results_history=[], moves=5):
        super().__init__(player_history, computer_history, results_history)
        self.moves = moves

    def predict(self):

        bins = [0,0,0]
        last_move = self.player_history[-1]
        relevant_history = self.player_history[-self.moves:]
        for i in range(len(relevant_history)-1):
            if(relevant_history[i] == last_move):
                bins[self.player_history[i+1]] += 1

        return win(np.argmax(np.array(bins))) 

# Model 4: Weighted sum of last n moves
'''Calculates a weighted sum and the results and players moves decaying over the last n moves.'''
class WeightedSum(Strategy):
    def __init__(self, player_history=[], computer_history=[], results_history=[], decay=0.8, moves=7):
        super().__init__(player_history, computer_history, results_history)
        self.decay = decay
        self.moves = moves

    def predict(self):
        relevant_history = to_categorical(self.player_history[-self.moves:], num_classes=3)
        relevant_results = self.results_history[-self.moves:]

        prod = np.array([i*j for i, j in zip(relevant_history, relevant_results)])
        final = [i*(self.decay**(self.moves - j)) for j, i in enumerate(prod)]
        final = np.sum(final, axis=0)

        return win(np.argmax(final))

