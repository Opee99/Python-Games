import random
import time


board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

input_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

comp_input_to_win = [
        [4, 8, 2, 6, 1, 3],
        [4, 7, 0, 2],
        [4, 6, 0, 8, 5, 1],
        [4, 5, 0, 6],
        [0, 2, 6, 8, 1, 3, 5, 7],
        [4, 3, 2, 8],
        [4, 2, 0, 8, 3, 7],
        [4, 1, 6, 8],
        [4, 0, 6, 2, 5, 7, 3, 1]
    ]

comp_input_defend = [
        [0, 4, 8], [4, 8, 0], [0, 8, 4], [2, 4, 6], [2, 6, 4], [4, 6, 2],
        [0, 1, 2], [1, 2, 0], [0, 2, 1], [3, 4, 5], [3, 5, 4], [4, 5, 3], [6, 7, 8], [7, 8, 6], [6, 8, 7],
        [0, 3, 6], [0, 6, 3], [3, 6, 0], [1, 4, 7], [4, 7, 1], [1, 7, 4], [2, 5, 8], [5, 8, 2], [2, 8, 5]
    ]
x_corner = [[0, 8], [2, 6]]
x_middle = [[5, 6, 7], [5, 0, 1], [3, 2, 1], [3, 8, 7], [7, 0, 3], [7, 2, 5], [1, 6, 3], [1, 8, 5 ]]
x_diagonal = [[5, 7, 8], [5, 1, 2], [3, 1, 0], [3, 7, 6]]

list_of_o = []
list_of_x = []

# If game is still going
game_is_going = True

# Who won? or tie?
winner = None

# Whose turn is it
current_player = 'X'

# game option
game_option = None


def start_menu():
    global game_option
    game_option = int(input('Press 1 for Single/Computer\nPress 2 for Multiplayer\nOption : '))


def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def handle_turn(player):
    if game_option == 2:
        pos = input('Player {} turn:\nChoose a position from 1 - 9: '.format(player))
        if not pos:
            handle_turn(player)
        elif pos not in input_list:
            print(f'you entered "{pos}" not accepted!')
            handle_turn(player)
        else:
            position = int(pos)
            position -= 1
            if position < 0 or position > 8:
                print(f'Board {position + 1} is not available \n Enter again!')
                handle_turn(player)
            else:
                if board[position] != '-':
                    if current_player == board[position]:
                        print(f'you have already selected position {position + 1}')
                    else:
                        print(f"--- {position + 1} is occupied by {board[position]} ---")
                    handle_turn(player)
                else:
                    board[position] = player
                    display_board()
    elif game_option == 1 and player == 'X':
        pos = input('Your turn:\nChoose a position from 1 - 9: '.format(player))
        if not pos:
            handle_turn(player)
        elif pos not in input_list:
            print(f'you entered "{pos}" not accepted!')
            handle_turn(player)
        else:
            position = int(pos)
            position -= 1
            if position < 0 or position > 8:
                print(f'Board {position + 1} is not available \n Enter again!')
                handle_turn(player)
            else:
                if board[position] != '-':
                    if current_player == board[position]:
                        print(f'you have already selected position {position + 1}')
                    else:
                        print(f"--- {position + 1} is occupied by {board[position]} ---")
                    handle_turn(player)
                else:
                    board[position] = player
                    display_board()
    elif game_option == 1 and player == 'O':
        print('Computer turn')
        time.sleep(1)
        comp_pos = computer_turn()
        print(f'--- {comp_pos + 1} ---')
        board[comp_pos] = player
        display_board()


def computer_turn():
    # computer occupied list
    empty_list = []

    for i in range(len(board)):
        if board[i] == '-':
            empty_list.append(i)
        elif board[i] == 'X':
            list_of_x.append(i)
        elif board[i] == 'O':
            if i not in list_of_o:
                list_of_o.append(i)

    # random number from the empty list for 1st move
    if len(empty_list) > 7:
        comp_input = 4
        if board[comp_input] == '-':
            return comp_input
        else:
            comp_input = random.choice(empty_list)
            return comp_input
    else:
        move = computer_move(empty_list)
        return move


def computer_move(empty_list):
    count_list_x = len(list_of_x) - 1
    count_list_o = len(list_of_o) - 1
    if count_list_o > 0:
        # best for win
        for x in comp_input_defend:
            for y in list_of_o:
                for z in list_of_o:
                    if (y == x[0] and z == x[1]) or (y == x[0] and z == x[1]):
                        if board[x[2]] == '-':
                            print('win')
                            return x[2]

    if count_list_x > 0:
        # best if x in center
        for x in comp_input_defend:
            for y in list_of_x:
                for z in list_of_x:
                    if (y == x[0] and z == x[1]) or (y == x[0] and z == x[1]):
                        if board[x[2]] == '-':
                            print('defend')
                            return x[2]

    if count_list_x > 0:
        # best if o in center
        for x in list_of_x:
            for y in list_of_x:
                for z in x_corner:
                    if (x == z[0] and y == z[1]) or (x == z[1] and y == z[0]):
                        x_even = [1, 3, 5, 7]
                        random.shuffle(x_even)
                        for x_odd in x_even:
                            if board[x_odd] == '-':
                                print('defend')
                                return x_odd

    if count_list_x > 0:
        # best for Diagonal
        for x in list_of_x:
            for y in list_of_x:
                for z in x_diagonal:
                    if (x == z[0] and y == z[1]) or (x == z[1] and y == z[0]):
                        if board[z[2]] == '-':
                            print('defend-d')
                            return z[2]

    if count_list_x > 0:
        # best for L
        for x in list_of_x:
            for y in list_of_x:
                for z in x_middle:
                    if (x == z[0] and y == z[1]) or (x == z[1] and y == z[0]):
                        if board[z[2]] == '-':
                            print('defends')
                            return z[2]

    for i in list_of_o:
        for comp_no in comp_input_to_win[i]:
            if board[comp_no] == '-':
                return comp_no
    return random.choice(empty_list)


def check_if_game_over():
    global game_is_going
    check_for_winner()

    if winner == 'X' or winner == 'O':
        game_is_going = False
        print(f'--- Player {winner} won. ---')
    else:
        check_if_tie()


def check_if_tie():
    global game_is_going
    if board.count('X') + board.count('O') > 8:
        game_is_going = False
        print('--- tie. ---')


def check_for_winner():
    global winner
    # check row
    if check_rows():
        winner = current_player
    # check column
    elif check_column():
        winner = current_player
    # check diagonals
    if check_diagonal():
        winner = current_player


def check_rows():
    if board[0] == board[1] == board[2] != '-':
        return current_player
    elif board[3] == board[4] == board[5] != '-':
        return current_player
    elif board[6] == board[7] == board[8] != '-':
        return current_player
    return None


def check_column():
    if board[0] == board[3] == board[6] != '-':
        return current_player
    elif board[1] == board[4] == board[7] != '-':
        return current_player
    elif board[2] == board[5] == board[8] != '-':
        return current_player
    return None


def check_diagonal():
    if board[0] == board[4] == board[8] != '-':
        return current_player
    elif board[2] == board[4] == board[6] != '-':
        return current_player
    return None


def flip_player(player):
    global current_player
    if player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def play_game():
    # menu of the game
    start_menu()

    # Display initial game
    display_board()
    while game_is_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player(current_player)


play_game()

