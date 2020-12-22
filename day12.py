import time

def rotate_ship(cur_dir, cmd, val ):
    dirs = ["W", "N", "E", "S"]
    dex = dirs.index(cur_dir)
    increment = int(val/90)

    if cmd == "R":
        new_dex = (increment+dex)%4
    elif cmd == "L":
        new_dex = (dex-increment)%4
    return dirs[new_dex]

def naivgate_ship(directions):
    coords = [0,0]
    cur_dir = 'E'
    for i in directions:
        cmd =  i[0]
        val = int(i[1:])
        if cmd == "L" or cmd == "R":
            cur_dir = rotate_ship(cur_dir, cmd, val)
            continue

        if cmd == 'F':
            cmd = cur_dir

        if cmd == "N":
            coords[1] += val
        elif cmd == "S":
            coords[1] -= val
        elif cmd == "W":
            coords[0] -= val
        elif cmd == "E":
            coords[0] += val
    return coords

def rotate_waypoint(cmd, val, waypoint_offset):
    increment = int(val/90)%4
    new_offset = [waypoint_offset[0], waypoint_offset[1]]
    if cmd == "L" and increment == 3:
        #270 L == 90 R
        increment = 1
    elif cmd == "L" and increment == 1:
        #90 R == 270L
        increment = 3

    if increment == 1:
        new_offset = [waypoint_offset[1], -waypoint_offset[0]]
    elif increment == 2:
        new_offset = [-waypoint_offset[0], -waypoint_offset[1]]
    elif increment == 3:
        new_offset = [-waypoint_offset[1], waypoint_offset[0]]

    return new_offset


def naivgate_waypoint(directions):
    waypoint_offset= [10,1]
    coords = [0,0]
    for i in directions:
        cmd =  i[0]
        val = int(i[1:])
        if cmd == "L" or cmd == "R":
            waypoint_offset = rotate_waypoint(cmd, val, waypoint_offset)
            continue

        if cmd == 'F':
            coords[0] += val*waypoint_offset[0]
            coords[1] += val*waypoint_offset[1]
            continue

        if cmd == "N":
            waypoint_offset[1] += val
        elif cmd == "S":
            waypoint_offset[1] -= val
        elif cmd == "W":
            waypoint_offset[0] -= val
        elif cmd == "E":
            waypoint_offset[0] += val
    return coords

def manhattan_distance(coords):
    return abs(coords[0])+abs(coords[1])


if __name__ == "__main__":
    directions = []
    with open('day12.txt', 'r') as f:
        directions = f.read().split('\n')
    start = time.time_ns()
    coords = naivgate_waypoint(directions)
    print(manhattan_distance(coords))
    end = time.time_ns()
    print(float(end-start)/1000000)