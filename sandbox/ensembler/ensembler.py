from strategy import *


class Ensembler:
    def __init__(self, scoring_decay=0.6):
        self.strategies = [Random(), LastMove(), Frequency(), Sequence(), WeightedSum()]

        self.scores = np.array([1,0,0,0,0])
        self.last_predictions = np.zeros(5,5)

        self.current_accuracy = 0
        self.accuracy = []
        self.games_played = 0

        self.player_history = []
        self.model_history = []
        self.results_history = []

        self.total_wins = 0
        self.total_losses = 0
        self.total_draws = 0
    
    def predict(self):
        results = np.array([0,0,0])
    
        for i in range(len(self.strategies)):
            if(self.weights[i] >0):
                choice = self.strategies[i].predict()
                results[choice] += self.scores[i]
                self.last_predictions[i] = choice

        return np.argmax(results)
                


