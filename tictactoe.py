import os

def drawBoard(board):
    for i in range(6, -1, -3):
        print(' ' + board[i] + '|' +
              board[i+1] + '|' + board[i+2])

def playerInput(board, turn):
    pos = -1
    print(turn + "'s turn:")
    while pos == -1:
        try:
            print("Pick position 1-9:")
            pos = int(input())
            if not (1 <= pos <= 9) or board[pos - 1] != ' ':
                print("Invalid position. Try again.")
                pos = -1
        except ValueError:
            print("Enter a valid number.")

    board[pos - 1] = turn
    return board

def checkWinner(board):
    for i in range(0, 3):
        r = i * 3
        if board[r] != ' ' and board[r] == board[r+1] == board[r+2]:
            return board[r]

    for i in range(0, 3):
        if board[i] != ' ' and board[i] == board[i+3] == board[i+6]:
            return board[i]

    if board[0] != ' ' and board[0] == board[4] == board[8]:
        return board[0]

    if board[2] != ' ' and board[2] == board[4] == board[6]:
        return board[2]

    return 0

def is_board_full(board):
    return ' ' not in board

def resultOfGame(result):
    if result == 0:
        print("It's a draw!")
    else:
        print('{} wins!'.format(result))

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    turn = 'X'
    board = [' '] * 9
    # player1=input("Enter player 1 name : ")
    # player2= input("Enter player 2 name :")

    while True:
        clearScreen()
        drawBoard(board)
        board = playerInput(board, turn)
        result = checkWinner(board)

        if result or is_board_full(board):
            clearScreen()
            drawBoard(board)
            resultOfGame(result)
            break

        turn = 'O' if turn == 'X' else 'X'

if __name__ == "__main__":
    main()
    
    