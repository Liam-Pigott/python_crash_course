import unittest
import blackjack

class TestBlackjack(unittest.TestCase):

    def test_deck_size(self):
        deck = blackjack.Deck()
        self.assertEqual(len(deck.deck), 52)
    
    def test_hand_value(self):
        hand = blackjack.Hand()
        hand.add_card(blackjack.Card('Two','Spades'))
        hand.add_card(blackjack.Card('King', 'Clubs'))
        self.assertEqual(hand.value, 12)

    def test_hand_with_aces(self):
        hand = blackjack.Hand()
        hand.add_card(blackjack.Card('Five', 'Diamonds'))
        hand.add_card(blackjack.Card('King', 'Clubs'))
        hand.add_card(blackjack.Card('Ace', 'Spades'))
        hand.adjust_for_aces()
        self.assertEqual(hand.value, 16)

if __name__ == '__main__':
    unittest.main()
