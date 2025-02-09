# Recommending a Care Game using a function----UPDATED VERSION
# This Python code also puts out the same output as the Program9, but it's slightly different in its functionality.


def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print ("Please enter a valid difficulty!")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print ("Please enter a valid number of players!")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print(f"You might like, {game}.")

main()