

def play_round(deck1, deck2):
    p1_card = deck1.pop(0)
    p2_card = deck2.pop(0)

    if p1_card > p2_card:
        deck1 += [p1_card, p2_card]
    elif p2_card > p1_card:
        deck2 += [p2_card, p1_card]
    else:
        print("shouldnt be here")
    return deck1, deck2

def score_deck(deck):
    score = 0
    deck = deck[::-1]
    for i in range(len(deck)):
        score += deck[i]*(i+1)
    return score

def play_game(deck1, deck2):

    while deck1 and deck2:
        deck1, deck2 = play_round(deck1, deck2)
    if not deck2:
        print("deck 1 wins")
        print(score_deck(deck1))
    else:
        print("deck 2 wins")
        print(deck2)
        print(score_deck(deck2))
if __name__ == "__main__":
    with open('day22.txt', 'r') as f:
        contents = f.read().split('\n\n')
        deck1 = [int(x) for x in contents[0].split('\n')[1:]]
        deck2 = [int(x) for x in contents[1].split('\n')[1:]]
    play_game(deck1, deck2)
    #Todo part 2