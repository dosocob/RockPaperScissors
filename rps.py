import time
import random
def rpsfriend():
    player1choice = ""
    player2choice = ""
    print("\nRock Paper Scissors")
    print("\n   1. Rock")
    print("\n   2. Paper")
    print("\n   3. Scissors")
    print("\n   4. Quit")
    choice = input("\n   Player 1 enter your choice: ")
    if choice == "1":
        player1choice = "Rock"
    elif choice == "2":
        player1choice = "Paper"
    elif choice == "3":
        player1choice = "Scissors"
    elif choice == "4":
        print("\n   Thanks for playing!")
        time.sleep(1)
        exit()
    choice = input("\n   Player 2 enter your choice: ")
    print("\n")
    if choice == "1":
        player2choice = "Rock"
    elif choice == "2":
        player2choice = "Paper"
    elif choice == "3":
        player2choice = "Scissors"
    elif choice == "4":
        print("\n   Thanks for playing!")
        time.sleep(1)
        exit()
    if player1choice == player2choice:
        print("It's a tie!")
    elif player1choice == "Rock" and player2choice == "Scissors":
        print("Player 1 wins!")
    elif player1choice == "Paper" and player2choice == "Rock":
        print("Player 1 wins!")
    elif player1choice == "Scissors" and player2choice == "Paper":
        print("Player 1 wins!")
    elif player1choice == "Rock" and player2choice == "Paper":
        print("Player 2 wins!")
    elif player1choice == "Scissors" and player2choice == "Rock":
        print("Player 2 wins!")
    elif player1choice == "Paper" and player2choice == "Scissors":
        print("Player 2 wins!")
    else:
        print("Invalid choice!")
    print("\n   1. Try Again")
    print("\n   2. Quit")
    choice = input("\n   Player 1 enter your choice: ")
    if choice == "1":
        rpsfriend()
    elif choice == "2":
        print("\n   Thanks for playing!")
        time.sleep(1)
        exit()
def rpscomputer():
    aichoice = random.randint(1,3)
    print(aichoice)
    print("Rock Paper Scissors")
    print("\n   1. Rock")
    print("\n   2. Paper")
    print("\n   3. Scissors")
    print("\n   4. Quit")
    choice = input("\n   Player 1 enter your choice: ")
    print("\n")
    if choice == aichoice:
        print("It's a tie!")
    elif choice == "1" and aichoice == 2:
        print("AI wins!")
    elif choice == "2" and aichoice == 3:
        print("AI wins!")
    elif choice == "3" and aichoice == 1:
        print("AI wins!")
    elif choice == "1" and aichoice == 3:
        print("Player wins!")
    elif choice == "2" and aichoice == 1:
        print("Player wins!")
    elif choice == "3" and aichoice == 2:
        print("Player wins!")

    elif choice == "4":
        print("\n   Thanks for playing!")
        time.sleep(1)
        exit()
    print("\n   1. Try Again")
    print("\n   2. Quit")
    choice = input("\n   Player 1 enter your choice: ")
    if choice == "1":
        rpscomputer()
    elif choice == "2":
        print("\n   Thanks for playing!")
        time.sleep(1)
        exit()
def main():
    print("\n   Rock Paper Scissors")
    print("\n   1. Player vs Player")
    print("\n   2. Player vs Computer")
    userin = input("\n   Select Gamemode: ")
    print("\n")
    if userin == "1":
        rpsfriend()
    elif userin == "2":
        rpscomputer()










main()




