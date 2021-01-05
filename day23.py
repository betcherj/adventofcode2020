

def crab_cup_game_move(cups, current_cup_index):
    cur_cup = cups[current_cup_index]
    grabbed = cups[current_cup_index+1:current_cup_index+4]
    cups = cups[:current_cup_index+1] + cups[current_cup_index+4:]
    max_label = max(cups)
    min_label = min(cups)
    dest_label = cur_cup-1
    try:
        dest_index = cups.index(dest_label)
    except:
        dest_index = -1

    while dest_index == -1:
        dest_label -= 1
        if dest_label < min_label:
            dest_label = max_label
        elif dest_label > max_label:
            dest_label = min_label
        try:
            dest_index = cups.index(dest_label)
        except:
            dest_index = -1
    cups = cups[:dest_index+1] + grabbed + cups[dest_index+1:]
    return cups, dest_index+1


if __name__ == "__main__":
    #TODO finish this
    cups = [1,2,3,4,8,7,5,9,6]
    cups = [3,8,9,1,2,5,4,6,7]
    dest_index = 0
    for i in range(9):
        cups, dest_index = crab_cup_game_move(cups, dest_index)
    print(cups)