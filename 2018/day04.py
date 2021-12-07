import re
from copy import deepcopy
from datetime import datetime
from time import time
start = time()

with open("2018/inputs/day_4_input.txt") as f:
    timestamps = f.readlines()
timestamps = sorted(timestamps)

#### PART 1

minute_counts = dict()
guard_template = [0] * 60

time_parser = re.compile(r"""\[(\d*)-(\d*)-(\d*) (\d*):(\d*)\]""")
event_parser = re.compile(r"""\[.*\] (.*)""")
guard_num_parser = re.compile(r"""Guard \#(\d*) begins shift""")

current_guard = None
sleepy_time = None

for ts in timestamps:
    timecode = [int(q) for q in re.match(time_parser, ts).groups()]
    timecode = datetime(*timecode)

    action = re.match(event_parser, ts[:-1]).group(1)
    if action[0]=='G':
        current_guard = int(re.match(guard_num_parser, action).group(1))
        if not(current_guard in minute_counts.keys()):
            minute_counts[current_guard] = deepcopy(guard_template)
    
    if action[0]=='f':
        sleepy_time = timecode
    
    if action[0]=='w':
        delta_t = timecode - sleepy_time
        minutes_out = delta_t.seconds // 60
        start_min = sleepy_time.minute
        for minute in range(start_min, start_min + minutes_out):
            minute_counts[current_guard][minute%60] += 1

sleep_totals = sorted(minute_counts.items(), key=lambda q: sum(q[1]), reverse=True)
guard_choice = max(minute_counts.items(), key=lambda q: sum(q[1]))[0]
sleepy_min = max([x for x in range(60)], key=lambda q: minute_counts[guard_choice][q])

print("\nGuard #{} was asleep most during minute {}".format(guard_choice, sleepy_min))
print("Product = {}".format(guard_choice * sleepy_min))
print("Runtime: {} seconds".format(time()-start))

#### PART 2

start = time()

guard_choice = None
sleepy_min = None
sleepy_ct = 0

for k,v in minute_counts.items():
    if max(v) > sleepy_ct:
        guard_choice = k
        sleepy_min = max([x for x in range(60)], key=lambda q: minute_counts[k][q])
        sleepy_ct = max(v)

print("\nGuard #{} spent minute {} asleep more than any other".format(guard_choice, sleepy_min))
print("Product = {}".format(guard_choice * sleepy_min))
print("Runtime: {} seconds".format(time()-start))