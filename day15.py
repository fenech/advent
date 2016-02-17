import re
from itertools import product

ingredients = {}

for line in open("day15.txt"):
    m = re.match(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", line)
    name, capacity, durability, flavor, texture, calories = m.groups()
    ingredients[name] = {
        "capacity": int(capacity),
        "durability": int(durability),
        "flavor": int(flavor),
        "texture": int(texture),
        "calories": int(calories)
    }

def combos_adding_to_100():
    for combination in product(xrange(101), xrange(101), xrange(101), xrange(101)):
        if sum(combination) == 100:
            yield combination

best_combo = None
highest_score = 0

for combo in combos_adding_to_100():
    capacity = durability = flavor = texture = calories = 0
    for amount, name in zip(combo, ingredients):
        capacity += amount * ingredients[name]["capacity"]
        durability += amount * ingredients[name]["durability"]
        flavor += amount * ingredients[name]["flavor"]
        texture += amount * ingredients[name]["texture"]
        calories += amount * ingredients[name]["calories"]

    if calories != 500:
        continue

    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        continue

    score = capacity * durability * flavor * texture
    if best_combo is None or score > highest_score:
        best_combo = combo
        highest_score = score

print highest_score