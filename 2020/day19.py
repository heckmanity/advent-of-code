import re
from time import time
start = time()

with open("2020/inputs/day_19_input.txt") as f:
    raw_data = f.readlines()

rule_parser = re.compile(r"""(?P<num>\d*): (?P<rule>.*)""")

msg_rules = dict()
messages = []
reading_rules = True
for line in raw_data:
    if line=="\n":
        reading_rules = False
        continue

    if reading_rules:
        parsed = re.match(rule_parser, line[:-1]).groupdict()
        msg_rules[int(parsed['num'])] = parsed['rule']
    
    else:
        messages.append(line[:-1])

#### PART 1 ####

rule_regex = {'|': '|'}
while not(0 in rule_regex.keys()):
    for rule_no, rule in msg_rules.items():
        if "\"" in rule:
            rule_regex[rule_no] = rule[1]
        else:
            references = [int(Q) if not(Q=='|') else '|' for Q in rule.split(' ')]
            ref_test = [(R in rule_regex.keys()) for R in references]
            if all(ref_test):
                this_rule = ''
                for ref in references:
                    this_rule += rule_regex[ref]
                if '|' in this_rule:
                    this_rule = '(?:' + this_rule + ')'
                rule_regex[rule_no] = this_rule

    for finished in rule_regex.keys():
        msg_rules.pop(finished, None)

rule_0 = re.compile('^' + rule_regex[0] + '$')
match_0_ct = 0

for msg in messages:
    if re.match(rule_0, msg):
        match_0_ct += 1

print("\n{} messages completely match rule 0".format(match_0_ct))
print("Runtime: {} seconds".format(time()-start))

#### PART 2 ####

start = time()

rule_0_partial = re.compile('^(' + rule_regex[42] + '+)(' + rule_regex[31] + '+)$')
rule_31 = re.compile(rule_regex[31])
rule_42 = re.compile(rule_regex[42])

match_0_ct = 0

for msg in messages:
    if re.match(rule_0_partial, msg):
        match_42, match_31 = re.match(rule_0_partial, msg).groups()

        match_31, sub_ct_31 = re.subn(rule_31, '', match_31)
        match_42, sub_ct_42 = re.subn(rule_42, '', match_42)

        if sub_ct_42 > sub_ct_31:
            match_0_ct += 1

print("\n{} messages completely match rule 0 after editing rules 8 & 11".format(match_0_ct))
print("Runtime: {} seconds".format(time()-start))