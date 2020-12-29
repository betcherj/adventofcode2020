
#Todo finish this

# def memory_game(target_index, starting_numbers):
#     #memory = [[0, 0] for i in range(max(starting_numbers)+1)]
#     memory = [0]*(max(starting_numbers)+1)
#     for num in range(len(starting_numbers)-1):
#         memory[starting_numbers[num]] = starting_numbers.index(starting_numbers[num])+1
#
#     last_number_spoken = starting_numbers[-1:][0]
#     for turn in range(len(starting_numbers)+1, target_index+1):
#         #print("TURN: " + str(turn) + " Last num spoken: " + str(last_number_spoken))
#
#         if len(memory)<last_number_spoken:
#             memory = memory + [0]*(last_number_spoken-len(memory)+1)
#         if memory[last_number_spoken] == 0:
#             #First time we have heard this number
#             memory[last_number_spoken] = turn
#             next_number = 0
#         else:
#             last_turn = turn -1 #Turn where the number was spoken
#             next_number = last_turn - memory[last_number_spoken]
#
#             if next_number == 0:
#                 next_number = 1
#
#             memory[last_number_spoken] = last_turn
#         # print("Next num: " + str(next_number))
#         # print('-------------------')
#         last_number_spoken = next_number
#     return last_number_spoken

def memory_game(rounds, starting_numbers):
    memory1 = [0]*10000
    memory2 = [0]*10000
    for i in range(len(starting_numbers)-1):
        memory1[starting_numbers[i]] = i
    last_num_said = starting_numbers[-1:][0]

    for round in range(len(starting_numbers), rounds):
        if memory1[last_num_said] == 0:
            memory1[last_num_said] = round-1
        else:
            memory2[last_num_said] = memory1[last_num_said] - memory2[last_num_said]

    return last_num_said

if __name__ == "__main__":
    starting_numbers = [0,3,6]
    rounds=10
    print(memory_game(rounds, starting_numbers))