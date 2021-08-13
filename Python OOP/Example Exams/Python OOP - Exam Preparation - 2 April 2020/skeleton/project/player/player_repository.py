from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        player_name = player.username
        for p in self.players:
            if p.username == player_name:
                raise ValueError(f"Player {player_name} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        for p in self.players:
            if p.username == player:
                self.players.remove(p)
                self.count -= 1

    def find(self, username: str):
        for p in self.players:
            if p.username == username:
                return p
