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

    # Deal community cards
    print("\nDealing community cards...\n")
    flop, turn, river = deal_community_cards(deck)
    print(f"Flop: {flop}")
    print(f"Turn: {turn}")
    print(f"River: {river}")

    # Players can take actions
    for player in player_hands:
        action = input(f"\n{player}, choose your action (check, bet, fold): ").lower()
        if action == "fold":
            print(f"{player} folded!")
        elif action == "bet":
            print(f"{player} placed a bet!")
        elif action == "check":
            print(f"{player} checked!")
        else:
            print(f"Invalid action. {player} skips their turn.")

    print("\nGame over! Evaluate hands and determine the winner manually.")


# Run the game
if __name__ == "__main__":
    play_poker()
