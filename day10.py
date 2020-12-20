
def chain_adaptors(adaptors):
    '''Assume we are getting a sorted list of adaptors'''
    last_adaptor_rating = 0
    one_jolt_count = 0
    three_jolt_count = 0
    for item in adaptors:
        if item-last_adaptor_rating == 1:
            one_jolt_count += 1
        elif item-last_adaptor_rating == 3:
            three_jolt_count +=1
        last_adaptor_rating = item

    return one_jolt_count*three_jolt_count
def chain_adaptors2(adaptors):
    #TODO finish this 
    three_in_a_row_ct = 0
    two_in_a_row_ct = 0
    for i in range(len(adaptors)-3):
        if adaptors[i] == adaptors[i+1]-1 and adaptors[i] == adaptors[i+2]-2:
            three_in_a_row_ct+=1
        elif adaptors[i] == adaptors[i+1]-1:
            two_in_a_row_ct += 1

    return 2**three_in_a_row_ct + two_in_a_row_ct


if __name__ == "__main__":
    adaptors = []
    with open('day10.txt', 'r') as f:
        contents = f.read().split('\n')
        adaptors = [int(x) for x in contents]
    adaptors.sort()
    adaptors = [0] + adaptors
    adaptors.append(adaptors[len(adaptors)-1]+3)
    print(chain_adaptors2(adaptors))
