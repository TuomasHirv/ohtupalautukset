import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader.players)
    palautus = stats.top_scorers_by_nationality("FIN")

    for olio in palautus:
        print(olio)



class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []

        self.get_players()
    def get_players(self):
        response = requests.get(self.url).json()
        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

class PlayerStats:
    def __init__(self, lista):
        self.pelaajat = lista
    def top_scorers_by_nationality(self, nation):
        pelaajat = list(filter(lambda pel: pel.nation == nation, self.pelaajat))
        pelaajat = sorted(pelaajat, key=lambda pel:pel.points, reverse = True)
        return pelaajat

main()


#"name":"Max Crozier","nationality":"CAN","assists":0,"goals":0,"team":"TBL","games":5,"id":8481719