import math
def tree_encounters(treeMap, right, down):
    count = 0
    pos = [0,0]
    while pos[1]<len(treeMap):
        if treeMap[pos[1]][pos[0]] == '#':
            count += 1
        pos[0] = pos[0] + right
        if pos[0] >= len(treeMap[0]):
            pos[0] = pos[0]-len(treeMap[0])
        pos[1] = pos[1] + down
    return count

if __name__ == "__main__":
    treeMap = []
    with open('day3.txt', 'r') as f:
        contents = f.read()
        treeMap = contents.split('\n')
    to_check = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    temp = []
    for j in to_check:
        temp.append(tree_encounters(treeMap, j[0], j[1]))
    res = 1
    for i in temp:
        res = i * res
    print(res)