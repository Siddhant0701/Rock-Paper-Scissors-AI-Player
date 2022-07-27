from markovModel import MarkovModel
from game import RPSgame
import itertools

# decay = [i/10 for i in range(5,11)]
# length = [i for i in range(2,5)]

# for (d, l) in itertools.product(decay, length):
#     print(f"Decay = {d} Length = {l}")
#     RPSgame(MarkovModel(l, decay=d), initMoves=l, playerInput="RSPRSPRSPPSRPSPRPSSRPSSSPRSPSRRPRRSPSRPSSSPRSRRRPS").start()
#     print("\n\n")


RPSgame(MarkovModel(3, decay=0.7), initMoves=3, rounds=100).start()
