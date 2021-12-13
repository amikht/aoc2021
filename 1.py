def depth_counter(sonar_output):
    if len(sonar_output) == 0: return
    
    prev_depth = sonar_output[0]
    inc_counter = 0
    for depth in sonar_output[1:]:
        if depth > prev_depth:
            inc_counter += 1
        prev_depth = depth
    return inc_counter

def rolling_depth_counter(sonar_output):
    if len(sonar_output) == 0: return

    sonar_window = []
    prev_sum = -1
    inc_counter = 0

    for depth in sonar_output:
        
        sonar_window.append(depth)
        if len(sonar_window) > 3:
            sonar_window.pop(0)
        
        cur_sum = rolling_depth_helper(sonar_window)
        
        if cur_sum is None: continue
        elif cur_sum > prev_sum and prev_sum != -1:
            inc_counter += 1
        prev_sum = cur_sum
    return inc_counter
        


def rolling_depth_helper(sonar):
    if len(sonar) != 3: return None

    return sum(sonar)

if __name__ == "__main__":
    user_input = input("Enter a depth reading >")
    sonar = []
    while user_input != "":
        sonar.append(int(user_input))
        user_input = input("Enter a depth reading >")
    
    user_input = input("Choose a method (type corresponding letter):\na) Direct\nb) Rolling sum\n\n>>>")
    print(depth_counter(sonar)) if user_input == "a" else print(rolling_depth_counter(sonar))