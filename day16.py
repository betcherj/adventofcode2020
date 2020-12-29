
def consolidate_ranges(ranges):
    #Todo think about how best to do this
    ranges.sort(key=lambda x : x[0])
    consolidated_ranges = []
    # for i in ranges:
    #     while i[0]<
    return consolidate_ranges



def find_ranges(rules):
    #Want to know if we will fall in this range
    # 12-100, 90-111 -> 12-111
    ranges = []
    for row in rules:
        name, temp = row.split(':')[:]
        temp_ranges = temp.strip(' ').split(' or ')
        for range in temp_ranges:
            low, high = range.split('-')[:]
            ranges.append((int(low), int(high)))
    ranges = consolidate_ranges(ranges)
    return ranges

def find_completly_invalid(neaby_tickets, ranges):
    return None

if __name__ == "__main__":
    with open('day16.txt', 'r') as f:
        contents = f.read().split('\n\n')
        fields = contents[0].split('\n')
        your_ticket = contents[1].split('\n')[1:]
        nearby_tickets = contents[2].split('\n')[1:]
    print(find_ranges(fields))