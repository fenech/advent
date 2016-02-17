import re

sequence = "1113122113"

for i in xrange(50):
    output = ""
    for repetitions, number in re.findall(r"((\d)\2*)", sequence):
        output += str(len(repetitions)) + number

    sequence = output

print len(sequence)