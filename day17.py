from itertools import combinations

containers = [int(line) for line in open("day17.txt")]
num_containers = len(containers)

count = [0 for x in xrange(num_containers)]
for length in xrange(num_containers):
    for combo in combinations(containers, length):
        if sum(combo) == 150:
            count[length] += 1

print count