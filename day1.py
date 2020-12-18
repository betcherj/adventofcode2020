
def sum_to_2020(x):
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i] + x[j] == 2020:
                return (i, j)
    print("No entries found")
    return None

def three_sum_2020(x):
    for i in range(len(x)):
        if x[i] > 2020:
            continue
        for j in range(i, len(x)):
            if x[j] + x[i] >2020:
                continue
            for p in range(j, len(x)):
                if x[i] + x[j] + x[p] == 2020:
                    return (i, j, p)
    print("No entries found")
    return None

if __name__ == "__main__":
    with open('day1.txt', 'r') as f:
        contents = f.read()
        temp = contents.split('\n')
    x = [int(a) for a in temp]
    # print(x)
    # res = sum_to_2020(x)
    # print(res)
    # print(x[res[0]]* x[res[1]])
    res = three_sum_2020(x)
    print(res)
    print(x[res[0]]* x[res[1]] * x[res[2]])
