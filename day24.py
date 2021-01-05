

def find_tile(instruction):
    location = [0.0,0.0]
    ptr = 0
    while ptr<len(instruction):
        dir = instruction[ptr]
        ptr += 1
        if dir == 'n' or dir == 's':
            dir = dir + instruction[ptr]
            ptr +=1
        if dir == 'ne':
            location[0] +=.5
            location[1] += 1
        elif dir == 'nw':
            location[0] -=.5
            location[1] += 1
        elif dir == 'se':
            location[0] += .5
            location[1] -= 1
        elif dir == 'sw':
            location[0] -= .5
            location[1] -= 1
        elif dir == 'w':
            location[0] -= 1
        elif dir == 'e':
            location[0] += 1
    return location

def flip_tiles(instructions):
    previously_flipped = {}
    for insruction in instructions:
        tile_location = find_tile(insruction)
        key = str(tile_location[0]) + ',' + str(tile_location[1])
        if key in previously_flipped:
            del previously_flipped[key]
        else:
            previously_flipped[key] = True
    #Part1
    return list(previously_flipped.keys())
    #return len(list(previously_flipped.keys()))

def day_flip(black_tiles):
    new_black_tiles = []
    adj_black_tile_count = {} #{tile:adjacent_black_tiles
    adj_tiles = []
    for tile in black_tiles:
        x, y = tile.split(',')[:]
        x, y = float(x), float(y)
        #add potential while tiles (all directions)
        #Todo figure out why this isnt working
        adj_tiles.append(str(x+1) + ',' + str(y))
        adj_tiles.append(str(x + .5) + ',' + str(y+1))
        adj_tiles.append(str(x - .5) + ',' + str(y+1))
        adj_tiles.append(str(x - 1) + ',' + str(y))
        adj_tiles.append(str(x - .5) + ',' + str(y-1))
        adj_tiles.append(str(x + .5) + ',' + str(y-1))
        for other_tile in adj_tiles:
            if other_tile in adj_black_tile_count:
                adj_black_tile_count[other_tile] += 1
            else:
                adj_black_tile_count[other_tile] = 1
        adj_tiles = []
    for another_tile, count in adj_black_tile_count.items():
        # Black and should be kept black
        if another_tile in black_tiles and count > 0 and count <= 2:
            new_black_tiles.append(another_tile)
        # White and should be flipped
        elif count == 2:
            new_black_tiles.append(another_tile)
    return new_black_tiles

if __name__ == "__main__":
    with open('day24.txt', 'r') as f:
        insructions = f.read().split('\n')
    black_tiles = flip_tiles(insructions)
    print(len(black_tiles))
    days = 100
    for i in range(days):
        black_tiles = day_flip(black_tiles)
    print(len(black_tiles))

