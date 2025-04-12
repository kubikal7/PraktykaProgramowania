class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""

        minus_result = self.p1points - self.p2points  #zmiana
        if minus_result == 0:  #zmiana
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4:
            if minus_result == 1:
                result = "Advantage "+self.player1_name  #
            elif minus_result == -1:
                result = "Advantage "+self.player2_name  #
            elif minus_result >= 2:
                result = "Win for "+self.player1_name  #
            else:
                result = "Win for "+self.player2_name  #
        else:
            temp_score = 0  #
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.p1points
                else:
                    result += "-"
                    temp_score = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result
