import unittest
import intermediate


class IntermediateExercises(unittest.TestCase):

    def test_swap_with_valid_values(self):
        dict1 = dict(zip('abcdefghij'.split(), range(0, 10)))
        res = dict(zip(range(0,10), 'abcdefghij'.split()))
        self.assertEqual(intermediate.swap_kv(dict1), res)

    def test_swap_should_raise_error(self):
        dict1 = {'a': 1, 'b': 'c', 'z': [1, 2, 3]}
        try:
            intermediate.swap_kv(dict1)
        except Exception as e:
            self.assertTrue(type(e) is TypeError)

    def test_time_slow_should_return_value_from_function(self):

        @intermediate.time_slow
        def test_func():
            return sum(range(0, 2000))

        self.assertTrue(not (test_func() is None))

    def test_two_new_decks(self):
        deck1 = intermediate.Deck()
        deck2 = intermediate.Deck()
        self.assertEqual(deck1, deck2)

    def test_removing_first_card_len(self):
        deck = intermediate.Deck()
        len_before = len(deck)
        deck.draw_first_card()
        len_after = len(deck)
        self.assertGreater(len_before, len_after)

    def test_removing_first_card_remaining(self):
        deck = intermediate.Deck()
        card = deck.draw_first_card()
        self.assertTrue(card not in deck)

    def test_remove_random_card_len(self):
        deck = intermediate.Deck()
        len_before = len(deck)
        deck.draw_random_card()
        len_after = len(deck)
        self.assertGreater(len_before, len_after)

    def test_removing_random_card_remaining(self):
        deck = intermediate.Deck()
        card = deck.draw_random_card()
        self.assertTrue(card not in deck)

    def test_shuffle_deck(self):
        deck1 = intermediate.Deck()
        deck2 = intermediate.Deck()
        deck2.shuffle()
        self.assertNotEqual(deck1, deck2)

    def test_sort_deck(self):
        deck1 = intermediate.Deck()
        deck2 = intermediate.Deck()
        deck1.shuffle()
        deck2.shuffle()
        deck1.sort()
        deck2.sort()
        self.assertEqual(deck1, deck2)

    def test_add_card_len(self):
        deck = intermediate.Deck()
        initial_len = len(deck)
        card = deck.draw_random_card()
        after_draw_len = len(deck)
        deck.add_card(card)
        after_add_len = len(deck)
        self.assertTrue((initial_len == after_add_len) & (after_draw_len < initial_len))

    def test_add_card(self):
        deck = intermediate.Deck()
        card = intermediate.Card('TrapCard', 100)
        deck.add_card(card)
        self.assertTrue(card in deck)
