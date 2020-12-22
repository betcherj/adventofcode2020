import copy
import numpy

def calculate_adjacents(grid):
    adj_occupied = numpy.zeros((len(grid), len(grid[0])), dtype=int)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                continue
            elif grid[i][j] == "L":
                continue
            elif grid[i][j] == "#":
                if i>0 and j>0:
                    adj_occupied[i-1][j-1] +=1
                if i>0:
                    adj_occupied[i-1][j] +=1
                if j>0:
                    adj_occupied[i][j-1] +=1
                if i<len(grid)-1 and j<(len(grid[0])-1):
                    adj_occupied[i+1][j+1] += 1
                if i<len(grid)-1:
                    adj_occupied[i+1][j] +=1
                if j<len(grid[0])-1:
                    adj_occupied[i][j+1] += 1
                if i<len(grid)-1 and j>0:
                    adj_occupied[i+1][j-1] +=1
                if i>0 and j<len(grid[0])-1:
                    adj_occupied[i-1][j+1] +=1
    return adj_occupied


def update_grid(grid, adj_occupied):
    changed = False
    occupied_count = 0
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "L" and adj_occupied[i][j] == 0:
                new_grid[i][j] = '#'
                changed = True
            elif grid[i][j] == "#" and adj_occupied[i][j] >= 4:
                new_grid[i][j] = "L"
                changed = True
            elif grid[i][j] == "#":
                occupied_count +=1
    return new_grid, changed, occupied_count


def calculate_adjacents2(grid):
    rows = len(grid)
    columns = len(grid[0])
    adj_occupied = numpy.zeros((rows, columns), dtype=int)
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == '.':
                continue
            elif grid[i][j] == "L":
                continue
            elif grid[i][j] == "#":
                a = i-1
                b = i+1
                c = j-1
                d = j+1
                big = max(a,b,c,d)
                found = [False]*8
                ctr = 0

                while ctr<=big and not(found[0] and found[1] and found[2] and found[3] and found[4] and found[5] and found[7]):
                    if ctr<=a and not found[0]:
                        if grid[a-ctr][j] != ".":
                            found[0] = True
                            adj_occupied[a-ctr][j] += 1

                    if ctr+b<rows and not found[1]:
                        if grid[b+ctr][j] != '.':
                            found[1] = True
                            adj_occupied[b+ctr][j] +=1

                    if ctr<=c and not found[2]:
                        if grid[i][c-ctr] != ".":
                            found[2] = True
                            adj_occupied[i][c-ctr] += 1

                    if ctr+d<columns and not found[3]:
                        if grid[i][d+ctr] != '.':
                            found[3] = True
                            adj_occupied[i][d+ctr] += 1

                    if not found[4] and ctr<=a and ctr<=c:
                        if grid[a-ctr][c-ctr] != ".":
                            found[4] = True
                            adj_occupied[a-ctr][c-ctr] +=1

                    if not found[5] and ctr<=a and ctr+d<columns:
                        if grid[a-ctr][d+ctr] != ".":
                            found[5] = True
                            adj_occupied[a-ctr][d+ctr] +=1

                    if not found[6] and ctr+b<rows and ctr<=c:
                        if grid[b+ctr][c-ctr] != ".":
                            found[6] = True
                            adj_occupied[b+ctr][c-ctr] +=1

                    if not found[7] and ctr+b<rows and ctr+d<columns:
                        if grid[b+ctr][d+ctr] != ".":
                            found[7] = True
                            adj_occupied[b+ctr][d+ctr] +=1
                    ctr+=1
    return adj_occupied


def update_grid2(grid, adj_occupied):
    changed = False
    occupied_count = 0
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "L" and adj_occupied[i][j] == 0:
                new_grid[i][j] = '#'
                changed = True
            elif grid[i][j] == "#" and adj_occupied[i][j] >= 5:
                new_grid[i][j] = "L"
                changed = True
            elif grid[i][j] == "#":
                occupied_count +=1
    return new_grid, changed, occupied_count



if __name__ == "__main__":
    seat_grid = []
    with open('day11.txt', 'r') as f:
        contents = f.read().split('\n')
        #seat_grid = [list(x.replace('L', '#')) for x in contents]
        seat_grid = [list(x) for x in contents]

    changed = True
    occupied_count = 0
    while changed:
        adj_occupied = calculate_adjacents2(seat_grid)
        seat_grid, changed, occupied_count = update_grid2(seat_grid, adj_occupied)
    print(occupied_count)

