def org(b, a):
    if a == 0:
        a = "Rock"
        print(f"{b} choice: {a}")
    elif a == 1:
        a = "Paper"
        print(f"{b} choice: {a}")
    elif a == 2:
        a = "Scissor"
        print(f"{b} choice: {a}")

from random import randrange as rand
while True:
    try:
        print("\nWelcome to the Rock-Paper-Scissor game: \nEnter '1' to play \nEnter '2' to exit the game")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            try:
                rounds = int(input("\nEnter the number of round you want to play: "))
                bp = 0
                pp = 0
                for i in range (rounds):
                    bot_turn = rand(0,3)
                    print("\nMenu: \nEnter '0' for Rock \nEnter '1' for Paper \nEnter '2' for Scissor")
                    try:
                        user_turn = int(input("\nEnter your choice(0,1,2): "))
                        if user_turn in (0,1,2):
                            print(f"\nRound-{i + 1}")
                            org("Your", user_turn)
                            org("Bot's", bot_turn)
                            if user_turn == bot_turn:
                                continue
                            elif user_turn == 0 and bot_turn == 1:
                                bp += 1
                            elif user_turn == 1 and bot_turn == 2:
                                bp += 1
                            elif user_turn == 2 and bot_turn == 0:
                                bp += 1
                            else:
                                pp += 1
                        else:
                            print("\nI don't want to play with you \n\"GAME RESTARTS\"")
                            break
                    except:
                        print("\nI don't want to play with you \n\"VALID VALUE NOT ENTERED\" \n\"GAME RESTARTS\"")
                        break
                else:
                    print(f"\nFinal Score: \nPoints of bot = {bp} \nYou points = {pp}")
                    if bp > pp:
                        print("Winner is the bot")
                    elif bp < pp:
                        print("You are the winner")
                    else:
                        print("It was a tie")
            except:
                print("Valid value not entered")
        elif ch == 2:
            break
        else:
            print("Invalid Choice")
    except:
        print("Valid value not entered")
        continue
print("Thank you for playing")



