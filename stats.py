class Stats():
    # statistic
    def __init__(self):
        # init statistic
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        # statisitc changes in game time
        self.guns_left = 2
        self.score = 0
