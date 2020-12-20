


#TODO Make this faster
def sum_to(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False


def find_invalid(transmission, preamble_length):
    for i in range(preamble_length + 1, len(transmission)):
        nums = transmission[i - preamble_length:i]
        if not sum_to(nums, transmission[i]):
            return transmission[i]
    return -1



def continious_sum_to(nums, position, target):
    total =0
    for i in range(position, len(nums)):
        total += nums[i]
        if total == target:
            val_range = transmission[position:i+1]
            val_range.sort()
            print("Numbers are")
            print(nums[position], nums[i])
            print('val is ')
            print(val_range[0]+val_range[len(val_range)-1])
            return True
        elif total>target:
            return False
    return False


def find_continious(transmission, target):

    for i in range(len(transmission)):
        if continious_sum_to(transmission, i, target):
            return True
    return False

if __name__ == "__main__":
    preamble_length = 25
    target = 15690279
    transmission = []
    with open('day9.txt', 'r') as f:
        contents = f.read().split('\n')
        for i in contents:
            transmission.append(int(i))
    #print(find_invalid(transmission, 25))\
    print(find_continious(transmission, target))
