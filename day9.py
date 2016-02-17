import sys
import re
from itertools import combinations, permutations

places = []
distances = {}

with open("day9.txt") as file:
    for line in file:
        m = re.match(r"(\w+) to (\w+) = (\d+)", line)
        places.append(m.group(1))
        places.append(m.group(2))
        distances[(m.group(1), m.group(2))] = int(m.group(3))

places = set(places)
min_distance = None

for route in permutations(places, len(places)):
    total_distance = 0
    for i in xrange(len(places) - 1):
        a, b = route[i:i+2]
        key = (a, b) if (a, b) in distances else (b, a)
        total_distance += distances[key]

    if min_distance is None or total_distance < min_distance:
        best_route = route
        min_distance = total_distance

print best_route, min_distance