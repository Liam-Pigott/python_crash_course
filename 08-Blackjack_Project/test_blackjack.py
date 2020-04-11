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

    def test_win_bet(self):
        chip = blackjack.Chips()
        chip.bet = 42
        chip.win_bet()
        self.assertEqual(chip.total, 142)
    
    def test_win_bet_blackjack(self):
        chip = blackjack.Chips()
        chip.bet = 42
        chip.win_bet_blackjack()
        self.assertEqual(chip.total, 163)

    def test_win_bet_with_total(self):
        chip = blackjack.Chips(145)
        chip.bet = 42
        chip.win_bet()
        self.assertEqual(chip.total, 187)

    def test_lose_bet(self):
        chip = blackjack.Chips()
        chip.bet = 42
        chip.lose_bet()
        self.assertEqual(chip.total, 58)


if __name__ == '__main__':
    unittest.main()
