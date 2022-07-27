from os import stat_result


class Model:
    def __init__(self, historyLimit=20):
        self.history = []
        self.historyLimit = historyLimit

        self.winDict = {"R" : "P", "P" : "S", "S" : "R"}
        self.lossDict = {"R" : "S", "P" : "R", "S" : "P"}

    def __str__(self):
        pass

    def update(self, choice):
        self.history.append(choice)
        if (len(self.history) > self.historyLimit):
            self.history.pop(0)
    
    def predict(self):
        pass

    def choose(self):
        return self.winDict[self.predict()]
    
    @staticmethod
    def getWinner(player, computer):
        winDict = {"R" : "P", "P" : "S", "S" : "R"}
        
        if (player == computer):
            return "Tie"
        elif (player == winDict[computer]):
            return "Player Wins"
        else:
            return "Computer Wins"
