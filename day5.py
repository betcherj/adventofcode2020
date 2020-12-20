
import math
import time
def binary_search2(seat_range, x):
    if len(x) == 1:
        if x == 'L':
            return seat_range[0]
        elif x == 'R':
            return seat_range[1]
    halfway = math.floor((seat_range[1] - seat_range[0])/2)+seat_range[0]
    if x[0] == "L":
        return binary_search2([seat_range[0], halfway], x[1:])
        #return [seat_range[0], halfway]
    elif x[0] == 'R':
        return binary_search2([halfway+1, seat_range[1]], x[1:])
        #return [halfway+1, seat_range[1]]

def binary_search(seat_range, x):
    if len(x) == 1:
        if x == 'F':
            return seat_range[0]
        elif x == 'B':
            return seat_range[1]
    halfway = math.floor((seat_range[1] - seat_range[0])/2)+seat_range[0]
    if x[0] == "F":
        return binary_search([seat_range[0], halfway], x[1:])
        #return [seat_range[0], halfway]
    elif x[0] == 'B':
        return binary_search([halfway+1, seat_range[1]], x[1:])
        #return [halfway+1, seat_range[1]]




if __name__ == "__main__":
    start = time.time_ns()
    rows = 127
    columns = 8
    tickets = []
    with open('day5.txt', 'r') as f:
        contents = f.read()
        tickets = contents.split('\n')
    all_ids = [x*8+j for x in range(0,128) for j in range(0,8)]

    for i in tickets:
        row = binary_search([0,127], i[:7])
        column = binary_search2([0,7], i[7:])
        val = row*8 + column
        #This is slow how to improve ?
        dex = all_ids.index(val)
        all_ids[dex] = 'x'
    for p in range(1, len(all_ids)-1):
        if all_ids[p-1] == 'x' and all_ids[p+1] == 'x' and all_ids[p] != 'x':
            print("Your ticket id is : " + str(all_ids[p]))
            end = time.time_ns()
            print(end-start)

