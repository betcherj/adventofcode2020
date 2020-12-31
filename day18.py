

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def eval_no_paren_addition_first(expression):
    total = 1
    exp = expression.split('*')
    for item in exp:
        total = total * eval(item)
    return total

def eval_no_paren(expression):
    ptr = 0
    while expression[ptr] != '+' and expression[ptr] != '-' and expression[ptr] != '*':
        ptr += 1
    total = expression[:ptr]
    while ptr<len(expression):
        op = expression[ptr]
        ptr+=1
        old_ptr = ptr
        while ptr<len(expression) and expression[ptr] != '+' and expression[ptr] != '-' and expression[ptr] != '*':
            ptr+=1
        val2 = expression[old_ptr:ptr]
        total = eval(str(total) + op + val2)
    return total

def eval_expression(expression):
    expression.replace(' ', '')
    last_paren_location = expression.rfind('(')
    while last_paren_location>-1:
        start = last_paren_location
        end = start + expression[start:].find(')')
        sub_expression = expression[start+1:end]
        total = eval_no_paren_addition_first(sub_expression)
        expression = expression[:start] + str(total) + expression[end+1:]
        last_paren_location = expression.rfind("(")
    total = eval_no_paren_addition_first(expression)

    return total

if __name__ == "__main__":
    import time
    start = time.time_ns()
    with open('day18.txt', 'r') as f:
        contents = f.read().split('\n')
        expressions = [x.replace(' ', '') for x in contents]
    total = 0
    for exp in expressions:
        total += eval_expression(exp)
    end = time.time_ns()
    print((end-start)/1000000)
    print(total)

