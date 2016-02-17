import re

for line in open("day12.txt"):
    print sum(int(d) for d in re.findall(r"-?\d+", line))