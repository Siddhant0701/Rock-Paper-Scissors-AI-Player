from gym import Env
from gym.spaces import Discrete, MultiDiscrete, Tuple
import numpy as np
from player import Player
import random

dict = {
    0: 'Rock',
    1: 'Paper',
    2: 'Scissors'
}


class RPSGameEnv(Env):

    '''A custom environment for the RPS game that can be used in the DQN algorithm'''

    def __init__(self, rounds_memory=5):
        self.action_space = Discrete(3)
        self.rounds_memory = rounds_memory
        self.observation_space = MultiDiscrete(np.array([[3 for _ in range(rounds_memory)] for _ in range(2)]))
        self.computer_player = Player('Computer')

        self.comp_history = np.zeros(rounds_memory)
        self.player_history = np.zeros(rounds_memory)

    def reset(self):
        self.comp_history = np.zeros(self.rounds_memory)
        self.player_history =  np.zeros(self.rounds_memory)
        return np.stack((self.comp_history, self.player_history))
    
    def step(self, action):
        choice = self.computer_player.play()

        self.comp_history = np.roll(self.comp_history, -1)
        self.player_history = np.roll(self.player_history, -1)

        self.comp_history[-1] = choice
        self.player_history[-1] = action

        if choice == action:
            reward = 0
        elif choice == 0 and action == 2:
            reward = 2
        elif choice == 1 and action == 0:
            reward = 2
        elif choice == 2 and action == 1:
            reward = 2
        else:
            reward = -2
        
        return np.stack((self.comp_history, self.player_history)), reward, False, {}


    def render(self):
        pass
