import re

wires = {"b": 3176}

def normalise(val):
    return val % 65536

def my_not(x):
    result = int(x)
    return normalise(~result)

def my_and(x, y):
    my_x = int(x)
    my_y = int(y)
    return normalise(my_x & my_y)

def my_or(x, y):
    my_x = int(x)
    my_y = int(y)
    return normalise(my_x | my_y)

def my_lshift(x, y):
    my_x = int(x)
    my_y = int(y)
    return normalise(my_x << my_y)


def my_rshift(x, y):
    my_x = int(x)
    my_y = int(y)
    return normalise(my_x >> my_y)

operators = {
    'NOT': my_not,
    'AND': my_and,
    'OR': my_or,
    'LSHIFT': my_lshift,
    'RSHIFT': my_rshift
}

recipes = {}
with open("file") as file:
    for line in file:
        recipe, output = line.rstrip().split(" -> ")
        recipes[output] = recipe

def get_value(wire):
    if wire not in recipes:
        return wire

    if wire in wires:
        return wires[wire]

    print
    print "recipe for " + wire + ": ", recipes[wire]
    if re.match(r"\d+$", recipes[wire]) is not None:
        wires[wire] = recipes[wire]
        return wires[wire]

    m = re.match(r"(\w+)$", recipes[wire])
    if m is not None:
        wires[wire] = get_value(m.group(1))
        return wires[wire]

    m = re.match(r"NOT (\w+)$", recipes[wire])
    if m is not None:
        wires[wire] = operators['NOT'](get_value(m.group(1)))
        return wires[wire]

    m = re.match(r"(\w+) (AND|OR|LSHIFT|RSHIFT) (\w+)$", recipes[wire])
    if m is not None:
        wires[wire] = operators[m.group(2)](get_value(m.group(1)), get_value(m.group(3)))
        print recipes[wire] + "=" + str(wires[wire])
        return wires[wire]

print get_value("a")