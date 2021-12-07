import re
from time import time
start = time()

with open("2015/inputs/day_12_input.txt") as f:
    data = f.readline()[:-1]

num_test = re.compile(r"""(\-*\d+)""")

#### PART 1 ####

numbers_found = re.findall(num_test, data)
numbers_found = [int(N) for N in numbers_found]

print("\nThe sum of all numbers in the file is {}".format(sum(numbers_found)))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

exec("data_list = " + data)

def get_sum(obj):
    if isinstance(obj, int):
        return obj
    if isinstance(obj, str):
        return 0
    if isinstance(obj, list):
        return sum([get_sum(i) for i in obj])
    if isinstance(obj, dict):
        if not("red" in obj.values()):
            return sum([get_sum(i) for i in obj.values()])
        else:
            return 0

working_sum = get_sum(data_list)

print("\nThe sum of all numbers ignoring red is {}".format(working_sum))
print("Runtime: {} seconds".format(time()-start))

# red_test = re.compile(r"""\"red\"""")

# sum_stack = []
# red_stack = []
# working_sum = 0
# red_found = False
# just_matched = False
# for char_ind in range(len(data)):
#     char = data[char_ind]
#     if char=='{':
#         sum_stack.append(working_sum)
#         red_stack.append(red_found)
#         working_sum = 0
#         red_found = False
#     if char=='}':
#         if red_found:
#             working_sum = sum_stack.pop()
#         else:
#             working_sum += sum_stack.pop()
#         red_found = red_stack.pop()
    
#     if re.match(num_test, data[char_ind:]):
#         if not(just_matched):
#             val_str = re.match(num_test, data[char_ind:]).group(1)
#             working_sum += int(val_str)
#             just_matched = True
#     else:
#         just_matched = False

#     if data[char_ind:char_ind+5]=="\"red\"":
#         red_found = True 