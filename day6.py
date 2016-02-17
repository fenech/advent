import re

ranges = re.compile(r"(\d+),(\d+) through (\d+),(\d+)")
turn_on = re.compile(r"^turn on")
turn_off = re.compile(r"^turn off")
toggle = re.compile(r"^toggle")

lights = [[0 for i in xrange(1000)] for j in xrange(1000)]
    
with open("file") as file:
    for line in file:
        r = ranges.search(line)
        if r is None:
            print line
            continue
        if turn_on.search(line) is not None:
            for i in xrange(int(r.group(1)), int(r.group(3)) + 1):
                for j in xrange(int(r.group(2)), int(r.group(4)) + 1):
                    lights[i][j] += 1
        elif turn_off.search(line) is not None:
            for i in xrange(int(r.group(1)), int(r.group(3)) + 1):
                for j in xrange(int(r.group(2)), int(r.group(4)) + 1):
                    lights[i][j] = max(lights[i][j] - 1, 0)
        elif toggle.search(line) is not None:
            for i in xrange(int(r.group(1)), int(r.group(3)) + 1):
                for j in xrange(int(r.group(2)), int(r.group(4)) + 1):
                    lights[i][j] += 2

count = 0                    
for i in xrange(1000):
    for j in xrange(1000):
        count += lights[i][j]

print count
