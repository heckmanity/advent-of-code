from time import time
from functools import reduce
start = time()

with open("2021/inputs/day_16_input.txt") as f:
    transmission = f.readline().strip()

def extract(stream, size):
    return stream[:size], stream[size:]

def parse_packet(data):
    version, data = extract(data, 3)
    type_ID, data = extract(data, 3)

    if int(type_ID, 2) == 4:
        finished = False
        bin_val = ''
        while not finished:
            big_byte, data = extract(data, 5)
            if big_byte[0] == '0':
                finished = True
            bin_val += big_byte[1:]
        value = int(bin_val, 2)

    else:
        len_type_ID, data = extract(data, 1)
        if len_type_ID == '0':
            length, data = extract(data, 15)
            length = int(length, 2)

            start_len = len(data)
            subpackets = []
            while start_len - len(data) < length:
                sub, data = parse_packet(data)
                subpackets.append(sub)
        else:
            length, data = extract(data, 11)
            length = int(length, 2)

            subpackets = []
            for sp in range(length):
                sub, data = parse_packet(data)
                subpackets.append(sub)

    return {
            'version': version, 
            'type_ID': type_ID,
            'data': value if int(type_ID, 2)==4 else subpackets 
           }, data

def get_version_sum(pkt):
    if type(pkt['data']) is list:
        return int(pkt['version'], 2) + sum( [get_version_sum(p) for p in pkt['data']] )
    else:
        return int(pkt['version'], 2)

#### PART 1

datastream = f"{int(transmission, 16):0{len(transmission)*4}b}"

packet_structure, _ = parse_packet(datastream)
vers_sum = get_version_sum(packet_structure)

print(f"\nThe sum of all version numbers is {vers_sum}")
print(f"Runtime: {time()-start} seconds")

#### PART 2

start = time()

many_ops = [ lambda l: reduce(lambda x, y: x+y, l),
             lambda l: reduce(lambda x, y: x*y, l),
             lambda l: reduce(lambda x, y: min(x,y), l),
             lambda l: reduce(lambda x, y: max(x,y), l),
             None,
             lambda l: reduce(lambda x, y: 1 if x > y else 0, l),
             lambda l: reduce(lambda x, y: 1 if x < y else 0, l),
             lambda l: reduce(lambda x, y: 1 if  x==y else 0, l) ]

def compute(pkt):
    op_code = int(pkt['type_ID'], 2)
    if op_code == 4:
        return pkt['data']

    inputs = [compute(p) for p in pkt['data']]    
    return many_ops[op_code](inputs)        
    
solution = compute(packet_structure)

print(f"\nThe value represented by the BITS transmission is {solution}")
print(f"Runtime: {time()-start} seconds")