import re

speeds = {}

def get_speed(speed, duration, rest):
    return lambda t: speed if t % (duration + rest) < duration else 0

for line in open("day14.txt"):
    m = re.match(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
    name, speed, duration, rest = m.groups()
    speeds[name] = get_speed(int(speed), int(duration), int(rest))

distances = {}
max_distance = None

for name in speeds.iterkeys():
    distance = sum(speeds[name](t) for t in xrange(2503))
    distances[name] = distance
    if max_distance is None or distance > max_distance:
        max_distance = distance

print distances
print max_distance

points = {}
for name in speeds.iterkeys():
    distances[name] = 0
    points[name] = 0

for t in xrange(2503):
    winners = []
    for name in speeds.iterkeys():
        distances[name] += speeds[name](t)
        if len(winners) == 0 or distances[name] > max_distance:
            max_distance = distances[name]
            winners = [name]
        elif distances[name] == max_distance:
            winners.append(name)
    for winner in winners:
        points[winner] += 1

print points


