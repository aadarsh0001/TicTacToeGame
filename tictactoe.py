# Function to Draw Platform

def print_tic_t_t(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |   {}".format(values[0], values[1], values[2]))
    print("\t_____|_____|_____")

    print("\t     |     |")
    print("\t  {}  |  {}  |   {}".format(values[3], values[4], values[5]))
    print("\t_____|_____|_____")

    print("\t     |     |")

    print("\t  {}  |  {}  |   {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

# Score-card function
def print_scoreboard(score_board):
    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t          SCOREBOARD 🥇 BY AADI          ")
    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    players= list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Function to know who won the game
def check_winner(player_position, current_player):

    # Possibility for winner
    soln = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

  # loop to check if any winning possibility satisfying or not
    for x in  soln:
        if all(y in player_position[current_player] for y in x):

            #if any winning possibility will satisfy , return true
            return True
    #if any winning possibility will not satisfy , return false
    return False

# Function to check eighter game draw or not
def check_draw(player_position):
    if len(player_position["X"]) + len(player_position["O"]) == 9:
        return True
    return False

# this function for single Game (game once in a time)
def single_game(current_player):

    # Represent the game
    values = [" " for x in range(9)]

    # Note X and O's positions
    player_position = {"X":[], "O":[]}

    # Loop for single game
    while True:
        print_tic_t_t(values)

        # Try block to move the input
        try:
            print("Player", current_player, "\'s turn. Number of box? :", end="")
            move = int(input())
        except ValueError:
            print("You input wrong value! Please try again")
            continue
    
        # Check either player have input correct position or not
        if move < 1 or move > 9:
            print(" Please enter right number of position 1 to 9")
            continue

        # Condition to check entered position is already filled or not
        if values[move-1] != ' ':
            print(" This position is already filled. Try another position!!!")
            continue

        # Update  the status of game

        # Update score card
        values[move-1] = current_player

        # Update the position of player
        player_position[current_player].append(move)

        # Function to check the winner
        if check_winner(player_position, current_player):
            print_tic_t_t(values)
            print("Congratulations 🎊", current_player, " is winner 🥇")
            print("\n")
            return current_player

        # Function to check the is draw or not
        if check_draw(player_position):
            print_tic_t_t(values)
            print("Hehe this game is draw")
            print("\n")
            return "D"

        # Change player's move
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

if __name__== "__main__":

    print("1st player's detail")
    play1 = input(" Please enter player's name :")
    print("\n")

    print("2nd player's detail")
    play2 = input(" Please enter player's name :")
    print("\n")

    # Save who choose X and who choose O
    current_player = play1

    # Save charecter choosen by player
    player_choice = {"X" : "", "O" : ""}

    # Save Character
    option = ["X", "O"]

    # Save the scorecard details
    score_board = {play1: 0, play2: 0}
    print_scoreboard(score_board)

    # Loop for game(TicTacToe) series
    # This loop will run till player choose to quit
    while True:

        # Choice of player
        print(current_player,"\'s Turn to choose")
        print("Enter 1, If your choice is X")
        print("Enter 2, If your choice is O")
        print("Enter 3, If your to Quit")

        # Try block for choice of player
        try:
            choice = int(input())
        except ValueError:
            print(" Oops your choice is wrong!, Please try again\n")
            continue

        # Rules for player's choice
        if choice == 1:
            player_choice["X"] = current_player
            if current_player == play1:
                player_choice["O"] = play2
            else:
                player_choice["O"] = play1

        elif choice == 2:
            player_choice["O"] = current_player
            if current_player == play1:
                player_choice["X"] = play2
            else:
                player_choice["X"] = play1
    
        elif choice == 3:
            print("Final Score")
            print_scoreboard(score_board)
            break

        else:
            print("Oops, Your choice is wrong ! Please try again\n")

        # Save the winner in single game(TicTacToe)
        winner = single_game(option[choice-1])

        # Edit scorecard as per winner
        if winner != "D":
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] +1
    
        print_scoreboard(score_board)
        # Change the turn of player to choose X or O
        if current_player == play1:
            current_player = play2
        else:
            current_player = play1

#~~~~~~~~~~~~~~~~~~~~~~~Game End~~~~~~~~~~~~~~~~~~~~~~~~~~