import random

#card attributes
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#control variable
playing = True

#Main classes
class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        deck_state = ''
        for card in self.deck:
            deck_state += '\n' + card.__str__()
        return "The deck state is:" + deck_state

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
    

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        card_string = 'You have the following cards in your hand:'
        for card in self.cards:
            card_string += '\n' + card.__str__()
        return card_string

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_aces()

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def win_bet_blackjack(self):
        self.total += round(self.bet * 1.5)

    def lose_bet(self):
        self.total -= self.bet
 
#helper functions
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("You have {} chips, how many chips would you like to bet?".format(chips.total)))
        except:
            print("Sorry, please provide an integer")
        else:
            if(chips.bet > chips.total):
                print("Sorry, you don't have enough chips. You have {}".format(chips.total))
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Your score is {}. Hit or stand? Enter h or s '.format(hand.value))
        if x[0].lower() == 'h':
            hit(deck, hand)
            if hand.value == 21:
                break
        elif x[0].lower:
            print('Player stands, dealers turn')
            playing = False
        else:
            print('Please enter a valid command (h or s)')
            continue
        break

def show_some(player,dealer):
    print("Dealers Hand with one card hidden!")
    print(dealer.cards[1])
    print("\n")
    print("Players hand:")
    for card in player.cards:
        print(card)
    print("\n")
    
def show_all(player,dealer):
    print("Dealers Hand:")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Players hand:")
    for card in player.cards:
        print(card)
    print("\n")

def player_busts(player, dealer, chips):
    print("Player goes bust!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def player_blackjack(player, dealer, chips):
    print("BLACKJACK!")
    chips.win_bet_blackjack()

def dealer_busts(player, dealer, chips):
    print("Dealer goes bust! Players wins the bet.")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print("Dealer wins! Player loses the bet")
    chips.lose_bet()
    
def push(player, dealer):
    print("Player and dealer have tied, PUSH")



# Main game
def start_game():
    global playing
    player_chips = Chips()
    while True:
        print("Welcome to Blackjack!")

        #take bet
        take_bet(player_chips)

        # Set up deck and player/dealer hands
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        if player_hand.value == 21 and dealer_hand != 21:
            player_blackjack(player_hand, dealer_hand, player_chips)
            continue

        #show initial state with one dealer card hidden
        show_some(player_hand, dealer_hand)

        while playing:
            #player prompt to hit or stand
            hit_or_stand(deck, player_hand)

            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        print("Player total chips: {}".format(player_chips.total))
        if player_chips.total <= 0:
            new_game = input("You've ran out of chips! Would you like to start over? (y/n)")
            if new_game[0].lower() == "y":
                player_chips = Chips()
                playing = True
                continue
            else:
                print("Thank you for playing!")
                break
        
        new_game = input("Would you like to play another hand? y/n")

        if new_game[0].lower() == "y":
            playing = True
            continue
        else:
            print("Thank you for playing!")
            break

# Set methods that should only be executed when running this file here
if __name__ == '__main__':
    start_game()
