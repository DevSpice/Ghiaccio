
def x_or_o():
    
    print("\n"*100)
    inp = input("Player 1: Do you wish to be X or O?\nEnter your choice: ")

    while inp.lower() != "x" and inp.lower() != "o":
       inp = input("Improper selection. Please choose either X or O: ")
    if inp.lower() == "o":
        print("Player 2 is X.")
        input()
        return "o"
    else:
        print("Player 2 is O.")
        input()
        return "x"

def display_board(brd):
    print("\n"*100)
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def check(choice, brd):
        if choice > 9 or choice < 1 or brd[choice - 1] == 'X' or brd[choice - 1] == 'O':
            return False
        else:
            return True

def win(brd):
    if brd[0] == brd[1] and brd[0] == brd[2]:
        return brd[0]
    elif brd[3] == brd[4] and brd[3] == brd[5]:
        return brd[3]
    elif brd[6] == brd[7] and brd[6] == brd[8]:
        return brd[6]
    elif brd[0] == brd[3] and brd[0] == brd[6]:
        return brd[0]
    elif brd[1] == brd[4] and brd[1] == brd[7]:
        return brd[1]
    elif brd[2] == brd[5] and brd[2] == brd[8]:
        return brd[2]
    elif brd[0] == brd[4] and brd[0] == brd[8]:
        return brd[0]
    elif brd[6] == brd[4] and brd[6] == brd[2]:
        return brd[6]
    else:
        return "None"

loop = 1


while loop == 1:
    board = ['1','2','3','4','5','6','7','8','9']
    p1 = x_or_o()
    current = 1
    again = 'null'
    while True:
        display_board(board)
        if current == 1:
            print("Player 1 - move")
            enter = int(input("Please enter a number to select your first space: "))
            while check(enter,board) == False:
                enter = int(input("Improper selection. Please enter a number to select your first space: "))
            if p1 == "o":
                board[enter - 1] = 'O'
            else:
                board[enter - 1] = 'X'
            current = 2
        else:
            print("Player 2 - move")
            enter = int(input("Please enter a number to place your marker: "))
            while check(enter,board) == False:
                enter = int(input("Improper selection. Please enter a number to select your first space: "))
            if p1 != "o":
                board[enter - 1] = 'O'
            else:
                board[enter - 1] = 'X'
            current = 1
        
        if win(board) == "O":
            if p1 == "o":
                display_board(board)
                print("Player 1 wins!")
                break
            else:
                display_board(board)
                print("Player 2 wins!")
                break

        elif win(board) == "X":
            if p1 == "o":
                display_board(board)
                print("Player 2 wins!")
                break
            else:
                display_board(board)
                print("Player 1 wins!")
                break
        else:
            pass
    
    while again.lower() != 'y' and again.lower() != 'n':
        again = input("Would you like to play again? Y/N: ")
        if again.lower() == 'n':
            loop = 0
        elif again.lower() == 'y':
            break
        else:
            again = input("Improper selection. Please choose either Y or N: ")
        

