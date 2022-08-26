import random

class Predictive_Models:

    def __init__(self):
        self.limit = 100
        self.score = 1
        self.recent_count = 5
        
        self.ai_history = []
        self.opponent_history = []
        self.results = []

        self.total = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0


    def update_history(self,ai_move, opponent_move, result):
        # Add given moves and result
        self.ai_history.append(ai_move)
        self.opponent_history.append(opponent_move)
        self.results.append(result)

        # Keeps list within memory limits by removing the oldest record
        if(len(self.ai_history) > self.limit):
            self.ai_history.pop(0)
            self.opponent_history.pop(0)
            self.results.pop(0)
        
        # Updates total stats
        if(len(self.ai_history) > self.recent_count):
            
            self.total += 1

            if(self.results[-1*(self.recent_count+1)] == 1):
                self.wins+=1

            elif(self.results[-1*(self.recent_count+1)] == 0):
                self.draws += 1

            else:
                self.losses += 1

    def update_scores(self, old_history_weight=0.2):
        old_accuracy = self.wins / self.total

        new_accuracy = self.results[-1*(self.recent_count):]
        squares = [i**2 for i in range(1,self.recent_count+1)]


