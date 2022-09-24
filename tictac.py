import random

#variables
winner = None
game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
game_active = True
player = "X"
winner = None
count = 0

#prints current board
def printBoard(game_board):
    print("\n" + game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8] + "\n")

#checks for win
def checkWin(game_board):
    global winner

    #check vertical wins
    if game_board[0] == game_board[3] == game_board[6]:
        winner = game_board[0]
        return True
    if game_board[1] == game_board[4] == game_board[7]:
        winner = game_board[1]
        return True
    if game_board[2] == game_board[5] == game_board[8]:
        winner = game_board[2]
        return True

    #check horizontal wins
    if game_board[0] == game_board[1] == game_board[2]:
        winner = game_board[0]
        return True
    if game_board[3] == game_board[4] == game_board[5]:
        winner = game_board[3]
        return True
    if game_board[6] == game_board[7] == game_board[8]:
        winner = game_board[6]
        return True
    
    #check diagonal wins
    if game_board[0] == game_board[4] == game_board[8]:
        winner = game_board[0]
        return True
    if game_board[2] == game_board[4] == game_board[6]:
        winner = game_board[2]
        return True

    return False

#check for tie
def checkTie():
    if count == 9:
        print("-----It's a tie-----\n")
        game_active = False
        return True

#main game loop
while(game_active):
    
    printBoard(game_board)

    #check for win
    if checkWin(game_board) == True:
        if winner == "X":
            print("-----YOU WIN!-----\n")
        if winner == "O":
            print("-----YOU LOST-----\n")
        game_active = False
        break

    if checkTie():
        break

    print("*** Current Player: " + player + " ***")

    #loop takes player input
    valid_spot = False
    while(not valid_spot):

        if player == "X":
            user_input = input("Input a number: ")
        else:
            user_input = random.randint(1, 9)

        if user_input >= 1 and user_input <= 9 and game_board[user_input-1] != "X" and game_board[user_input-1] != "O":
            game_board[user_input-1] = player
            valid_spot = True
            count += 1
        elif user_input >= 1 and user_input <= 9:
            if player == "X":
                print("That spot is taken.")
        else:
            if player == "X":
                print("Input is not 1 through 9.")

    #switch players
    if player == "X":
        player = "O"
    else:
        player = "X"