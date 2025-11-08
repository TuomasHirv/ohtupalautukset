class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nation = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists
    
    def __str__(self):
        return (self.name + " team " + self.team + " " + str(self.goals) + " + " + str(self.assists) + " = " + str(self.points))
