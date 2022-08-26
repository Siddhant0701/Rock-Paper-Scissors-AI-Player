from models.model import Model
from models.random import RandomModel


class RPSgame:
    def __init__(self, model, initMoves=0, initModel=RandomModel(), rounds=50, playerInput=""):
        self.model = model
        self.initMoves = initMoves
        self.initModel = initModel
        self.rounds = rounds if playerInput == "" else len(playerInput)

        self.roundsPlayed = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0

        self.playerInput = playerInput
        self.testMode = (playerInput != "")

    def start(self):
        self.gamePrint("Starting Game")

        for i in range(self.rounds):
            self.play_round()
            self.roundsPlayed += 1

        self.printPerformance()
        if(self.testMode):
            return ({"ratio" : self.wins / self.losses, "win" : self.wins, "loss" : self.losses, "tie" : self.ties, "rounds":self.roundsPlayed})
    
    def play_round(self):
        
        if(self.roundsPlayed <= self.initMoves):
            currentModel =self.initModel
        else:
            currentModel = self.model

        player_choice = self.get_input() if self.playerInput == "" else self.test_player_input()
        my_choice = currentModel.choose()

        if(self.roundsPlayed <= self.initMoves):
            self.initModel.update(player_choice)
        
        self.model.update(player_choice)

        self.gamePrint("You chose " + player_choice + " and I chose " + my_choice)
        self.gamePrint("")
        result = Model.getWinner(player_choice, my_choice)

        if(result == "Tie"):
            self.ties += 1
        elif(result == "Player Wins"):
            self.losses += 1
        elif(result == "Computer Wins"):
            self.wins += 1
        
        self.gamePrint(result)

    def gamePrint(self, s):
        if(not self.testMode):
            print(s)

    def printPerformance(self):
        self.gamePrint("Win Rate: " + str(self.wins *100 / self.roundsPlayed))
        self.gamePrint("Loss Rate: " + str(self.losses*100 / self.roundsPlayed))
        self.gamePrint("Tie Rate: " + str(self.ties*100 / self.roundsPlayed))
    
    def get_input(self):
        d = ["R", "P", "S"]
        self.gamePrint("Please enter your choice: R(1), P(2), or S(3)")
        x = input()
        while(x != "1" and x!="2" and x!="3"):
            self.gamePrint("Invalid input. Please enter your choice: R(1), P(2), or S(3)")
            x = input()
        return d[int(x) - 1]

    def test_player_input(self):
        x = self.playerInput[0]
        self.playerInput = self.playerInput[1:]
        return x
