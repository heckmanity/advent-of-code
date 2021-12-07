from alive_progress import alive_bar
from copy import deepcopy
from time import time
start = time()

with open("2020/inputs/day_18_input.txt") as f:
    p_set = [line[:-1] for line in f.readlines()]

def add_spaces(expression):
    new_expression = ''
    for i in range(len(expression)):
        if expression[i]=='(':
            new_expression += '( '
        elif expression[i]==')':
            new_expression += ' )'
        else:
            new_expression += expression[i]
    return new_expression

#### PART 1 ####

def new_math(expression, lvl=0):
    if type(expression)==str:
        terms = expression.split(' ')
    else:
        terms = expression
        
    first = terms.pop(0)
    if first=='(':
        value, terms = new_math(terms, lvl=lvl+1)
    else:
        value = int(first)
    
    while len(terms) > 0:
        operation = terms.pop(0)
        if operation==')':
            return value, terms
        
        arg = terms.pop(0)
        if arg=='(':
            arg, terms = new_math(terms, lvl=lvl+1)
        else:
            arg = int(arg)
        
        if operation=='*':
            value *= arg
        if operation=='+':
            value += arg
    
    if lvl==0:
        return value
    else:
        return value, terms

hw_sum = 0

for problem in p_set:
    parsed = add_spaces(problem)
    hw_sum += new_math(parsed)

print("\nThe sum of all answers to the problem set is {}".format(hw_sum))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

sign = lambda x: -1 if x<0 else (0 if x==0 else 1)

def add_parens(expression):
    expression = expression.replace(' ', '')

    i = 0
    while i < len(expression):
        if not(expression[i]=='+'):
            i += 1
            continue
        
        offsets = [-1, 1]
        parens = '()'

        for off in offsets:
            parity = sign(off)
            which = parens[0 if parity==1 else 1]
            if expression[i+off]==which:
                paren_ct = 1
                while not(paren_ct==0):
                    off += parity
                    offsets[1 if parity==1 else 0] += parity
                    if expression[i+off]=='(':
                        paren_ct += parity
                    if expression[i+off]==')':
                        paren_ct -= parity
        
        left_offset, right_offset = offsets
        expression = expression[:i+left_offset] + '('         \
                        + expression[i+left_offset:i+right_offset+1] + ')' \
                        + expression[i+right_offset+1:]
        i += 2

    return expression

hw_sum = 0

for problem in p_set:
    hw_sum += eval(add_parens(problem))

print("\nThe sum of all answers to the advanced problem set is {}".format(hw_sum))
print("Runtime: {} seconds".format(time()-start))