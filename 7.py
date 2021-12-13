import pygal

def parse_input(filename):
    positions = []
    with open(filename) as file:
        positions = file.readline().split(",")
        positions = list(map(lambda x: int(x), positions))
    return positions


def visualize_consumption(positions):
    
    # Generate data for every possible guess
    data = []
    guess = 0
    while guess <= max(positions):
        data.append(get_fuel_at_value(positions, guess)[0])
        guess += 1
    
    chart = pygal.Line()
    chart.title = "Fuel cost"
    chart.x_labels = map(str, range(max(positions)))
    chart.add("fuel cost", data)
    chart.render_to_file('./tmp/chart.svg')


def get_fuel_at_value(positions, guess):
    cost = 0
    cost_left = 0
    cost_right = 0
    for crab in positions: # n time
        fuel = crab - guess
        cost += (abs(fuel) * (abs(fuel) + 1))//2
        if fuel > 0:
            cost_right += fuel
        elif fuel < 0:
            cost_left += abs(fuel)
    return (cost, cost_left, cost_right)


def optimize_fuel(positions):
    guess = max(positions) // 2 #Start guessing at the middle of the field
    ## This ensures it will take len(positions)/2 guesses at most to find the
    ## best solution

    previous_cost = 0
    cost = -1
    while cost < previous_cost:
        previous_cost = cost
        
        if cost_left > cost_right:
            guess += 1
        elif cost_left < cost_right:
            guess -= 1
        if previous_cost == -1:
            previous_cost = cost
            cost -= 1
    return (guess, previous_cost)