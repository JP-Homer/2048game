from utilities import generate_piece, print_board

DEV_MODE = False

valid_inputs = ['w', 'a', 's', 'd', 'q']

    

def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    piece = generate_piece(game_board)
    game_board[piece["row"]][piece["column"]] = piece["value"]
    
    print_board(game_board)
    print()

    while True:
        comp_piece = generate_piece(game_board)
        game_board[comp_piece["row"]][comp_piece["column"]] = comp_piece["value"]
        # check to see if the game is over using the game_over function
        if game_over(game_board) == True:
            print("You lose.")

        print_board(game_board)
        print()
        
        game_board_updated = [[], [], [], []]
        for index, row in enumerate(game_board):
            for cell in row:
                game_board_updated[index].append(cell)
        quit = 0
        while game_board == game_board_updated:
            inp1 = input()
            while inp1 not in valid_inputs:
                inp1 = input()
            if inp1 == 'q':
                quit += 1
                print("Goodbye")    
                break
            if inp1 == 'w':
                col1 = []
                col2 = []
                col3 = []
                col4 = []
                row1 = []
                row2 = []
                row3 = []
                row4 = []
                for row in game_board:
                    for index, cell in enumerate(row):
                        if index == 0:
                            col1.append(cell)
                        elif index == 1:
                            col2.append(cell)
                        elif index == 2:
                            col3.append(cell)
                        elif index == 3:
                            col4.append(cell)
                col_game_board = [col1, col2, col3, col4]

                for row in col_game_board:
                    for cell in row[:]:
                        if cell == 0:
                            row.remove(cell)
                for row in col_game_board:
                    for index, cell in enumerate(row):
                        if row.count(cell) > 1 and index != (len(row) - 1):
                            if cell == row[index + 1]:
                                row[index] = cell + cell
                                row.pop(index + 1)
                    for row in col_game_board[:]:
                        while len(row) < 4:
                            row.append(0)

                for row in col_game_board:
                    for index, cell in enumerate(row):
                        if index == 0:
                            row1.append(cell)
                        elif index == 1:
                            row2.append(cell)
                        elif index == 2:
                            row3.append(cell)
                        elif index == 3:
                            row4.append(cell)
                game_board = [row1, row2, row3, row4]
            elif inp1 == 's':
                col1 = []
                col2 = []
                col3 = []
                col4 = []
                row1 = []
                row2 = []
                row3 = []
                row4 = []

                for row in game_board:
                    for index, cell in enumerate(row):
                        if index == 0:
                            col1.append(cell)
                        elif index == 1:
                            col2.append(cell)
                        elif index == 2:
                            col3.append(cell)
                        elif index == 3:
                            col4.append(cell)
                col_game_board = [col1, col2, col3, col4]

                for row in col_game_board:
                    for cell in row[:]:
                        if cell == 0:
                            row.remove(cell)
                for row in col_game_board:
                    row.reverse()
                for row in col_game_board:
                    for index, cell in enumerate(row):
                        if row.count(cell) > 1 and index != (len(row) - 1):
                            if cell == row[index + 1]:
                                row[index] = cell + cell
                                row.pop(index + 1)
                for row in col_game_board:
                    row.reverse()
                for row in col_game_board[:]:
                    while len(row) < 4:
                        row.insert(0, 0)

                for row in col_game_board:
                    for index, cell in enumerate(row):
                        if index == 0:
                            row1.append(cell)
                        elif index == 1:
                            row2.append(cell)
                        elif index == 2:
                            row3.append(cell)
                        elif index == 3:
                            row4.append(cell)
                game_board = [row1, row2, row3, row4]
            elif inp1 == 'a':
                for row in game_board:
                    for cell in row[:]:
                        if cell == 0:
                            row.remove(cell)
                for row in game_board:
                    for index, cell in enumerate(row):
                        if row.count(cell) > 1 and index != (len(row) - 1):
                            if cell == row[index + 1]:
                                row[index] = cell + cell
                                row.pop(index + 1)
                for row in game_board[:]:
                    while len(row) < 4:
                        row.append(0)          
            elif inp1 == 'd':
                for row in game_board:
                    for cell in row[:]:
                        if cell == 0:
                            row.remove(cell)
                for row in game_board:
                    row.reverse()
                for row in game_board:
                    for index, cell in enumerate(row):
                        if row.count(cell) > 1 and index != (len(row) - 1):
                            if cell == row[index + 1]:
                                row[index] = cell + cell
                                row.pop(index + 1)
                for row in game_board:
                    row.reverse()
                for row in game_board[:]:
                    while len(row) < 4:
                        row.insert(0, 0)
        if quit > 0:
            break
        stop = 0
        for row in game_board:
            for cell in row:
                if cell == 2048:
                    stop += 1
                    print("You win")    
        if stop > 0:
            break
        print_board(game_board)
        print()

    return game_board


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    for row in game_board:
        for cell in row:
            if cell == 0:
                return False
    
    list1 = []
    for row in game_board:
        for index, cell in enumerate(row):
            if index != (len(row) - 1):
                if cell != row[index + 1]:
                    list1.append('break')
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    for row in game_board:
        for index, cell in enumerate(row):
            if index == 0:
                col1.append(cell)
            elif index == 1:
                col2.append(cell)
            elif index == 2:
                col3.append(cell)
            elif index == 3:
                col4.append(cell)
    col_game_board = [col1, col2, col3, col4]
    for row in col_game_board:
        for index, cell in enumerate(row):
            if index != (len(row) - 1):
                if cell != row[index + 1]:
                    list1.append('break')
    if len(list1) + 8 == 32:
        return True
    else:
        return False


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
