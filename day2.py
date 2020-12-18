
def valid_passwords_count(x):
    #[min, max, letter, password]
    count = 0
    for i in x:
        minLet, maxLet, letter, password = i[:]
        dex = password.find(letter)
        occurances = 0
        while dex != -1:
            occurances += 1
            password = password[dex+1:]
            dex = password.find(letter)
        if occurances<=maxLet and occurances>=minLet:
            count +=1
    return count

def valid_passwords_count_two(x):
    count = 0
    for i in x:
        indexOne, indexTwo, letter, password = i[:]
        if bool(password[indexOne-1] == letter) ^ bool(password[indexTwo-1] == letter):
            count +=1

    return count
if __name__ == "__main__":
    x = []
    with open('day2.txt', 'r') as f:
        contents = f.read()
        temp = contents.split('\n')
        for i in temp:
            stop1 = i.find('-')
            stop2 = i.find(' ')
            stop3 = i.find(':')
            x.append([int(i[:stop1]), int(i[stop1+1:stop2]), i[stop2+1:stop3], i[stop3+2:]])
    #res = valid_passwords_count(x)
    res = valid_passwords_count_two(x)
    print(res)
