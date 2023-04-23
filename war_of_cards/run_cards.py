from cards import Card
from cards import Deck
from war_of_cards import suits, ranks, values



card_deck = Deck()
card_deck.shuffle_cards()
bottom_card = card_deck.all_cards[-1]
print(bottom_card)