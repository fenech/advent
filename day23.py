import re

def init_register(registers, r):
    if r not in registers:
        registers[r] = 0

def hlf(registers, r, line):
    init_register(registers, r)
    registers[r] //= 2
    return line + 1

def tpl(registers, r, line):
    init_register(registers, r)
    registers[r] *= 3
    return line + 1

def inc(registers, r, line):
    init_register(registers, r)
    registers[r] += 1
    return line + 1

def jmp(line, offset):
    return line + offset

def jie(registers, r, line, offset):
    init_register(registers, r)
    if registers[r] % 2 == 0:
        return line + offset
    return line + 1

def jio(registers, r, line, offset):
    init_register(registers, r)
    if registers[r] == 1:
        return line + offset
    return line + 1

instructions = open("day23.txt").readlines()
length = len(instructions)
registers = { "a": 1 }
line = 0
while line < length:
    instruction = instructions[line]

    m = re.match(r"hlf (\w+)", instruction)
    if m is not None:
        line = hlf(registers, m.group(1) , line)
        continue

    m = re.match(r"tpl (\w+)", instruction)
    if m is not None:
        line = tpl(registers, m.group(1), line)
        continue

    m = re.match(r"inc (\w+)", instruction)
    if m is not None:
        line = inc(registers, m.group(1), line)
        continue

    m = re.match(r"jmp ([+-]\d+)", instruction)
    if m is not None:
        line = jmp(line, int(m.group(1)))
        continue

    m = re.match(r"jie (\w+), ([+-]\d+)", instruction)
    if m is not None:
        line = jie(registers, m.group(1), line, int(m.group(2)))
        continue

    m = re.match(r"jio (\w+), ([+-]\d+)", instruction)
    if m is not None:
        line = jio(registers, m.group(1), line, int(m.group(2)))
        continue

    print "couldn't parse instruction: " + instruction

print registers["b"]