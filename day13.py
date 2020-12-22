import functools

def find_departure_time(earliest_departure, schedule):
    num_busses = len(schedule)
    times_before_earliest = [earliest_departure%schedule[i] for i in range(num_busses)]
    final_times = [earliest_departure-times_before_earliest[m]+schedule[m] for m in range(num_busses)]
    dex = final_times.index(min(final_times))
    return (min(final_times)-earliest_departure)*schedule[dex]


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
        schedule2 = [[times[i], i] for i in range(len(times)) if times[i] != 'x']
    #Part1
    #print(find_departure_time(earliest_departure, schedule))
    #Part2
    #TODO Part two 
    print(schedule2)

