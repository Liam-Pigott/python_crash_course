import random


# helper functions
# takes input for player 1 to choose X or O
def select_marker():
    result = input("Please pick a marker 'X' or 'O'")
    if result.upper() != 'X' and result.upper() != 'O':
        return ''  # keeps the loop going until valid input is selected
    else:
        print(f'Player 1 has selected {result.upper()}')
        return result.upper()


# assign whatever marker is left to player2
def assign_p2_marker(p1):
    return 'X' if p1 == 'O' else 'O'


def clear_output():
    print('\n' * 100)


# print board in 3x3 grid, 123 top 456 middle, 789 bottom
def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('---------')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('---------')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('\n')


# takes input from the player and validates the move
def choose_position(board, player):
    position = input(f'Player {player} please enter a number: ')
    if position.lower() == 'q' or position.lower() == 'quit':
        return 'quit'
    elif int(position) in range(1, 10):
        # VALIDATION
        position = int(position)
        if is_valid_move(board, int(position)):
            return position
        else:
            print('Move is invalid, please choose another square!')
            return choose_position(board, player)
    else:
        print('Invalid input!')
        return choose_position(board, player)


# if the position has empty string, move is valid
def is_valid_move(board, pos):
    return board[pos] == ' '


def decide_first_go():
    # choose p1 or p2
    rand = random.randint(1, 2)
    print(f'Player {rand} gets the first move!')
    return rand


def print_welcome_message():
    print('\n\nWelcome to Tic Tac Toe!\n')
    print('Choose squares by entering numbers 1 - 9 where 1 is the top left square and 9 is the bottom right.\n')


# check that the are no empty string placeholders in the list
def full_board_check(board):
    return ' ' not in board


def win_check(board, mark):
    winning_combos = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9], [2, 5, 8]]
    result = False
    for combo in winning_combos:
        check = list(map(lambda num: board[num] == mark, combo))
        if False not in check:
            result = True
    return result


def mark_position(board, pos, mark):
    board[pos] = mark
    return board


# main game function
def start_game():
    print_welcome_message()

    # assign player markers
    player1 = ''
    while player1 == '':
        player1 = select_marker()
    # player1 has selected, assign player 2 as other option
    player2 = assign_p2_marker(player1)

    # player1 is 1, player2 is 2
    player_turn = decide_first_go()

    # control variable for game loop
    is_playing = True
    # init and maintain state of the board
    current_board = ['#'] + [' '] * 9

    # Main game loop
    while is_playing:
        clear_output()
        display_board(current_board)
        player_choice = choose_position(current_board, player_turn)
        if player_choice == 'quit':
            print('Quitting game...')
            break
        player_mark = player1 if player_turn == 1 else player2
        # valid move entered, update the current state of the game
        current_board = mark_position(current_board, player_choice, player_mark)
        # check for winning scenario
        has_won = win_check(current_board, player_mark)
        if has_won:
            # pretty print final outputs
            clear_output()
            display_board(current_board)
            print(f'Player {player_turn} is the winner!')
            restart = input(f'Would you like to play again? (Y/N)')
            if restart.upper() == 'Y':
                clear_output()
                start_game()
            else:
                break
        # nothing else to be seen here, can toggle the player turn now
        player_turn = 1 if player_turn == 2 else 2
        if full_board_check(current_board):
            print('No spaces, no winners. Starting the game again')
            start_game()


start_game()
