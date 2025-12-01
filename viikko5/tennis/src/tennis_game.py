class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        
        self.match_point = 4
        self.zero_points_text = "Love"
        self.one_points_text = "Fifteen"
        self.two_points_text = "Thirty"
        self.three_points_text = "Forty"
        self.match_point_tie_text = "Deuce"

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score_information = ""
        if self.player1_score == self.player2_score:
            score_information = self.text_for_tasatilanne()
        elif self.player1_score >= self.match_point or self.player2_score >= self.match_point:
            score_information = self.text_for_advantage()
        else:
            score_information = self.normal_score_text()
        return score_information

    def text_for_tasatilanne(self):
        return_text = ""
        if self.player1_score == 0:
            return_text = self.zero_points_text+"-All"
        elif self.player1_score == 1:
            return_text = self.one_points_text+"-All"
        elif self.player1_score == 2:
            return_text = self.two_points_text+"-All"
        else:
            return_text = self.match_point_tie_text
        return return_text
        
    def text_for_advantage(self):
        return_text = ""
        advantage = self.player1_score - self.player2_score
        if advantage == 1:
            return_text = "Advantage "+self.player1_name
        elif advantage == -1:
            return_text = "Advantage "+self.player2_name
        elif advantage >= 2:
            return_text = "Win for "+self.player1_name
        else:
            return_text = "Win for "+self.player2_name
        return return_text
    def normal_score_text(self):
        return_text = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                return_text = return_text + "-"
                temp_score = self.player2_score
            if temp_score == 0:
                return_text = return_text + self.zero_points_text
            elif temp_score == 1:
                return_text = return_text + self.one_points_text
            elif temp_score == 2:
                return_text = return_text + self.two_points_text
            elif temp_score == 3:
                return_text = return_text + "Forty"
        return return_text

