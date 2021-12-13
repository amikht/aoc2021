BINGO_SIZE = 5

def load_data(file):
    """
    input -> text file
    output -> (arr<int> bingo_numbers, arr<arr<int>> bingo_boards)
    """
    with open(file, "r") as file_obj:
        data = file_obj.read().split("\n\n")
        # Cast all bingo numbers provided to integers for easy comparison.
        bingo_numbers = list(map(lambda x: int(x), data[0].split(",")))
        bingo_boards = []
        for board in data[1:]:
            # Parse down all the white space to turn the bingo boards into lists
            # After they are parsed, map all the strings to numbers for math later
            bingo_boards.append([list(map(lambda x: int(x), row.split())) for row in board.split("\n")])
        
        return (bingo_numbers, bingo_boards)

def gen_board_state(num_boards):
    """
    input -> Number of bingo boards recieved
    output -> arr<arr<bool>> bingo_state initialized to false
    """
    bingo_state = []
    for i in range(num_boards):
        bingo_state.append([[False for i in range(BINGO_SIZE)] for i in range(BINGO_SIZE)])
    return bingo_state

def draw_number(num, boards, state):
    for i in range(len(boards)):
        for j in range(BINGO_SIZE):
            for k in range(BINGO_SIZE):
                if boards[i][j][k]==num:
                    state[i][j][k] = True


def check_boards_for_bingos(state):
    """
    input -> current bingo boards state
    output -> index of board where a bingo has occurred, or -1 for failure
    """
    bingos = []
    for i in range(len(state)):
        # check rows
        for j in range(BINGO_SIZE):
            skipped_row = False
            skipped_col = False
            for k in range(BINGO_SIZE):
                if state[i][j][k] == False:
                    skipped_row = True
                if state[i][k][j] == False:
                    skipped_col = True
            if not skipped_row or not skipped_col:
                bingos.append(i) # Save the board where the bingo was found
                break # If a row or col was completed w/o getting false, a bingo was found. Break.

    return bingos


def calc_bingo_value(num, board, state):
    """
    input -> bingo board, bingo board state (one board)
    """
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not state[i][j]:
                total += board[i][j]
    return num * total


def find_first_winner(nums, boards):
    state = gen_board_state(len(boards))
    result = 0
    while nums:
        draw_number(nums[0], boards, state)
        bingo = check_boards_for_bingos(state)
        if bingo != []:
            result = calc_bingo_value(nums[0], boards[bingo[0]], state[bingo[0]])
            break
        else:
            nums = nums[1:]
    return result


def find_last_winner(nums:list, boards:list):
    state = gen_board_state(len(boards))
    nums_index = 0
    last_bingo_index = 0
    bingos = []


    while nums_index < len(nums) - 1:
        draw_number(nums[nums_index], boards, state)
        new_bingos = check_boards_for_bingos(state)
        if new_bingos != []:
            last_bingo_index = nums_index
            bingos = [(boards[i], state[i]) for i in range(len(boards)) if i in new_bingos]
            boards = [boards[i] for i in range(len(boards)) if i not in new_bingos]
            state = [state[i] for i in range(len(state)) if i not in new_bingos]
        nums_index += 1

    # Does the final board have a bingo?
    return calc_bingo_value(nums[last_bingo_index], bingos[-1][0], bingos[-1][1])


if __name__ == "__main__":
    filename = input("Enter bingo game file path >>>")
    nums, boards = load_data(filename)
    choice = input("Enter board to find:\n1) First winner\n2) Last winner\n\n>>>")
    if choice=="1":
        print(find_first_winner(nums, boards))
    else:
        print(find_last_winner(nums, boards))
