from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        card_name = card.name
        for c in self.cards:
            if c.name == card_name:
                raise ValueError(f"Card {card_name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        for c in self.cards:
            if c.name == card:
                self.cards.remove(c)
                self.count -= 1

    def find(self, name: str):
        for c in self.cards:
            if c.name == name:
                return c
