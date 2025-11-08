"""Importataan requests ja player jotta voimme tehdä olioita"""
import requests
from player import Player

def main():
    """Koodi on pilkottu osiin mutta tässä se alkaa"""
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader.players)
    palautus = stats.top_scorers_by_nationality("FIN")

    for olio in palautus:
        print(olio)



class PlayerReader:
    """Luetaan tiedosto ja luodaan lista olioista"""
    def __init__(self, url):
        self.url = url
        self.players = []

        self.get_players()
    def get_players(self):
        """Tehdään luokan tehtävä tässä"""
        response = requests.get(self.url, timeout = 10).json()
        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)
    def place_holder(self):
        """pylint valittaa, että on liian vähän funktioita"""
        return self.players

class PlayerStats:
    """Tässä luetaan lista olioista ja niistä voi tehdä tilastoja"""
    def __init__(self, lista):
        self.pelaajat = lista
    def top_scorers_by_nationality(self, nation):
        """lista tietyn maalaisista ja se on sortattu pisteiden perusteella"""
        pelaajat = list(filter(lambda pel: pel.nation == nation, self.pelaajat))
        pelaajat = sorted(pelaajat, key=lambda pel:pel.points, reverse = True)
        return pelaajat
    def toka_place_holder(self):
        """koska muuten pylin valittaa"""
        return self.pelaajat

main()
