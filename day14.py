

def get_binary_rep(num):
    rep = '{0:b}'.format(num)
    dif = 36-len(rep)
    if dif>0:
        rep = '0'*dif+rep
    return rep


#
# def write_to_memory(cmds):
#     total = 0
#     mask = 0
#     memory = {}
#     for cmd in cmds:
#         if cmd[:4] == "mask":
#             mask = cmd.split('=')[1].strip(' ')
#         else:
#             op, val = cmd.split(' = ')[:]
#             binary_str = get_binary_rep(int(val))
#             location = int(op[op.index('[')+1:op.index(']')])
#             res = ''
#             for i in range(36):
#                 if mask[i] != 'X':
#                     res = res + mask[i]
#                 else:
#                     res = res + binary_str[i]
#             memory[location] = int(res, 2)
#     for key, val in memory.items():
#         total += val
#     return total

def get_mem_addresses(result):
    memory_address=[result[35]]
    if result[35] == 'X':
        memory_address = ['0','1']
    for i in range(34, -1,-1):
        if result[i] == 'X':
            temp_addresses = memory_address.copy()
            memory_address = memory_address + temp_addresses
            half = len(memory_address)/2
            for j in range(len(memory_address)):
                if j < half:
                    memory_address[j] = '0' + memory_address[j]
                else:
                    memory_address[j] = '1' + memory_address[j]
        else:
            for j in range(len(memory_address)):
                memory_address[j] = result[i] + memory_address[j]
    return memory_address


def write_to_memory_2(cmds):
    total = 0
    mask = 0
    memory = {}
    for cmd in cmds:
        if cmd[:4] == "mask":
            mask = cmd.split('=')[1].strip(' ')
        else:
            op, val = cmd.split(' = ')[:]
            location = int(op[op.index('[') + 1:op.index(']')])
            binary_str = get_binary_rep(int(location))
            res = ''
            for i in range(36):
                if mask[i] != '0':
                    res = res + mask[i]
                else:
                    res = res + binary_str[i]
            write_locations = get_mem_addresses(res)
            for spot in write_locations:
                int_rep = int(spot, 2)
                memory[int_rep] = int(val)
    for key, val in memory.items():
        total += val
    return total

if __name__ == "__main__":
    with open('day14.txt', 'r') as f:
        cmds = f.read().split("\n")
    #print(write_to_memory(cmds))
    print(write_to_memory_2(cmds))