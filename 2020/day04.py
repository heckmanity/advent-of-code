import re
from time import time
start = time()

all_eight_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])

code = re.compile(r"""[a-z]{3}[:]{1}""", re.VERBOSE)

with open("2020/inputs/day_4_input.txt") as f:
    passport_list = f.readlines()

#### PART 1

valid_ct = 0
current_passport = []
current_passport_fields = []
valid_passports = []
for line in passport_list:
    if line=="\n":
        missing_fields = all_eight_fields.difference(set(current_passport_fields))
        if not(missing_fields) or missing_fields=={'cid'}:
            valid_ct += 1
            valid_passports.append(current_passport)
        current_passport = []
        current_passport_fields = []
        continue
    fields = re.findall(code, line)
    for fld in fields:
        current_passport_fields.append(fld[:-1])
    current_passport.append(line[:-1])

print("\nThere are {} 'valid' passports".format(valid_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

valid_data = re.compile(r"""(byr:(19[2-9][0-9] | 200[0-2])$) |
                            (iyr:(201[0-9] | 2020)$) |
                            (eyr:(202[0-9] | 2030)$) |
                            (hgt:((1[5-8][0-9]cm | 19[0-3]cm) | (59in | 6[0-9]in | 7[0-6]in))$ ) |
                            (hcl:(\#[0-9a-f]{6})$) |
                            (ecl:(amb|blu|brn|gry|grn|hzl|oth)$) |
                            (pid:[0-9]{9}$)""", re.VERBOSE)

valid_ct = 0

for PP in valid_passports:
    legit = True
    for line in PP:
        fields = line.split(" ")
        for fld in fields:
            if fld[:3]=='cid':
                continue
            if not(re.match(valid_data, fld)):
                legit = False
    if legit:
        valid_ct += 1

print("\nThere are {} 'valid' passports".format(valid_ct))
print("Runtime: {} seconds".format(time()-start))