from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == "Beginner":
            self.player_repository.add(Beginner(username))
        elif type == "Advanced":
            self.player_repository.add(Advanced(username))
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            self.card_repository.add(MagicCard(name))
        elif type == "Trap":
            self.card_repository.add(TrapCard(name))

    def add_player_card(self, username: str, card_name: str):
        card = [c for c in self.card_repository.cards if c.name == card_name]
        player = [p for p in self.player_repository.players if p.username == username]
        if card and player:
            card = card[0]
            player = player[0]
            player.card_repository.add(card)
            return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = [p for p in self.player_repository.players if p.username == attack_name]
        enemy = [p for p in self.player_repository.players if p.username == enemy_name]
        if attacker and enemy:
            attacker = attacker[0]
            enemy = enemy[0]
            BattleField.fight(attacker, enemy)
            return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for player in self.player_repository.players:
            result += f"Username: {player.username} - Health: {player.health} - Cards {len(player.card_repository.cards)}\n"
            for card in player.card_repository.cards:
                result += f"### Card: {card.name} - Damage: {card.damage_points}\n"

        return result
