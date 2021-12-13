def parse_instruction(ins):
    ins = ins.lower().split(" ")
    
    return {"pos": int(ins[1]), "depth":0} if ins[0] == "forward" else {"depth": int(ins[1]) * {"down": 1, "up": -1}[ins[0]], "pos":0}

def pilot(ins_arr):
    depth = 0
    pos = 0

    for ins in ins_arr:
        ins = parse_instruction(ins)
        depth += ins["depth"]
        pos += ins["pos"]
    
    return depth * pos

def pilot_aim(ins_arr):
    depth = 0
    pos = 0
    aim = 0

    for ins in ins_arr:
        ins = parse_instruction(ins)
        if ins["pos"] == 0:
            aim += ins["depth"]
        else:
            pos += ins["pos"]
            depth += aim * ins["pos"]
    
    return depth * pos

if __name__ == "__main__":
    user_input = input("Enter an instruction (enter to finish) >")
    instructions = []
    while user_input != "":
        instructions.append(user_input)
        user_input = input("Enter a depth reading >")

    user_input = input("Choose a method (type corresponding letter):\na) No aim\nb) Aim\n\n>>>")
    
    print(pilot(instructions)) if user_input == "a" else print(pilot_aim(instructions))