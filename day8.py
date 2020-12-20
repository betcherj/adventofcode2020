import copy

def eval_ops(instructions,ptr, accumulator):
    '''Takes a code and returns a pointer to the next instruction'''
    op, val, visited = instructions[ptr][:]
    if visited:
        return -1
    #Mark as visited
    instructions[ptr][2] = True
    if op == 'acc':
        accumulator += val
        ptr+=1
    elif op == 'jmp':
        ptr+=val
    elif op == 'nop':
        ptr+=1

    if ptr == len(instructions):
        print("successfully terminated")
        return accumulator

    return eval_ops(instructions, ptr, accumulator)

def check_change(instructions, jmp_indexes, nop_indexes):
    '''checks if program terminates if we swap jmp for nop or nop for jump'''
    for i in jmp_indexes:
        mod_instructions = copy.deepcopy(instructions)
        mod_instructions[i][0] = 'nop'
        accumulator = eval_ops(mod_instructions, 0, 0)
        if accumulator != -1:
            return accumulator
    for j in nop_indexes:
        mod_instructions = copy.deepcopy(instructions)
        mod_instructions[j][0] = 'jmp'
        accumulator = eval_ops(mod_instructions, 0, 0)
        if accumulator != -1:
            return accumulator
    return -1


if __name__ == "__main__":
    instructions = []
    nop_indexes = []
    jmp_indexes = []
    with open('day8.txt', 'r') as f:
        contents = f.read().split('\n')
        for i in range(len(contents)):
            item = contents[i]
            #this will need to change if the instruction length is variable
            op = item[:3]
            if op == 'nop':
                nop_indexes.append(i)
            elif op == 'jmp':
                jmp_indexes.append(i)
            val = int(item[4:])
            instructions.append([op,val, False])

    print(check_change(instructions, jmp_indexes, nop_indexes))


