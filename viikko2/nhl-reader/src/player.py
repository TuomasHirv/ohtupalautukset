"""Tässä moduulissa luodaan player olioita"""
class Player:
    """Luodaan luokka player"""
    def __init__(self, tiedot):
        self.name = tiedot['name']
        self.nation = tiedot['nationality']
        self.team = tiedot['team']
        self.goals = tiedot['goals']
        self.assists = tiedot['assists']
        self.points = self.goals + self.assists

    def __str__(self):
        return (self.name + " team " + self.team + " " + str(self.goals)
                + " + " + str(self.assists) + " = " + str(self.points))

    def luotu_functio_pylintille(self):
        """Tämä luotiin vain jotta pylint ei valita siitä"""
        return self.name ++ self.nation
