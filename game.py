



from random import choice

valid_options = ["rock", "paper", "scissors"]


def winner(user_choice, computer_choice):
    if user_choice == "rock" and computer_choice == "rock":
        #print("It's a tie!")
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "paper":
        #print("The computer wins")
        return "The computer wins"
    elif user_choice == "rock" and computer_choice == "scissors":
        #print("The user wins")
        return "The user wins"

    elif user_choice == "paper" and computer_choice == "rock":
        #print("The computer wins")
        #return "The computer wins"
        return "The user wins"
    elif user_choice == "paper" and computer_choice == "paper":
        #print("It's a tie!")
        return "It's a tie!"
    elif user_choice == "paper" and computer_choice == "scissors":
        #print("The user wins")
        #return "The user wins"
        return "The computer wins"

    elif user_choice == "scissors" and computer_choice == "rock":
        #print("The computer wins")
        return "The computer wins"
    elif user_choice == "scissors" and computer_choice == "paper":
        #print("The user wins")
        return "The user wins"
    elif user_choice == "scissors" and computer_choice == "scissors":
        return "It's a tie!"



if __name__ == "__main__":

    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_options:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_options)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    winning_message = winner(user_choice=u, computer_choice=c)
    print(winning_message)
