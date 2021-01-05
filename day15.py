
# def memory_game(rounds, starting_numbers):
#     memory1 = [0]*10000
#     memory2 = [0]*10000
#     for i in range(len(starting_numbers)-1):
#         memory1[starting_numbers[i]] = i
#     last_num_said = starting_numbers[-1:][0]
#
#     for round in range(len(starting_numbers), rounds):
#         if memory1[last_num_said] == 0:
#             memory1[last_num_said] = round-1
#         else:
#             memory2[last_num_said] = memory1[last_num_said] - memory2[last_num_said]
#
#     return last_num_said

def memory_game(rounds, starting_numbers):
    memory = {}
    for i in range(1, len(starting_numbers)):
        number = str(starting_numbers[i-1])
        if number in memory:
            last_round_spoken = memory[number][0]
            memory[number] = [i, last_round_spoken]
        else:
            memory[number] = [i, 0]
    last_number_spoken = str(starting_numbers[-1])
    for round in range(len(starting_numbers)+1, rounds+1):
        if last_number_spoken not in memory:
            memory[last_number_spoken] = [round-1, 0]
            to_say = 0
        else:
            last_round_spoken = memory[last_number_spoken][0]
            memory[last_number_spoken] = [round-1, last_round_spoken]
            to_say = round-1-int(last_round_spoken)
        last_number_spoken = str(to_say)
    return to_say



if __name__ == "__main__":
    import time
    start = time.time()
    starting_numbers = [1,0,15,2,10,13]
    rounds=30000000
    res = memory_game(rounds, starting_numbers)
    end = time.time()
    print(res)
    print(end-start)