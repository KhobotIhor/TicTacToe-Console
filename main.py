import random
import os
import sys
winner = ''

print("Welcome to the TicTacToe Game!")
side = input("Please choose your side(type 'X' for X or 'O' for O)  ")
if side == 'X':
    computer_side = 'O'
elif side == 'O':
    computer_side = 'X'
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = ''''''

def check_winner():
    global winner
    if squares[0] == squares[1] == squares[2]==side or squares[3] == squares[4] == squares[5]==side or squares[6] == squares[7] == squares[8]==side:
        winner = 'You'
        return True
    elif squares[0] == squares[1] == squares[2]==computer_side or squares[3] == squares[4] == squares[5]==computer_side or squares[6] == squares[7] == squares[8]==computer_side:
        winner = 'Computer'
        return True
    elif squares[0] == squares[3] == squares[6] == side or squares[1] == squares[4] == squares[7] == side or squares[2] == squares[5] == squares[8] == side:
        winner = 'You'
        return True
    elif squares[0] == squares[3] == squares[6] == computer_side or squares[1] == squares[4] == squares[7] == computer_side or squares[2] == squares[5] == squares[8] == computer_side:
        winner = 'Computer'
        return True
    elif squares[0] == squares[4] == squares[8] == side or squares[2] == squares[4] == squares[6] == side:
        winner = 'You'
        return True
    elif squares[0] == squares[4] == squares[8] == computer_side or squares[2] == squares[4] == squares[6] == computer_side:
        winner = 'Computer'
        return True
    else:
        return False
def show_board(board):
    for i in range(len(squares)):
        if i == 2 or i == 5:
            board += f' {squares[i]}\n ---------\n'
        elif i == 8:
            board += f' {squares[i]}\n'
        else:
            board += f' {squares[i]} |'

    print(board)


show_board(board)
def user_turn():
    try:
        square = int(input("Choose a square to put your figure in  "))
    except ValueError:
        print("You didn't follow the instructions, so computer will choose square for you")
        square = random.choice(squares)

    squares[square-1] = side
    print('Your turn: ')
    show_board(board)


def computer_turn():
    free_squares = []
    for item in squares:
        try:
            int(item)
            free_squares.append(item)
        except ValueError:
            pass

    try:
        computer_square = random.choice(free_squares)
        squares[computer_square-1] = computer_side
        print('Computer turn: ')
        show_board(board)
    except IndexError:
        win = check_winner()
        if win:
            pass
        else:
            print('Draw!')


while True:
    user_turn()
    computer_turn()
    win = check_winner()
    if win:
        print(f'{winner} won!')
        break
again = input("Want to start again (y/n)? ")
if again == 'y':
    os.system('python "C:/Users/ihobo/PycharmProjects/tictactoe/main.py"')
