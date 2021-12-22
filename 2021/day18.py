from time import time
from string import digits
import re
from itertools import product
start = time()

with open("2021/inputs/day_18_input.txt") as f:
    assignment = [ln.strip() for ln in f.readlines()]

class SnailNum:
    def __init__(self, val):
        self.rep_str = val
        self.reduced = False

        while not self.reduced:
            self.reduced = self.reduce()

        depth = 0
        reg_num_at_start = re.match(re.compile(r"""\[\d+,"""), self.rep_str)
        if reg_num_at_start:
            breakpoint = reg_num_at_start.span()[1] - 1
        else:
            for i, ch in enumerate(self.rep_str[1:-1]):
                if ch == '[':
                    depth += 1
                if ch == ']':
                    depth -= 1
                    if depth==0 and i>0:
                        breakpoint = i+2
                        break
        
        self.left = self.rep_str[1:breakpoint]
        if not self.left.count('['):
            self.left = int(self.left)
        else:
            self.left = SnailNum(self.left)

        self.right = self.rep_str[breakpoint+1:-1]
        if not self.right.count('['):
            self.right = int(self.right)
        else:
            self.right = SnailNum(self.right)
        
    def reduce(self):
        depth = 0
        reg_nums = []
        split_index = -1
        for i, ch in enumerate(self.rep_str):
            if ch == '[':
                depth += 1
            elif ch == ']':
                depth -= 1
            elif ch in digits:
                if self.rep_str[i-1] in digits:
                    reg_nums[-1] += ch
                    if split_index < 0:
                        split_index = len(reg_nums) - 1
                else:
                    reg_nums.append(ch)
            else:
                continue

            if depth > 4:
                self.explode(len(reg_nums))
                return False
            
        if split_index >= 0:
            self.split(split_index)
            return False
        
        return True

    def explode(self, val_index):
        vals = re.split("[\[\],]+", self.rep_str)[1:-1]
        delims = re.split("[0-9]+", self.rep_str)

        if val_index > 0:
            vals[val_index - 1] = str(int(vals[val_index-1]) + int(vals[val_index]))
        if val_index < len(vals) - 2:
            vals[val_index + 2] = str(int(vals[val_index+2]) + int(vals[val_index+1]))
        vals.pop(val_index)
        vals[val_index] = '0'

        delims[val_index] = delims[val_index][:-1]
        delims.pop(val_index+1)
        delims[val_index + 1] = delims[val_index + 1][1:]

        new_str = ''
        for s in range(len(vals)):
            new_str += delims[s] + vals[s]
        new_str += delims[-1]
        self.rep_str = new_str
    
    def split(self, val_index):
        vals = re.split("[\[\],]+", self.rep_str)[1:-1]
        delims = re.split("[0-9]+", self.rep_str)

        val_to_split = int(vals[val_index])
        repl_val = f"[{val_to_split // 2},{(val_to_split // 2) + (val_to_split % 2)}]"

        new_str = ''
        for s in range(len(vals)):
            if s == val_index:
                new_str += delims[s] + repl_val
            else:
                new_str += delims[s] + vals[s]
        new_str += delims[-1]
        self.rep_str = new_str
    
    def __add__(self, other):
        return SnailNum('[' + str(self) + ',' + str(other) + ']')
    
    def __abs__(self):
        return 3 * abs(self.left) + 2 * abs(self.right)

    def __str__(self):
        return self.rep_str

#### PART 1

total = SnailNum(assignment[0])

for ln in assignment[1:]:
    total = total + SnailNum(ln)

print(f"\nThe magnitude of the final sum is {abs(total)}")
print(f"Runtime: {time()-start} seconds")

#### PART 2

start = time()

best_mag = 0
for i, j in product(range(len(assignment)), repeat=2):
    if not i==j:
        pair_sum = SnailNum(assignment[i]) + SnailNum(assignment[j])
        if abs(pair_sum) > best_mag:
            best_mag = abs(pair_sum)

print(f"\nThe largest magnitude of any sum from the assignment is {best_mag}")
print(f"Runtime: {time()-start} seconds")