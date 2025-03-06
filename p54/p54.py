"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

"""

# kinda trash but still works. and yes ai helped write but aint no body got time to do this by hand lol

def card_value(card):
    """Convert card value to numeric value for comparison"""
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
              '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[card[0]]

def parse_hand(cards):
    """Parse a hand of 5 cards into a list of tuples (value, suit)"""
    parsed_hand = []
    for card in cards:
        if len(card) == 3:  # Handle "10" as a special case
            value = "10"
            suit = card[2]
        else:
            value = card[0]
            suit = card[1]
        parsed_hand.append((value, suit))
    return parsed_hand

def get_card_counts(hand):
    """Get counts of each card value in the hand"""
    counts = {}
    for card in hand:
        value = card[0]
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts

def get_values(hand):
    """Get the card values in the hand, sorted by count and then by card value"""
    counts = get_card_counts(hand)
    # Sort values by count (descending) and then by card value (descending)
    values = sorted(counts.keys(), key=lambda x: (counts[x], card_value(x)), reverse=True)
    return values

def get_suits(hand):
    """Get the suits in the hand"""
    return [card[1] for card in hand]

def is_royal_flush(hand):
    values = [card[0] for card in hand]
    suits = get_suits(hand)
    royal_values = {'10', 'J', 'Q', 'K', 'A'}
    return len(set(suits)) == 1 and set(values) == royal_values

def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)

def is_four_of_a_kind(hand):
    counts = get_card_counts(hand)
    return 4 in counts.values()

def is_full_house(hand):
    counts = get_card_counts(hand)
    return sorted(counts.values()) == [2, 3]

def is_flush(hand):
    suits = get_suits(hand)
    return len(set(suits)) == 1

def is_straight(hand):
    values = sorted([card_value(card) for card in hand])
    return values == list(range(min(values), max(values) + 1))

def is_three_of_a_kind(hand):
    counts = get_card_counts(hand)
    return 3 in counts.values()

def is_two_pairs(hand):
    counts = get_card_counts(hand)
    return list(counts.values()).count(2) == 2

def is_one_pair(hand):
    counts = get_card_counts(hand)
    return list(counts.values()).count(2) == 1

def is_high_card(hand):
    # All hands qualify for high card, but this function helps maintain the pattern
    return True

def hand_rank(hand):
    """Rank the hand from 1 (high card) to 10 (royal flush)"""
    if is_royal_flush(hand):
        return 10
    if is_straight_flush(hand):
        return 9
    if is_four_of_a_kind(hand):
        return 8
    if is_full_house(hand):
        return 7
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_three_of_a_kind(hand):
        return 4
    if is_two_pairs(hand):
        return 3
    if is_one_pair(hand):
        return 2
    return 1  # High card

def compare_hands(hand1, hand2):
    """Compare two hands and return 1 if hand1 wins, 2 if hand2 wins"""
    rank1 = hand_rank(hand1)
    rank2 = hand_rank(hand2)
    
    if rank1 > rank2:
        return 1
    elif rank2 > rank1:
        return 2
    
    # If ranks are equal, compare the values
    values1 = get_values(hand1)
    values2 = get_values(hand2)
    
    for v1, v2 in zip(values1, values2):
        if card_value(v1) > card_value(v2):
            return 1
        elif card_value(v2) > card_value(v1):
            return 2
    
    # If all values match, it's a tie (not possible in this problem)
    return 0

def poker(line):
    """Determine the winner of a poker hand"""
    cards = line.strip().split()
    p1_cards = cards[:5]
    p2_cards = cards[5:]
    
    p1_hand = parse_hand(p1_cards)
    p2_hand = parse_hand(p2_cards)
    
    return compare_hands(p1_hand, p2_hand)

def main():
    p1_wins = 0
    with open("p54/0054_poker.txt", "r") as file:
        for line in file:
            result = poker(line)
            if result == 1:
                p1_wins += 1
    
    print(f"Player 1 wins {p1_wins} hands")

if __name__ == "__main__":
    main()