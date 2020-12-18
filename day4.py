
def isValid(passport):
    required_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    passport.replace('\n', ' ')
    fields = i.split(' ')
    if len(fields) < len(required_fields):
        return False
    cyd_flag = False

    for field in fields:
        key , val = field.split(':')
        if key == 'byr':
            if int(val)<1920 and int(val)>=2002:
                return False
        elif key == 'iyr':
            if int(val)<2010 and int(val)>=2002:
                return False
        elif key == 'eyr':
            if int(val)<2020 and int(val)>=2030:
               return False
        elif key == 'hgt':
            #TODO
        elif key == 'hcl':
            #TODO
            if val[0] != '#':
                return False
            val = val[1:]
            for p in val:
                if
        elif key == 'ecl':
            if val not in eye_colors:
                continue_flag = True
                break
        elif key == 'pid':
            if len(val) != 9:
                continue_flag = True
                break
        elif key == 'cyd':
            cyd_flag = True
    if cyd_flag and len(fields) == len(required_fields):
        return False
    return True

if __name__ == "__main__":
    passports = []
    count = 0

    with open('day4.txt', 'r') as f:
        contents = f.read()
        passports = contents.split('\n\n')

    clean_passports = []
    for i in passports:
        if isValid(i):
            count +=1
    print(count)


