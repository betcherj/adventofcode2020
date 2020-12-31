
def consolidate_ranges(ranges):
    #assumes sorted list is received
    ptr = 0
    consolidated_ranges = []
    while ptr<len(ranges)-1:
        element = ranges[ptr]
        high = element[1]
        low = element[0]
        while ptr<len(ranges) and high>=ranges[ptr][0]:
            if high<=ranges[ptr][1]:
                high = ranges[ptr][1]
            ptr+=1

        ptr += 1
        consolidated_ranges.append((low, high))

    return consolidated_ranges



def find_ranges(rules):
    ranges = []
    for row in rules:
        name, temp = row.split(':')[:]
        temp_ranges = temp.strip(' ').split(' or ')
        for range in temp_ranges:
            low, high = range.split('-')[:]
            ranges.append((int(low), int(high)))
    ranges.sort(key=lambda x:x[0])
    ranges = consolidate_ranges(ranges)
    return ranges

def check_in_ranges(num, ranges):
    for range in ranges:
        if num>=range[0] and num<=range[1]:
            return True
    return False

def find_completly_invalid(rules, nearby_tickets):
    #outside_range = []
    valid_ticks = []

    ranges = find_ranges(rules)
    for item in nearby_tickets:
        flag = True
        fields = item.split(',')
        for val in fields:
            if not check_in_ranges(int(val), ranges):
                #outside_range.append(int(val))
                flag = False
                break
        if flag:
            valid_ticks.append(item)
    return valid_ticks
    #return sum(outside_range)

def find_invalid(rule_index, rules, tickets):
    possibilities = [1]*len(rules)
    ranges = []
    row = rules[rule_index]
    name, temp = row.split(':')[:]
    temp_ranges = temp.strip(' ').split(' or ')
    for item in temp_ranges:
        low, high = item.split('-')[:]
        ranges.append((int(low), int(high)))

    for item in tickets:
        fields = item.split(',')
        for i in range(len(fields)):
            if not check_in_ranges(int(fields[i]), ranges):
                possibilities[i] &= 0
    return possibilities

def match_categories(rules, tickets):
    invalid_spots = []
    invalid_spots_and_sums = []

    for i in range(len(rules)):
        invalid_spots.append(find_invalid(i, rules, tickets))
    for j in range(len(invalid_spots)):
        invalid_spots_and_sums.append([sum(invalid_spots[j]), invalid_spots[j], j])
    invalid_spots_and_sums.sort(key = lambda x: x[0])
    rule_assigned = [False]*len(rules)
    rules_to_fields = [-1]*len(rules)

    for p in range(len(rules)):
        invalid_spot_item = invalid_spots_and_sums[p][1]
        real_rule_index = invalid_spots_and_sums[p][2]
        for m in range(len(invalid_spot_item)): #This should be num rules
            if invalid_spot_item[m] and not rule_assigned[m]:
                rule_assigned[m] = True
                rules_to_fields[real_rule_index] = m

    return rules_to_fields





if __name__ == "__main__":
    import time
    start = time.time_ns()
    with open('day16.txt', 'r') as f:
        contents = f.read().split('\n\n')
        fields = contents[0].split('\n')
        your_ticket = contents[1].split('\n')[1:]
        your_ticket = your_ticket[0].split(',')
        nearby_tickets = contents[2].split('\n')[1:]
    valid_tickets = find_completly_invalid(fields, nearby_tickets)
    rules_to_fields = match_categories(fields, valid_tickets)
    total = 1
    #Question asks to multiple first 6 feilds once translated
    for i in range(6):
        total = total * int(your_ticket[rules_to_fields[i]])
    end = time.time_ns()
    print(total)
    print((end-start)/1000000)