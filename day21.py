

def count_instances(recipes, all_allergens, all_ingredients):
    y_to_x = dict.fromkeys(all_allergens)

    for item in recipes:
        allergens, ingredients = item[0].copy(), set(item[1])

        for allergen in allergens:
            if y_to_x[allergen] == None:
                y_to_x[allergen] = list(ingredients)
            else:
                y_to_x[allergen] = list(set(y_to_x[allergen]).intersection(ingredients))
    to_remove = set()
    done = False
    while not done:
        done = True
        new_y_to_x = y_to_x
        for key, val in list(y_to_x.items()):
            if len(val) == 1:
                to_remove.add(val[0])
            else:
                done = False
                new_val = []
                for item in val:
                    if item not in to_remove:
                        new_val.append(item)
                new_y_to_x[key] = new_val
        y_to_x = new_y_to_x

    sorted_keys = sorted(y_to_x)
    cannonical_dangerous = ''
    for k in sorted_keys:
        cannonical_dangerous += y_to_x[k][0] + ','
    return cannonical_dangerous[:-1]

       #part 1
    # potential_allergens = []
    # for i in y_to_x.values():
    #     potential_allergens += i
    # potential_allergens = list(set(potential_allergens))
    # not_allergens = [x for x in all_ingredients if x not in potential_allergens]
    # return len(not_allergens)

if __name__ == "__main__":
    import time
    start_time = time.time_ns()
    recipies = []
    all_allergens = []
    all_ingredients = []

    with open('day21.txt', 'r') as f:
        contents = f.read().split('\n')
        for i in contents:
            start = i.find('(')
            ingredients = i[:start].strip(' ').split(' ')
            allergens = i[start+10:-1].split(', ')
            all_allergens += allergens
            all_ingredients += ingredients
            recipies.append((allergens, ingredients))
    all_allergens = set(all_allergens)
    res = count_instances(recipies, all_allergens, all_ingredients)
    end_time = time.time_ns()
    print(res)
    print((end_time-start_time/1000000))


