def binary_to_dec(binary_arr: list):
    result = 0
    for i in range(len(binary_arr)-1, -1, -1):
        result += int(binary_arr[i]) * pow(2, len(binary_arr) - (i+1))
    return result


def gamma_rate(diagnostics: list):
    # Create a list with as many elements as the input has bits 
    sum_lst = [0 for i in range(len(diagnostics[0]))]
    for val in diagnostics:
        for i in range(len(val)):
            sum_lst[i] += int(val[i])

    
    return [0 if val / len(diagnostics) < 0.5 else 1 for val in sum_lst]


def epsilon_rate(gamma_rate: list):
    return [0 if i==1 else 1 for i in gamma_rate]


def power_consuption(gamma_rate: list, epsilon_rate: list):
    return binary_to_dec(gamma_rate) * binary_to_dec(epsilon_rate)


def oxygen_rating(diagnostics: list):
    cur_bit = 0
    while len(diagnostics) > 1:
        bit_sum = 0
        for val in diagnostics:
            bit_sum += int(val[cur_bit])
        most_common_bit = 0 if bit_sum / len(diagnostics) < 0.5 else 1
        diagnostics = list(filter(lambda x: int(x[cur_bit]) == most_common_bit, diagnostics))
        cur_bit += 1
    return binary_to_dec(diagnostics[0])


def co2_rating(diagnostics: list):
    cur_bit = 0
    while len(diagnostics) > 1:
        bit_sum = 0
        for val in diagnostics:
            bit_sum += int(val[cur_bit])
        least_common_bit = 1 if bit_sum / len(diagnostics) < 0.5 else 0
        diagnostics = list(filter(lambda x: int(x[cur_bit]) == least_common_bit, diagnostics))
        cur_bit += 1
    return binary_to_dec(diagnostics[0])


def life_support(o2, co2):
    return o2*co2

if __name__ == "__main__":
    user_input = input("Enter diagnostics >>>")
    diagnostics = []
    while user_input != "":
        diagnostics.append(user_input)
        user_input = input("Enter diagnostics >>>")
    
    gamma = gamma_rate(diagnostics)
    oxygen = oxygen_rating(diagnostics)
    co2 = co2_rating(diagnostics)

    print("Power Consumption: " + str(power_consuption(gamma, epsilon_rate(gamma))))
    print("Life support rating: " + str(life_support(oxygen, co2)))
