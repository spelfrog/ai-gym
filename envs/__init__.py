rom gym.envs.registration import register

register(
        id='Fuzzy-CartPole-v0',
        entry_point='envs.cartpole:FuzzyCartEnv',
        )

register(
        id='Wumpus-v0',
        entry_point='envs.wumpus:WumpusWorldEnv',
        )

