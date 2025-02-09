import random

# Define poker hand rankings
rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12,
               'King': 13, 'Ace': 14}


# Create the deck
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]


# Shuffle and deal cards
def deal_cards(deck, num_players):
    random.shuffle(deck)
    hands = {f"Player {i + 1}": [deck.pop(), deck.pop()] for i in range(num_players)}
    return hands


# Simulate the community cards
def deal_community_cards(deck):
    flop = [deck.pop() for _ in range(3)]
    turn = deck.pop()
    river = deck.pop()
    return flop, turn, river


# Get the player's bet (Call, Raise, or Fold)
def get_bet(current_bet, player):
    while True:
        try:
            action = input(
                f"{player}, current highest bet is {current_bet}. Do you want to 'call', 'raise', or 'fold'? ").lower()
            if action == 'fold':
                return 'fold', 0
            elif action == 'call':
                return 'call', current_bet
            elif action == 'raise':
                raise_amount = int(
                    input(f"{player}, enter the amount you want to raise (minimum raise is {current_bet + 10}): "))
                if raise_amount >= current_bet + 10:
                    return 'raise', raise_amount
                else:
                    print(f"Raise must be at least {current_bet + 10}.")
            else:
                print("Invalid action. Please choose 'call', 'raise', or 'fold'.")
        except ValueError:
            print("Invalid input! Please enter a valid number for raise.")


# Evaluate a player's hand using poker rules
def evaluate_hand(hand, community_cards):
    # Combine hand and community cards
    all_cards = hand + community_cards
    ranks = [card.split()[0] for card in all_cards]
    suits = [card.split()[-1] for card in all_cards]

    # Count frequency of each rank
    rank_count = {rank: ranks.count(rank) for rank in set(ranks)}
    sorted_ranks = sorted(ranks, key=lambda x: rank_values[x], reverse=True)

    # Check for Flush
    flush = len(set(suits)) == 1
    # Check for Straight
    straight = sorted([rank_values[rank] for rank in sorted_ranks]) == list(
        range(min(rank_values[rank] for rank in sorted_ranks), max(rank_values[rank] for rank in sorted_ranks) + 1))

    # Rank the hand (simplified)
    if flush and straight:
        if sorted_ranks[0] == 'Ace':
            return 'Royal Flush', 10
        return 'Straight Flush', 9
    if 4 in rank_count.values():
        return 'Four of a Kind', 8
    if sorted(rank_count.values()) == [2, 3]:
        return 'Full House', 7
    if flush:
        return 'Flush', 6
    if straight:
        return 'Straight', 5
    if 3 in rank_count.values():
        return 'Three of a Kind', 4
    if list(rank_count.values()).count(2) == 2:
        return 'Two Pair', 3
    if 2 in rank_count.values():
        return 'One Pair', 2
    return 'High Card', 1


# Main game loop
def play_poker():
    print("Welcome to Texas Hold'em Poker!")
    num_players = int(input("Enter the number of players (2-8): "))

    if not 2 <= num_players <= 8:
        print("Invalid number of players. Please restart the game.")
        return

    # Initialize the deck and deal cards
    deck = create_deck()
    player_hands = deal_cards(deck, num_players)

    print("\nDealing cards to players...\n")
    for player, hand in player_hands.items():
        print(f"{player}'s hand: {hand}")

    # Players can place their bets
    total_pot = 0
    bets = {f"Player {i + 1}": 0 for i in range(num_players)}  # Initialize all bets to 0
    players_in_game = list(player_hands.keys())  # Track players still in the game
    current_bet = 0  # The current highest bet

    # Pre-flop betting
    print("\nPre-flop betting round...")
    for player in player_hands:
        action, bet = get_bet(current_bet, player)
        if action == 'fold':
            print(f"{player} folded!")
            players_in_game.remove(player)
        elif action == 'call':
            total_pot += bet
            bets[player] = bet
            print(f"{player} called the bet of {bet}.")
        elif action == 'raise':
            total_pot += bet
            bets[player] = bet
            current_bet = bet
            print(f"{player} raised the bet to {bet}.")

    # Deal community cards (flop)
    print("\nDealing the community cards...\n")
    flop, turn, river = deal_community_cards(deck)
    print(f"Flop: {flop}")

    # Post-flop betting round
    print("\nPost-flop betting round...")
    for player in players_in_game:
        action, bet = get_bet(current_bet, player)
        if action == 'fold':
            print(f"{player} folded!")
            players_in_game.remove(player)
        elif action == 'call':
            total_pot += bet
            bets[player] = bet
            print(f"{player} called the bet of {bet}.")
        elif action == 'raise':
            total_pot += bet
            bets[player] = bet
            current_bet = bet
            print(f"{player} raised the bet to {bet}.")

    # Deal the turn and river cards
    print("\nDealing the Turn and River cards...\n")
    print(f"Turn: {turn}")
    print(f"River: {river}")

    # Final betting round after river
    print("\nFinal betting round...")
    for player in players_in_game:
        action, bet = get_bet(current_bet, player)
        if action == 'fold':
            print(f"{player} folded!")
            players_in_game.remove(player)
        elif action == 'call':
            total_pot += bet
            bets[player] = bet
            print(f"{player} called the bet of {bet}.")
        elif action == 'raise':
            total_pot += bet
            bets[player] = bet
            current_bet = bet
            print(f"{player} raised the bet to {bet}.")

    print(f"\nTotal pot: {total_pot}")

    # Evaluate hands of remaining players and determine the winner
    player_rankings = []
    for player in players_in_game:
        hand = player_hands[player]
        community_cards = flop + [turn, river]
        hand_name, hand_value = evaluate_hand(hand, community_cards)
        player_rankings.append((player, hand_name, hand_value))

    # Sort players by hand value (higher value wins)
    player_rankings.sort(key=lambda x: x[2], reverse=True)
    winner = player_rankings[0]
    print(f"\n{winner[0]} wins with {winner[1]} and takes the pot of {total_pot}!")

    # End the game
    print("\nGame over!")


# Run the game
if __name__ == "__main__":
    play_poker()
