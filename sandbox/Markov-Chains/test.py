from game import RPSgame
from markovModel import MarkovModel

result = RPSgame(MarkovModel(2, decay=0.77), initMoves=2, rounds=100).start()
print(result)
