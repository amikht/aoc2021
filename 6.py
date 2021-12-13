def parse_input(filename):
    with open(filename, "r") as file:
        state = [int(x) for x in file.readline().split(",")]
    counts = [0 for x in range(9)]
    for fish in state:
        counts[fish] += 1
    return counts


def step(counts):
    """
    Performs one iteration ("day") in the lanternfish simulation.
    Modifies state in-place. Return None.

    Realizing that I could do this without having to individually
    keep track of every fish was revolutionary. I had to switch because
    keeping track of every fish was ballooning the size of the array
    I had to manage and the time complexity of this function beyond belief.
    By only keeping track of *how many* fish are in each possible state,
    I can maintain constant space and time complexity for this function.
    Infinite scalability!
    """
    new_fish = counts[0]
    for x in range(8):
        counts[x] = counts[x+1]
    counts[6] += new_fish
    counts[8] = new_fish

if __name__=="__main__":
    filename = input("Enter input file path >>>")
    state = parse_input(filename)
    print(state)
    steps = int(input("How many days to simulate? >>>"))
    for x in range(steps):
        step(state)
    print(sum(state))