import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def value(self):
        return Card.ranks.index(self.rank)

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self):
        return self.hand.pop(0) if self.hand else None

    def collect_cards(self, cards):
        self.hand.extend(cards)

class WarGame:
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.deck = Deck()
        self.deal_cards()

    def deal_cards(self):
        while self.deck.cards:
            self.player1.hand.append(self.deck.deal())
            self.player2.hand.append(self.deck.deal())

    def play_round(self):
        card1 = self.player1.play_card()
        card2 = self.player2.play_card()
        if card1 and card2:
            print(f"{self.player1.name} plays {card1}, {self.player2.name} plays {card2}")
            if card1.value() > card2.value():
                self.player1.collect_cards([card1, card2])
                print(f"{self.player1.name} wins the round!")
            elif card1.value() < card2.value():
                self.player2.collect_cards([card1, card2])
                print(f"{self.player2.name} wins the round!")
            else:
                self.handle_war([card1, card2])

    def handle_war(self, war_cards):
        print("War!")
        war_pile = war_cards
        for _ in range(3):
            war_pile.append(self.player1.play_card())
            war_pile.append(self.player2.play_card())
        self.play_round()

    def is_game_over(self):
        return not self.player1.hand or not self.player2.hand

    def play_game(self):
        while not self.is_game_over():
            input("Press Enter to play a round...")
            self.play_round()
        winner = self.player1 if self.player1.hand else self.player2
        print(f"{winner.name} wins the game!")

# Example usage
game = WarGame("Player 1", "Player 2")
game.play_game()