from collections.abc import Hashable
from collections import namedtuple
from random import choice,shuffle
import time


def swap_kv(dict1):
    res = {}
    for k, v in dict1.items():
        if not issubclass(type(v), Hashable):
            raise TypeError('{0} is not hashable'.format(v))
        else:
            res[v] = k
    return res


def time_slow(func):

    def how_fast():
        start = time.time()
        res = func()
        stop = time.time()
        delta_millis = (stop - start)*1000
        print('The execution of the function {0} took {1} milliseconds'.format(func.__name__, delta_millis))
        return res

    return how_fast


Card = namedtuple('Card', 'suite rank')


class Deck:
    ranks = list(range(2, 11)) + 'A K Q J'.split()
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self._cards = [Card(suite, rank) for suite in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __str__(self):
        return ', '.join([str(card) for card in self._cards])

    def __iter__(self):
        return (card for card in self._cards)

    def __setitem__(self, position, card):
        self._cards[position] = card

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for index, card in enumerate(self):
            if other[index] != card:
                return False
        return True

    def shuffle(self):
        shuffle(self)

    def sort(self):
        self._cards.sort(key=lambda card: self.suits.index(card.suite)*13 + self.ranks.index(card.rank))

    def add_card(self, card):
        self._cards.append(card)
        self.shuffle()

    def draw_first_card(self):
        return self._cards.pop(0)

    def draw_random_card(self):
        card = choice(self)
        index = self._cards.index(card)
        self._cards.pop(index)
        return card


if __name__ == '__main__':

    @time_slow
    def test():
        return sum(range(0, 8930))

    deck = Deck()
    print(deck)
    shuffle(deck)
    print(deck)

    print(choice(deck))
    deck.sort()
    print(deck)
    d2 = Deck()
    d2.sort()
    print(d2)
    print(deck == d2)
    # print(test())
    # print(swap_kv({'b':1,'c':2,'a':[1,2]}))
