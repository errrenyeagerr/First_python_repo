import random


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


# Get the player's bet
def get_bet():
    while True:
        try:
            bet = int(input("Enter your bet (10, 20, or 50): "))
            if bet in [10, 20, 50]:
                return bet
            else:
                print("Invalid bet! Please bet 10, 20, or 50.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


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
    bets = {}
    players_in_game = list(player_hands.keys())  # Track players still in the game

    for player in player_hands:
        bet = get_bet()
        total_pot += bet
        bets[player] = bet
        print(f"{player} has bet {bet}.")

    # Deal community cards (flop)
    print("\nDealing the community cards...\n")
    flop, turn, river = deal_community_cards(deck)
    print(f"Flop: {flop}")

    # Show player actions after dealing flop
    for player in players_in_game:
        action = input(f"\n{player}, choose your action (check, bet, fold): ").lower()
        if action == "fold":
            print(f"{player} folded!")
            players_in_game.remove(player)
        elif action == "bet":
            bet = get_bet()
            total_pot += bet
            bets[player] += bet
            print(f"{player} placed a bet of {bet}.")
        elif action == "check":
            print(f"{player} checked!")
        else:
            print(f"Invalid action. {player} skips their turn.")

    # Deal the turn and river cards
    print("\nDealing the Turn and River cards...\n")
    print(f"Turn: {turn}")
    print(f"River: {river}")

    # Final player actions after the river
    for player in players_in_game:
        action = input(f"\n{player}, choose your action (check, bet, fold): ").lower()
        if action == "fold":
            print(f"{player} folded!")
            players_in_game.remove(player)
        elif action == "bet":
            bet = get_bet()
            total_pot += bet
            bets[player] += bet
            print(f"{player} placed a bet of {bet}.")
        elif action == "check":
            print(f"{player} checked!")
        else:
            print(f"Invalid action. {player} skips their turn.")

    print(f"\nTotal pot: {total_pot}")

    # Winner calculation (for now, let's assume Player 1 wins)
    if len(players_in_game) == 1:
        winner = players_in_game[0]
        winnings = total_pot
        print(f"\n{winner} wins the pot of {winnings}!")
        print(f"{winner} has won {winnings}!")
    else:
        print("\nNo winner determined yet. You can implement hand evaluation to declare a winner.")

    # End the game
    print("\nGame over!")


# Run the game
if __name__ == "__main__":
    play_poker()
