import re
from itertools import combinations, permutations

happiness = {}
names = []

for line in open("day13.txt"):
    m = re.match(r"(\w+).*(gain|lose) (\d+).* (\w+)", line)
    if m is None:
        print "couldn't recognise line: " + line
    value = int(m.group(3))
    if m.group(2) == "lose":
        value = -value

    names.append(m.group(1))
    names.append(m.group(4))

    happiness[(m.group(1), m.group(4))] = value

names.append("me")
names = set(names)

for name in names:
    happiness[("me", name)] = 0
    happiness[(name, "me")] = 0

num_guests = len(names)
max_happiness = None

for layout in permutations(names, num_guests):
    total_happiness = 0
    for i in xrange(num_guests):
        total_happiness += happiness[(layout[i], layout[(i+1)%num_guests])]
        total_happiness += happiness[(layout[i], layout[(i-1)%num_guests])]
    if max_happiness is None or total_happiness > max_happiness:
        best_layout = layout
        max_happiness = total_happiness

print best_layout, max_happiness

