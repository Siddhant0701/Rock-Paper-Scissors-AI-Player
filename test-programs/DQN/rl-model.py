import game_env

env = game_env.RPSGameEnv()
env.reset()

episodes = 10
for i in range(episodes):
    state = env.reset()
    done = False

    score = 0

    for i in range(50):
        action = env.action_space.sample()
        next_state, reward, done, info = env.step(action)
        score += reward

    print(f'Score: {score}')

