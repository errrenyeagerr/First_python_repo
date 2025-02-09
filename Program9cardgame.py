# Recommending a Care Game using a function.

def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("klondike")
        else:
            print("Enter a valid number of player!")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Enter a valid number of player!")
    else:
        print("Enter a valid difficulty!")


def recommend(game):
    print(f"You might like, {game}.")

main()