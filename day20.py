

def check_match(edge1, edge2):
    normal = True
    reflected = True
    for i in range(len(edge1)):
        if edge1[i] != edge2[i]:
            normal = False
            break
    edge1 = edge1[::-1]
    for j in range(len(edge1)):
        if edge1[j] != edge2[j]:
            reflected = False
            break
    return normal or reflected

def check_is_corner(id, tile, tile_dict):
    matched = [0, 0, 0, 0]
    res = True
    for other_id, other_tile in tile_dict.items():
        if id == other_id:
            continue
        for i in range(4):
            if check_match(tile[i], other_tile[0]):
                matched[i] = 1
            elif check_match(tile[i], other_tile[1]):
                matched[i] =1
            elif check_match(tile[i], other_tile[2]):
                matched[i] = 1
            elif check_match(tile[i], other_tile[3]):
                matched[i] = 1
        if sum(matched)>2:
            res = False
            break
    return res

def find_corners(tiles_dict):
    corners = []
    for id, tile in tiles_dict.items():
        if check_is_corner(id, tile, tile_dict):
            corners.append(id)
    return corners

def parse_tiles(contents):
    #tile_dict {id: [top, bottom, left, right]}
    tile_dict = {}
    for item in contents:
        rows = item.split('\n')
        id = rows[0][:-1].split(' ')[1]
        rows = rows[1:]
        top = rows[0]
        bottom = rows[len(rows)-1]
        left = ''
        right = ''
        for row in rows:
            left+= row[0]
            right += row[len(row)-1]
        tile_dict[id] = [top, bottom, left, right]
    return tile_dict

if __name__ == "__main__":
    with open('day20.txt', 'r') as f:
        contents = f.read().split('\n\n')

    tile_dict = parse_tiles(contents)
    corners = find_corners(tile_dict)
    # Part 1
    # total = 1
    # for corner in corners:
    #     total = total * int(corner)
    # print(total)
    # Part 2
    #TODO
