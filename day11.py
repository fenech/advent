import re

password = "vzbxkghb"
password = "vzbxxyzz"
ready = False

chars = list(password)

alphabet = [chr(x) for x in xrange(ord("a"), ord("z") + 1)]
straights = ["".join(x) for i in xrange(len(alphabet) - 2) for x in [alphabet[i:i+3]]]

def validate(password):
    if not any(re.search(s, password) for s in straights):
        return False
    if re.search(r"[iol]", password) is not None:
        return False
    if re.search(r"(.)\1.*(.)\2.*", password) is None:
        return False
    return True

def increment(chars, index):
    char = chars[index]
    if char == "z":
        chars[index] = "a"
        return increment(chars, index - 1)
    chars[index] = chr(ord(char) + 1)
    return chars


while not (ready and validate(password)):
    ready = True
    chars = increment(chars, len(password) - 1)
    password = "".join(chars)

print password
