
def isValid(passport):
    required_fields = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    actual_fields = []
    fields = passport.replace('\n', ' ').split(' ')
    if len(fields) < len(required_fields):
        return False
    for field in fields:
        key , val = field.split(':')
        if key != 'cid':
            actual_fields.append(key)
        if key == 'byr':
            if int(val)<1920 or int(val)>2002:
                return False
        elif key == 'iyr':
            if int(val)<2010 or int(val)>2020:
                return False
        elif key == 'eyr':
            if int(val)<2020 or int(val)>2030:
               return False
        elif key == 'hgt':
            units = val[-2:]
            if units != 'in' and units !='cm':
                return False
            measure = int(val[:-2])
            if units == "cm" and (measure<150 or measure>193):
                return False
            elif units == "in" and (measure<59 or measure>76):
                return False
        elif key == 'hcl':
            if val[0] != '#' or len(val) != 7:
                return False
            val = val[1:]
            for p in val:
                ascii_val = ord(p.lower())
                if not ((ascii_val>=97 and ascii_val<=122) or (ascii_val>=48 and ascii_val<=57)):
                    return False
        elif key == 'ecl':
            if val not in eye_colors:
                return False
        elif key == 'pid':
            if len(val) != 9:
                return False
    actual_fields.sort()
    if required_fields != actual_fields:
        return False
    return True

if __name__ == "__main__":
    passports = []
    count = 0

    with open('day4.txt', 'r') as f:
        contents = f.read()
        passports = contents.split('\n\n')
    ctr = 0
    for i in passports:
        ctr+=1
        if isValid(i):
            count +=1
    print(count)


