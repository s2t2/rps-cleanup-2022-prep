







#def test_winning_choice():
#    assert winning_choice(user_choice="rock", computer_choice="paper") == "paper"
#    assert winning_choice(user_choice="rock", computer_choice="rock") == None
#    assert winning_choice(user_choice="rock", computer_choice="scissors") == "rock"
#
#    assert winning_choice(user_choice="paper", computer_choice="paper") == None
#    assert winning_choice(user_choice="paper", computer_choice="rock") == "paper"
#    assert winning_choice(user_choice="paper", computer_choice="scissors") == "scissors"
#
#    assert winning_choice(user_choice="scissors", computer_choice="paper") == "scissors"
#    assert winning_choice(user_choice="scissors", computer_choice="rock") == "rock"
#    assert winning_choice(user_choice="scissors", computer_choice="scissors") == None


from game import winner

def test_winner():
    tie_message = "It's a tie!"
    win_message = "The user wins"
    lose_message = "The computer wins"

    assert winner(user_choice="rock", computer_choice="paper") == lose_message
    assert winner(user_choice="rock", computer_choice="rock") == tie_message
    assert winner(user_choice="rock", computer_choice="scissors") == win_message

    assert winner(user_choice="paper", computer_choice="paper") == tie_message
    assert winner(user_choice="paper", computer_choice="rock") == win_message
    assert winner(user_choice="paper", computer_choice="scissors") == lose_message

    assert winner(user_choice="scissors", computer_choice="paper") == win_message
    assert winner(user_choice="scissors", computer_choice="rock") == lose_message
    assert winner(user_choice="scissors", computer_choice="scissors") == tie_message
