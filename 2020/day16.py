import re
from time import time
start = time()

with open("2020/inputs/day_16_input.txt") as f:
    raw_data = f.readlines()

parser = re.compile(r"""(?P<field_name>[\w\s]*): (?P<r1>\d*)-(?P<r2>\d*) or (?P<r3>\d*)-(?P<r4>\d*)""")

valid_ranges = dict()
tickets = []

reading_ranges = True
reading_tickets = False
for dataline in raw_data:
    if reading_ranges:
        parsed = re.match(parser, dataline)
        if parsed:
            parsed = parsed.groupdict()
            field = parsed['field_name']
            ranges = [int(v) for k,v in parsed.items() if not(k=='field_name')]
            valid_ranges[field] = ranges
        else:
            reading_ranges = False
    
    elif reading_tickets:
        if not(dataline=="nearby tickets:\n" or dataline=="\n"):
            tickets.append([int(v) for v in dataline[:-1].split(',')])
    
    else:
        if dataline=="your ticket:\n":
            continue
        else:
            my_ticket = [int(v) for v in dataline[:-1].split(',')]
            reading_tickets = True

#### PART 1 ####

valid_numbers_per_field = dict()
for fld, rng in valid_ranges.items():
    valid_numbers_per_field[fld] = set()
    for index_in in [0, 2]:
        for val in range(rng[index_in], rng[index_in+1] + 1):
            valid_numbers_per_field[fld].add(val)

valid_numbers = set()
for rng in valid_numbers_per_field.values():
    for val in rng:
        valid_numbers.add(val)

error_rate = 0

for tkt in tickets[::-1]:
    for val in tkt:
        if not(val in valid_numbers):
            error_rate += val
            tickets.pop(tickets.index(tkt))
            break

print("\nThe ticket scanning error rate is {}".format(error_rate))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

field_names = list(valid_ranges.keys())
tickets = [my_ticket] + tickets
field_positions = dict()

for fld_ind in range(len(my_ticket)):
    printed_values = set()
    for tkt in tickets:
        printed_values.add(tkt[fld_ind])
    
    poss_fields = []
    for fld in field_names:
        if len(printed_values.difference(valid_numbers_per_field[fld]))==0:
            poss_fields.append(fld)
    field_positions[fld_ind] = poss_fields

solved_fields = []
while not all([len(v)==1 for v in field_positions.values()]):
    for fld_ind in range(len(my_ticket)):
        details = [field_positions[fld_ind][0], fld_ind]
        if len(field_positions[fld_ind])==1 and not(details in solved_fields):
            solved_fields.append(details)
    
    for fld in solved_fields:
        for fld_ind in range(len(my_ticket)):
            if fld[0] in field_positions[fld_ind] and not(fld[1]==fld_ind):
                field_positions[fld_ind].pop(field_positions[fld_ind].index(fld[0]))

dest_product = 1

for fld in solved_fields:
    if fld[0][:9]=="departure":
        fld_ind = fld[1]
        dest_product *= my_ticket[fld_ind]

print("\nThe 'departure' field product is {}".format(dest_product))
print("Runtime: {} seconds".format(time()-start))