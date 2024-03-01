# for shuffling the deck
import random

# intialise all possible card values
card_rank = "23456789TJQKA"
# initalise all the suits (diamonds, clubs, hearts, spades)
suits = "dchs"
# intialise all 9 positions at the table
table_positions = ["BT", "SB", "BB", "UTG", "UTG + 1", "MP", "LJ", "HJ", "CO"]

# class for the card
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

# class for the deck
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in card_rank for suit in suits]
        random.shuffle(self.cards)

# class for the poker hand
class Hand:
    def __init__(self, cards):
        self.cards = cards

# create a board to input (preflop, flop, turn, or river)
def create_board():
    board = input("Board: ").upper().split(",")

# calculate the equity of all the hands against each other based on the board
def calculate_equity(hands, board):
    pass

# main function for executing poker equity percentages
def main():
    # take input of hands
    players = int(input("How many players are in this hand (2-9): "))
    if players < 2 or players > 9:
        exit()
        
    # to hold both the player's position and hand
    player = {}

    # input all hands of players that are playing this hand

    # create the board at the desired phase
    board = 

    # calculate the equity of the hands against each other
    hand_equity = 

    # print the equity layout of hands head to head

# main function error checking
if __name__ == "__main__":
    main()