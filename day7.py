
def can_contain_SG(contents_dict):
    return "shiny gold" in contents_dict.keys()


def check_bags(bags_dict):
    final_dict = bags_dict
    all_done = True
    for key, vals in bags_dict.items():
        if len(vals) > 1:
            all_done = False
        new_vals = []
        for val in vals:
            space_index = val.find(' ')
            num = val[:space_index]
            color = val[space_index+1:]
            if color == 'shiny gold':
                new_vals = ['1 shiny gold']
                break
            elif bags_dict[color] == ['1 shiny gold']:
                new_vals = ['1 shiny gold']
                break
            elif bags_dict[color]:
                new_vals.append(val)
        final_dict[key] = new_vals
    if all_done:
        return final_dict

    return check_bags(final_dict)

def check_bag_recs(bags_dict, bag_recs):
    #Need to subtract one from this due to top level shiny gold bag not being counted
    if not bag_recs:
        return 1
    total = 1
    for item in bag_recs:
        space_index = item.find(' ')
        num = item[:space_index]
        color = item[space_index+1:]
        total += int(num)*check_bag_recs(bags_dict, bags_dict[color])
    return total


if __name__ == "__main__":
    rules_dict = {}
    with open('day7.txt', 'r') as f:
        contents = f.read()
        lines = contents.split('\n')
        #Input parsing for part one
        # for line in lines:
        #     vals = []
        #     stop1 = line.index('bags contain')
        #     key = line[:stop1].strip(' ')
        #     if 'shiny gold' in key:
        #         continue
        #     elif 'shiny gold' in line:
        #         rules_dict[key] = ['1 shiny gold']
        #         continue
        #     elif 'no other' in line:
        #         rules_dict[key] = []
        #         continue
        #     stop2 = stop1 + len('bags contain')
        #     line = line[stop2:].strip(' ')
        #     stop3 = line.find(',')
        #     while stop3 != -1:
        #         vals.append(line[:stop3-4].strip(' '))
        #         line = line[stop3+1:]
        #         stop3 = line.find(',')
        #     vals.append(line[:-5].strip(' '))
        # final_dict = check_bags(rules_dict)
        # count = 0
        # for key, val in final_dict.items():
        #     if val == ['1 shiny gold']:
        #         count +=1
        for line in lines:
            vals = []
            stop1 = line.index('bags contain')
            key = line[:stop1].strip(' ')
            if 'no other' in line:
                rules_dict[key] = []
                continue
            stop2 = stop1 + len('bags contain')
            line = line[stop2:].strip(' ')
            stop3 = line.find(',')
            while stop3 != -1:
                vals.append(line[:stop3-4].strip(' '))
                line = line[stop3+1:]
                stop3 = line.find(',')
            vals.append(line[:-5].strip(' '))

            rules_dict[key] = vals
    shiny_gold_recs = rules_dict['shiny gold']
    print(check_bag_recs(rules_dict, shiny_gold_recs)-1)



