
import random

print("Welcome to Triple Showdown!\nWhere you must use your hands to play against a handless creature and defeat it!")

while True:
    start = input("Press S to start the game or F to exit: ").strip().upper()

    if start == "S":
        print("\nThe game has started!")

        the_list = ["Rock", "Paper", "Scissors"]

        your_score = 0
        comp_score = 0

        for round_number in range(1, 4):
            print(f"\n---------- Round {round_number} ----------")

            while True:
                your_choice = input("""Choose one:
1- Rock
2- Paper
3- Scissors
Your choice: """)

                if your_choice == "1":
                    your_choice_text = "Rock"
                    break

                elif your_choice == "2":
                    your_choice_text = "Paper"
                    break

                elif your_choice == "3":
                    your_choice_text = "Scissors"
                    break

                else:
                    print("Invalid choice! Please enter 1, 2, or 3.")

            comp_choice = random.choice(the_list)

            print("\nYour choice:", your_choice_text)
            print("Computer's Choice:", comp_choice)

            if your_choice_text == comp_choice:
                print("It's a Tie!")

            elif (your_choice_text == "Rock" and comp_choice == "Scissors") or \
                 (your_choice_text == "Paper" and comp_choice == "Rock") or \
                 (your_choice_text == "Scissors" and comp_choice == "Paper"):

                print("You win!")
                your_score += 1

            else:
                print("The Computer Wins!")
                comp_score += 1

            print("\nYour score:", your_score)
            print("Computer's Score:", comp_score)

        print("\n========== Final Score ==========")
        print("Your score:", your_score)
        print("Computer's Score:", comp_score)

        if your_score > comp_score:
            print("\nYou are the overall winner! Congratulations!")

        elif comp_score > your_score:
            print("\nThe Computer is the overall winner!")

        else:
            print("\nThe game ended in a tie!")

    elif start == "F":
        print("You have exited the game, See you next time!")
        break

    else:
        print("Invalid input! Please enter S to start or F to exit.")