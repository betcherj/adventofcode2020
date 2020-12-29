
def find_departure_time(earliest_departure, schedule):
    num_busses = len(schedule)
    times_before_earliest = [earliest_departure%schedule[i] for i in range(num_busses)]
    final_times = [earliest_departure-times_before_earliest[m]+schedule[m] for m in range(num_busses)]
    dex = final_times.index(min(final_times))
    return (min(final_times)-earliest_departure)*schedule[dex]

def find_consecutive_bf(schedule, indicies):
    #This is really slow
    increment = schedule[0]
    ptr = 0
    Found = False
    while not Found:
        ptr+=increment
        Found = True
        for i in range(1, len(schedule)):
            if (ptr + indicies[i]) % schedule[i] != 0:
                Found = False
                break
    return ptr

def find_consecutive(schedule, indicies):
    Found = False
    ptr = 0
    while not Found:
        ptr += schedule[0]
        for i in range(1, len(schedule)):
            Found = True
            if (ptr+indicies[i])%schedule[i] != 0:
                Found = False
                break
    return ptr

if __name__ == "__main__":
    schedule = None
    earliest_departure = None
    with open("day13.txt", "r") as f:
        contents = f.read().split('\n')
        earliest_departure = int(contents[0])
        #Part1 input parsing
        #schedule = [int(x) for x in contents[1].split(',') if x != 'x']
        #Part2Input parsing
        times = contents[1].split(',')
        schedule = [int(x) for x in times if x != 'x']
        indicies = [int(j) for j in range(len(times)) if times[j] != 'x']
    #Part1
    #print(find_departure_time(earliest_departure, schedule))
    #Part2
    #Todo look into chinese remainder theorem 



