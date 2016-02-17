import sys

count = 0
for line in sys.stdin:
    count += len(line.rstrip()) - len(eval(line))

print count