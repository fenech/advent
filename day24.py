from itertools import combinations
from operator import mul

with open("day24.txt") as file:
    packages = map(int, map(str.rstrip, list(file)))

total_weight = sum(packages)
parts = 4
weight_each = total_weight / parts

def has_sum(packages, groups):
    for count in xrange(1, len(packages)):
        for combination in (c for c in combinations(packages, count) if sum(c) == weight_each):
            if groups == 2:
                return True
            elif groups < parts:
                return has_sum(list(set(packages) - set(combination)), groups - 1)
            elif has_sum(list(set(packages) - set(combination)), groups - 1):
                return reduce(mul, combination, 1)

print has_sum(packages, parts)

