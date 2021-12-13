def parse_input(input_file):
    lines = []
    with open(input_file) as file:
        lines = file.readlines()
        lines = list(map(lambda x: x.split(" -> "), lines))
        lines = [[[int(x) for x in el.split(",")] for el in y] for y in lines]
    return lines


def filter_lines(lines):
    """
    Only keeps lines in the list where x=x OR y=y
    """
    return [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]


def gen_line_coords(lines):
    """
    Generates a list of coordinates for each point containined in straight lines.
    Lines format -> list, each line is a list with start + end point
    """
    coords = []
    for pair in lines:
        if pair[0][0] == pair[1][0]: # x-direction matches
            direction = -(pair[0][1] - pair[1][1])//abs(pair[0][1] - pair[1][1])
            for y in range(pair[0][1], pair[1][1]+direction, direction):
                coords.append([pair[0][0], y])
        elif pair[0][1] == pair[1][1]: # y-direction matches
            direction = -(pair[0][0] - pair[1][0])//abs(pair[0][0] - pair[1][0])
            for x in range(pair[0][0], pair[1][0]+direction, direction):
                coords.append([x, pair[0][1]])
        else: # 45 degree
            distance = abs(pair[0][0] - pair[1][0]) + 1
            x_dir = -(pair[0][0] - pair[1][0])//abs(pair[0][0] - pair[1][0])
            y_dir = -(pair[0][1] - pair[1][1])//abs(pair[0][1] - pair[1][1])
            for x in range(distance):
                coords.append([pair[0][0] + x * x_dir, pair[0][1] + x * y_dir])
    return coords

def calculate_overlaps(coords):
    board = [[0 for x in range(1000)] for y in range(1000)]

    for coord in coords:
        board[coord[0]][coord[1]] += 1
    
    result = 0    
    for row in board:
        for x in row:
            if x > 1:
                result += 1
    
    return result


if __name__=="__main__":
    filename = input("Enter input file path >>>")
    coords = parse_input(filename)
    angles = input("Include lines at 45 degrees? (y/n) >>>")
    if angles == "y":
        coords = gen_line_coords(coords)
    else:
        coords = gen_line_coords(filter_lines(coords))
    print(calculate_overlaps(coords))