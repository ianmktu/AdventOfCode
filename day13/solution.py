import numpy as np

from math import gcd
from functools import reduce 

def day13():
    lines = [line.rstrip() for line in open('input.txt')]

    timestamp = int(lines[0])
    bus_ids = [b for b in lines[1].split(",")]

    earliest_time = np.inf
    found_bus_id = -1
    for bus_id in bus_ids:
        if bus_id == "x":
            continue
        bus_id = int(bus_id)
        count = 0
        while True:
            if (timestamp + count) % bus_id == 0:
                if count < earliest_time:
                    earliest_time = count
                    found_bus_id = bus_id
                break
            else:
                count += 1

    bus_ids_only = []
    bus_id_min_offset = []
    bus_id_min_offset_map = {}
    bus_id_and_offset = []
    for minute, bus_id in enumerate(bus_ids):
        if bus_id == "x":
            continue
        else:
            bus_id_min_offset.append((int(bus_id), minute))
            bus_id_min_offset_map[int(bus_id)] = minute
            bus_ids_only.append(int(bus_id))
            bus_id_and_offset.append(int(bus_id) + minute)

    def find_time(input_bus_id_min_offset, start_time=0, increment=None):
        found_time = start_time
        if increment is None:
            increment = min([bus_id for bus_id, _ in input_bus_id_min_offset])
        while True:
            aligns = True
            for bus_id, minute in input_bus_id_min_offset:
                if (found_time + minute) % bus_id != 0:
                    aligns = False
                    break

            if aligns:
                return found_time

            found_time += increment
        return -1
    
    def lcm(denominators):
        return reduce(lambda a,b: a*b // gcd(a,b), denominators)

    found_time = 0
    for i in range(1, len(bus_id_min_offset)):
        current_bus_ids = [bus_id for bus_id, _ in bus_id_min_offset[0:i]]
        if len(current_bus_ids) == 1:
            current_bus_ids *= 2 
        found_time = find_time(input_bus_id_min_offset=bus_id_min_offset[0:i+1],
                               start_time=found_time,
                               increment=lcm(current_bus_ids))

    print("\n****************************************************")
    print("\nDay 13: Part 1")
    print("Answer: {}".format(earliest_time * found_bus_id))

    print("\nDay 13: Part 2")
    print("Answer: {}".format(found_time))
    print("\n****************************************************")


if __name__ == '__main__':
    day13()
