#  File: Poker.py

#  Description: Play poker with me

#  Student Name: Yilin Wen

#  Student UT EID: YW22559

#  Partner Name: Jiaxi Wang

#  Partner UT EID: JW53499

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 02/10/2022

#  Date Last Modified: 02/14/2022

import sys
import random


class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__(self, rank=12, suit='S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__(self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    # equality tests
    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class Deck (object):
    # constructor
    def __init__(self, num_decks=1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # deal a card
    def deal(self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

    # def __str__ (self):
    #     for card in self.deck:
    #         print(card, end= ' ')


class Poker (object):
    # constructor
    def __init__(self, num_players=2, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = []
        self.numCards_in_Hand = num_cards

        # deal the cards to the players
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.players_hands.append(hand)


    # simulate the play of poker
    def play(self):
        # print(self.players_hands)
        # sort the hands of each player and print
        for i in range(len(self.players_hands)):
            sorted_hand = sorted(self.players_hands[i], reverse=True)
            self.players_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)
        # print(self.players_hands)

        # determine the type of each hand and print

        # first make a list of all type-checking functions:
        func_check = [self.is_royal, self.is_straight_flush, self.is_four_kind, self.is_full_house, self.is_flush,
                      self.is_straight, self.is_three_kind, self.is_two_pair, self.is_one_pair, self.is_high_card]

        hand_type = []  # create a list to store type of hand
        hand_points = []  # create a list to store points for hand
        for hand in self.players_hands:
            for f in func_check:
                points, types = f(hand)
                if points != 0:
                    hand_type.append(types)
                    hand_points.append(points)
                    break

        # print results
        print()
        for i in range(len(self.players_hands)):
            print("Player {}: {}".format(i + 1, hand_type[i]))

        print()

        # zip the results
        result = list(zip(range(len(self.players_hands)), hand_type, hand_points))
        # determine winner and print
        result.sort(key=lambda x: x[2], reverse=True)
        # print(result)
        winners = []
        for r in result:
            if r[1] == result[0][1]:
                winners.append(r)

        if len(winners) == 1:
            print("Player {} wins.".format(winners[0][0] + 1))
        else:
            for w in winners:
                print("Player {} ties.".format(w[0] + 1))

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand

    def is_royal(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
        if (not same_suit):
            return 0, ''

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)
        if (not rank_order):
            return 0, ''

        points = self.calc_points(
            10, hand[0].rank, hand[1].rank, hand[2].rank, hand[3].rank, hand[4].rank)

        return points, 'Royal Flush'

    def is_straight_flush(self, hand):
        # check if is same suit
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
        if (not same_suit):
            return 0, ''

        # check if ranks are in sequence
        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == hand[0].rank - i)
        if (not rank_order):
            return 0, ''

        # calculate points and return
        points = self.calc_points(
            9, hand[0].rank, hand[1].rank, hand[2].rank, hand[3].rank, hand[4].rank)
        return points, 'Straight Flush'

    def is_four_kind(self, hand):
        # check if there are 4 of same rank:
        for i in range(len(hand)):
            if hand[4-i] == hand[3-i] and hand[3-i] == hand[2-i] and hand[2-i] == hand[1-i]:
                r_same = hand[4-i].rank
                r_side = hand[-i].rank
                return self.calc_points(8, r_same, r_same, r_same, r_same, r_side), 'Four of a Kind'

        # is no four of a kind
        return 0, ''

    def is_full_house(self, hand):
        # check if there are 3 of same rank:
        for i in range(len(hand)):
            if hand[4-i] == hand[3-i] and hand[3-i] == hand[2-i]:
                three_rank = hand[4-i].rank
                if hand[1-i] == hand[-i]:
                    two_rank = hand[-i].rank
                    return self.calc_points(7, three_rank, three_rank, three_rank, two_rank, two_rank), 'Full House'

        # is not full house
        return 0, ''

    def is_flush(self, hand):
        # check if the suits are the same
        same_rank = True
        for i in range(len(hand) - 1):
            same_rank = same_rank and hand[i].suit == hand[i+1].suit
        if same_rank:
            return self.calc_points(6, hand[0].rank, hand[1].rank, hand[2].rank, hand[3].rank, hand[4].rank), 'Flush'

        return 0, ''

    def is_straight(self, hand):
        # check if the ranks are in order:
        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == hand[0].rank - i)

        if rank_order:
            return self.calc_points(5, hand[0].rank, hand[1].rank, hand[2].rank, hand[3].rank, hand[4].rank), 'Straight'

        return 0, ''

    def is_three_kind(self, hand):
        # check if there are 3 of same rank:
        for i in range(len(hand)):
            if hand[4-i] == hand[3-i] and hand[3-i] == hand[2-i]:
                three_rank = hand[4-i].rank
                return self.calc_points(4, three_rank, three_rank, three_rank, hand[-i].rank, hand[1-i].rank), 'Three of a Kind'

        return 0, ''

    def is_two_pair(self, hand):
        for i in range(len(hand)):
            if hand[4-i] == hand[3-i]:
                for j in {2, 1}:
                    if hand[j-i] == hand[j-1-i]:
                        high_pair = hand[j-i].rank
                        low_pair = hand[4-i].rank
                        side = hand[-i].rank if j == 2 else hand[2-i].rank
                        return self.calc_points(3, high_pair, high_pair, low_pair, low_pair, side), 'Two Pair'

        return 0, ''

    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand
    def is_one_pair(self, hand):

        for i in range(len(hand)-1):
            if hand[i] == hand[i+1]:
                sides = list({0, 1, 2, 3, 4}.difference({i, i+1}))
                points = self.calc_points(
                    2, hand[i].rank, hand[i].rank, hand[sides[0]].rank, hand[sides[1]].rank, hand[sides[2]].rank)
                return points, 'One Pair'

        return 0, ''

    def is_high_card(self, hand):
        return self.calc_points(1, hand[0].rank, hand[1].rank, hand[2].rank, hand[3].rank, hand[4].rank), 'High Card'

    # calculate the points for each type. It's basically a polynomial with coefficients as input.
    def calc_points(self, h, c1, c2, c3, c4, c5):
        return h * 15**5 + c1 * 15**4 + c2 * 15**3 + c3 * 15**2 + c4 * 15 + c5


def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int(line)
    if (num_players < 2) or (num_players > 6):
        return

    # create the Poker object
    game = Poker(num_players)

    # play the game
    print("Number of players:", num_players)
    print()
    game.play()


if __name__ == "__main__":
    main()

