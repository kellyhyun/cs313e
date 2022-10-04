#  File: Poker.py

#  Description: simulating playing poker

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

#  Partner Name: Joon Kim (Unique Number: 52595)

#  Partner UT EID: jk45873

#  Course Name: CS 313E

#  Unique Number: 52600

#  Date Created:9/18/21

#  Date Last Modified:

import sys, random3


class Card(object):
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


class Deck(object):
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
        random3.shuffle(self.deck)

    # deal a card
    def deal(self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)


class Poker(object):
    # constructor
    def __init__(self, num_players=2, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards

        # deal the cards to the players
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.all_hands.append(hand)

    # Auxillary function checking the type of hand and the number of points and appending them
    # to corresponding lists.
    def check_type_and_points(self, point, type, hand_type, hand_points):
        if type != '':
            hand_type.append(type)
            hand_points.append(point)

            return True
        return False

    # simulate the play of poker
    def play(self):
        # sort the hands of each player and print
        for i in range(len(self.all_hands)):
            sorted_hand = sorted(self.all_hands[i], reverse=True)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)

        # determine the type of each hand and print
        hand_type = []  # create a list to store type of hand
        hand_points = []  # create a list to store points for hand
        # Goes through each player's hand and check if it falls under certain categories. The loop goes through highet to lowest category and ends once it finds the highest category that a player's hand fall into.
        for i in range(len(self.all_hands)):
            for test in range(10):
                if test == 0:
                    point, type = self.is_royal(self.all_hands[i])
                    break_or_not = self.check_type_and_points(point, type, hand_type, hand_points)
                    if break_or_not:
                        break

                elif test == 1:
                    point, type = self.is_straight_flush(self.all_hands[i])
                    break_or_not = self.check_type_and_points(point, type, hand_type, hand_points)
                    if break_or_not:
                        break

                elif test == 2:
                    point, type = self.is_four_kind(self.all_hands[i])
                    break_or_not = self.check_type_and_points(point, type, hand_type, hand_points)
                    if break_or_not:
                        break

                elif test == 3:
                    point, type = self.is_full_house(self.all_hands[i])
                    break_or_not = self.check_type_and_points(point, type, hand_type, hand_points)
                    if break_or_not:
                        break

                elif test == 4:
                    point, type = self.is_flush(self.all_hands[i])
                    break_or_not = self.check_type_and_points(point, type, hand_type, hand_points)
                    if break_or_not:
                        break

                elif test == 5:
                    point, type = self.is_straight(self.all_hands[i])
                    break_or_not = self.check_type_and_points(point, type, hand_type, hand_points)
                    if break_or_not:
                        break

                elif test == 6:
                    point, type = self.is_three_kind(self.all_hands[i])
                    break_or_not = self.check_type_and_points(point, type, hand_type, hand_points)
                    if break_or_not:
                        break

                elif test == 7:
                    point, type = self.is_two_pair(self.all_hands[i])
                    break_or_not = self.check_type_and_points(point, type, hand_type, hand_points)
                    if break_or_not:
                        break

                elif test == 8:
                    point, type = self.is_one_pair(self.all_hands[i])
                    break_or_not = self.check_type_and_points(point, type, hand_type, hand_points)
                    if break_or_not:
                        break

                elif test == 9:
                    point, type = self.is_high_card(self.all_hands[i])
                    break_or_not = self.check_type_and_points(point, type, hand_type, hand_points)
                    if break_or_not:
                        break

        print(hand_type)
        # Prints all player's hand type
        for i in range(len(self.all_hands)):
            print('Player {}: {}'.format(i + 1, hand_type[i]))

        print()

        # determine winner and print
        winner = 0
        winner_index = 0
        tie = False
        tie_index = 0
        for i in range(len(self.all_hands)):
            if i == 0:
                winner = hand_points[0]

            elif hand_points[i] == winner:
                tie = True
                tie_index = i

            if hand_points[i] > winner:
                if tie:
                    tie = False
                winner = hand_points[i]
                winner_index = i

        if tie == False:
            print('Player {} wins.'.format(winner_index + 1))
        else:
            print('Player {} ties.'.format(winner_index + 1))
            print('Player {} ties.'.format(tie_index + 1))

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

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush'

    # determine if a hand is a straight flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_straight_flush(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True

        # determines the rank of the highest card and checks if the next highest card
        # is one rank lower than the previous one for all five cards
        for j in range(14, 1, -1):
            if hand[0].rank == j:
                for i in range(len(hand)):
                    rank_order = rank_order and (hand[i].rank == j - i)

        # it is not a straight flush if not all cards differ by one in rank
        if (not rank_order):
            return 0, ''

        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight Flush'

    # determine if a hand is a four of a kind
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_four_kind(self, hand):
        rank_match = True
        execute_this = True

        # determines what the rank of the highest card is and checks if the subsequent
        # three card are same in rank
        for i in range(14, 1, -1):
            if hand[0].rank == i:
                for j in range(len(hand) - 1):
                    execute_this = execute_this and (hand[j].rank == i)

        # runs if the first four cards are not the same and checks if the last
        # four cards are same in rank
        if execute_this != True:
            for i in range(14, 1, -1):
                if hand[1].rank == i:
                    for j in range(1, 5):
                        rank_match = rank_match and (hand[j].rank == i)

        # if none above is True, it is not a four of a kind
        if (not rank_match and not execute_this):
            return 0, ''

        # assigns the last four cards the highest constants if they are the same
        if execute_this:
            points = 8 * 15 ** 5 + (hand[4].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[0].rank)
        # assigns the first four cards the highest constants if thy are the same
        else:
            points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[4].rank)

        return points, 'Four of a Kind'

    # determine if a hand is a full house
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_full_house(self, hand):
        rank_match = True
        execute_this = True
        overall_boolean = False

        # determines the rank of the first card and checks if the first three cards are
        # the same in rank
        for i in range(14, 0, -1):
            if hand[0].rank == i:
                for j in range(len(hand) - 2):
                    execute_this = execute_this and (hand[j].rank == i)

        # determines if the last two cards are the same in rank if the first three were
        # the same
        if execute_this:
            overall_boolean = (hand[3].rank == hand[4].rank)

        # checks the last three if the first three were not the same
        else:
            for i in range(14, 0, -1):
                if hand[2].rank == i:
                    for j in range(2, len(hand)):
                        rank_match = rank_match and (hand[j].rank == i)

        # checks if the first two cards are the same f the last three were the same
        if rank_match:
            overall_boolean = (hand[0].rank == hand[1].rank)

        # if overall boolean is false, it is not a full house
        if (not overall_boolean):
            return 0, ''

        # if the hand is sorted incorrectly, then return blank
        if (hand[2].rank < hand[3].rank):
            return 0, ''

        # assigns the first three cards the highest constants if they were the same
        if execute_this:
            points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[4].rank)
        # assign the last three cards the highest consants if they were the same
        else:
            points = 7 * 15 ** 5 + (hand[4].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
            points = points + (hand[1].rank)

        return points, 'Full House'

    # determine if a hand is a flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_flush(self, hand):
        same_suit = True
        # Checks if all five cards have the same suit
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Flush'

    # determine if a hand is a straight
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_straight(self, hand):
        rank_order = True

        # checks if all five cards differ by one in rank
        for j in range(14, 1, -1):
            if hand[0].rank == j:
                for i in range(len(hand)):
                    rank_order = rank_order and (hand[i].rank == j - i)

        # if not, the hand is not a straight
        if (not rank_order):
            return 0, ''

        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight'

    # determine if a hand is a three of a kind
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_three_kind(self, hand):
        rank_match = True
        execute_this = True
        execute_this_again = True

        # checks if the first three are the same in rank
        for i in range(14, 1, -1):
            if hand[0].rank == i:
                for j in range(len(hand) - 2):
                    execute_this = execute_this and (hand[j].rank == i)

        # if it is not, then it checks if the second through fourth card are the same
        if execute_this != True:
            for i in range(14, 1, -1):
                if hand[1].rank == i:
                    for j in range(1, 4):
                        rank_match = rank_match and (hand[j].rank == i)

        # if the hand satisfies none of the above, it checks if the last three cards
        # are the same
        if execute_this != True and rank_match != True:
            for i in range(14, 1, -1):
                if hand[1].rank == i:
                    for j in range(2, 5):
                        execute_this_again = execute_this_again and (hand[j].rank == i)

        # if no conditions above are satisfied, the hand is not a three of a kind
        if (not execute_this and not rank_match and not execute_this_again):
            return 0, ''

        # assigns first three the highest constants if they are the same
        if execute_this:
            points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[4].rank)
        # asigns the second though fourth card the highest constants if they are the same
        elif rank_match:
            points = 4 * 15 ** 5 + (hand[3].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
            points = points + (hand[4].rank)
        # assigns the ast three the highest constants if they are the same
        else:
            points = 4 * 15 ** 5 + (hand[3].rank) * 15 ** 4 + (hand[4].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
            points = points + (hand[1].rank)

        return points, 'Three of a Kind'

    # determine if a hand is a two pair
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_two_pair(self, hand):
        rank_match = True
        execute_this = True
        check_second1 = False
        check_second2 = False
        check_second3 = False

        # determines the rank of the first card and checks if the second card is same in
        # rank
        for i in range(14, 0, -1):
            if hand[0].rank == i:
                for j in range(len(hand) - 3):
                    execute_this = execute_this and (hand[j].rank == i)

        # if the first two cards are the same, this checks if the third and fourth or the
        # fourth and fifth cards are the same
        if execute_this:
            check_second1 = (hand[2] == hand[3])
            check_second2 = (hand[3] == hand[4])
            rank_match = False

        # if the first two card are not the same, it checks if the second and hird card
        # are the same
        if execute_this == False:
            for i in range(14, 0, -1):
                if hand[1].rank == i:
                    for j in [1, 2]:
                        rank_match = rank_match and (hand[j].rank == i)

        # if the second and third cards are the same, it checks if the third and fourth
        # cards are the same
        if rank_match:
            check_second3 = (hand[3] == hand[4])

        # if none of the checkpoint booleans are True, the hand is not a two pair
        if (not check_second1 and not check_second2 and not check_second3):
            return 0, ''

        # assigns the first two cards the highest constants and the next two cards the next
        # highest constants if the first four cards are two pairs
        if check_second1:
            points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[4].rank)
        # assigns the first two cards the highest constats and the last two cards the next
        # highest constants if the first two and the last two cards are two pairs
        elif check_second2:
            points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1
            points = points + (hand[2].rank)
        # assigns the second and third cards the highest and the last two cards the next
        # highet constant if the last four cards form two pairs
        elif check_second3:
            points = 3 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
            points = points + (hand[4].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[0].rank)

        return points, 'Two Pair'

    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand
    def is_one_pair(self, hand):
        one_pair = False
        this_card = 0
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                one_pair = True
                this_card = i
                break
        if (not one_pair):
            return 0, ''

        if this_card == 0:
            points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[4].rank)
        elif this_card == 1:
            points = 2 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
            points = points + (hand[0].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
            points = points + (hand[4].rank)
        elif this_card == 2:
            points = 2 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
            points = points + (hand[0].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
            points = points + (hand[4].rank)
        elif this_card == 3:
            points = 2 * 15 ** 5 + (hand[3].rank) * 15 ** 4 + (hand[4].rank) * 15 ** 3
            points = points + (hand[0].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
            points = points + (hand[2].rank)

        return points, 'One Pair'

    # determine if a hand is a high card
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_high_card(self, hand):

        # assigns the highest card to the highest constant, the next highest card to the
        # next highest constant, etc.
        points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'High Card'


def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int(line)
    if (num_players < 2) or (num_players > 6):
        return

    # create the Poker object
    game = Poker(num_players)

    # print the number of players from sys.stdin
    print('Number of players: {}'.format(num_players))
    print()

    # play the game
    game.play()


if __name__ == "__main__":
    main()
