import random
board = [" - "," - "," - ",
         " - "," - "," - ",
         " - "," - "," - "]

currentplayer = ' X '
gamerunning = True
winner = None

# printing the board
def printboard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----|-----|-----")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----|-----|-----")
    print(board[6]+" | "+board[7]+" | "+board[8])
    print()

#getting user input
def userinput():
    inp = int(input("enter any number between 0-8: "))
    if inp>=0 and inp<=8:
        if board[inp]==" - ":
            board[inp]=currentplayer
        else:
            print("place already filled")
            userinput()
    else:
        print("enter the values between 0-8.")
        userinput()

# switching the person
def switch_user():
    global currentplayer 
    if currentplayer==" X ":
        currentplayer=" O "
    else:
        currentplayer=" X "

#check for vertical
def check_for_vertical_win(board):
    global winner,gamerunning
    if board[0] == board[3] == board[6] and board[0] != " - ":
        print(f"the winner is player {board[0]}")
        printboard(board)
        gamerunning = False
        return True
    elif board[1] == board[4] == board[7] and board[1] != " - ":
        print(f"the winner is player {board[0]}")
        printboard(board)
        gamerunning = False
        return True
    elif board[2] == board[5] == board[8] and board[2] != " - ":
        print(f"the winner is player {board[0]}")
        printboard(board)
        gamerunning = False
        return True

def check_for_horizontal_win(board):
    global winner,gamerunning
    if board[0] == board[1] == board[2] and board[0] != " - ":
        print(f"the winner is player {board[0]}")
        printboard(board)
        gamerunning = False
        return True
    elif board[3] == board[4] == board[5] and board[3] != " - ":
        print(f"the winner is player {board[3]}")
        printboard(board)
        gamerunning = False
        return True
    elif board[6] == board[7] == board[8] and board[6] != " - ":
        print(f"the winner is player {board[6]}")
        printboard(board)
        gamerunning = False
        return True

def check_for_diagnol_win(board):
    global winner,gamerunning
    if board[0] == board[4] == board[8] and board[0] != " - ":
        print(f"the winner is player {board[0]}")
        printboard(board)
        gamerunning = False
        return True
    elif board[2] == board[4] == board[6] and board[3] != " - ":
        print(f"the winner is player {board[2]}")
        printboard(board)
        gamerunning = False
        return True

#checking for win
def check_for_win(board):
    check_for_diagnol_win(board)
    check_for_horizontal_win(board)
    check_for_vertical_win(board)
    return True

# checking for tie
def check_for_tie(board):
    if " - " not in board:
        print("it's a tie")
        printboard(board)
        gamerunning = False

# computer move
def computer():
    while currentplayer==" O ":
        position = random.randint(0,8)
        if board[position]==" - ":
            board[position]=" O "
            switch_user()
        

while gamerunning:
    printboard(board)
    userinput()
    check_for_tie(board)
    check_for_win(board)
    switch_user()
    computer()
    check_for_tie(board)
    check_for_win(board)