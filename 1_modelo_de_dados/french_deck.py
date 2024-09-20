import collections

from random import choice


# Definição de uma classe básica usando namedtuple, para representar apenas uma carta.
Card = collections.namedtuple("Card", ["rank", "suit"])


# Definição de uma classe para comportar o baralho de cartas.
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    teste_card = Card("4", "clubs")
    print(teste_card)

    deck = FrenchDeck()
    print("\nTamanho do baralho: ", len(deck))
    print("Primeira carta: ", deck[0])
    print("Ultima Carta: ", deck[-1])
    print("Carta aleatória: ", choice(deck))
    print("deck[:3] = ", deck[:3])
    print("deck[12::13] = ", deck[12::13])
    # print("reversed = ", list(reversed(deck)))

    card_in_deck = Card("Q", "spades") in deck
    print("spades Q in deck?", card_in_deck)
