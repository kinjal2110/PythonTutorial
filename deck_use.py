import deck


def create_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')

    return deck
    cards = deck.create_deck()

    for card in cards:
     print(card)


