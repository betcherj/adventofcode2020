def count_any_ys(group_answers):
    count = [0]*26
    for participant_answers in group_answers:
        for answer in participant_answers:
            val = ord(answer)-97
            count[val] = count[val] | 1

    return sum(count)

def count_all_ys(group_answers):
    count = [0]*26
    for participant_answers in group_answers:
        for answer in participant_answers:
            val = ord(answer)-97
            count[val] +=  1
    all_ys = [x for x in count if x == len(group_answers)]
    return len(all_ys)


#26 possible
if __name__=="__main__":
    plane_answers = []
    with open('day6.txt', 'r') as f:
        contents = f.read()
        plane_answers = contents.split('\n\n')
    count = 0
    for i in plane_answers:
        group_answers = i.replace('\n', ' ').split(' ')
        count += count_all_ys(group_answers)
    print(count)