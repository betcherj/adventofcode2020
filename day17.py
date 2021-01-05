
def find_neighbors(cube):
    neighbors = []
    x, y, z = cube[:]
    for i in range(-1,2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i==0 and j == 0 and k ==0:
                    continue
                neighbors.append((x+i, y+j, k+z))
    return neighbors

def update_state(active_cubes):
    new_active_cubes = []
    active_neighbors = {}
    for cube in active_cubes:
        neighbors = find_neighbors(cube)
        for neighbor in neighbors:
            if neighbor in active_neighbors:
                active_neighbors[neighbor] +=1
            else:
                active_neighbors[neighbor] = 1
    for cube, active_neighbors in active_neighbors.items():
        if cube in active_cubes and (active_neighbors == 2 or active_neighbors ==3):
            new_active_cubes.append(cube)
        elif active_neighbors == 3:
            new_active_cubes.append(cube)
    return new_active_cubes

def find_neighbors_4d(cube):
    neighbors = []
    x, y, z, w = cube[:]
    for i in range(-1,2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1,2):
                    if i==0 and j == 0 and k ==0 and l ==0:
                        continue
                    neighbors.append((x+i, y+j, k+z, w+l))
    return neighbors

def update_state_4d(active_cubes):
    new_active_cubes = []
    active_neighbors = {}
    for cube in active_cubes:
        neighbors = find_neighbors_4d(cube)
        for neighbor in neighbors:
            if neighbor in active_neighbors:
                active_neighbors[neighbor] +=1
            else:
                active_neighbors[neighbor] = 1
    for cube, active_neighbors in active_neighbors.items():
        if cube in active_cubes and (active_neighbors == 2 or active_neighbors ==3):
            new_active_cubes.append(cube)
        elif active_neighbors == 3:
            new_active_cubes.append(cube)
    return new_active_cubes

if __name__=="__main__":
    active_cubes = []
    with open('day17.txt', 'r') as f:
        contents = f.read().split('\n')
        for i in range(len(contents)):
            for j in range(len(contents[0])):
                if contents[i][j] == "#":
                    active_cubes.append((j, i, 0, 0))
                    #active_cubes.append((j,i,0))
    # Part 1
    # for i in range(6):
    #     active_cubes = update_state(active_cubes)
    # print(len(active_cubes))

    for i in range(6):
        active_cubes = update_state_4d(active_cubes)
    print(len(active_cubes))