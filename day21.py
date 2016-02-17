import re
import sys
from itertools import product, combinations

weapons_input = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""

armor_input = """Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""

rings_input = """Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

def parse_input(input_string):
    d = {}
    for line in input_string.splitlines()[1:]:
        name, cost, damage, armor = re.split(r"\s{2,}", line)
        d[name] = {
            "Cost": int(cost),
            "Damage": int(damage),
            "Armor": int(armor)
        }
    return d

weapons = parse_input(weapons_input)
armor = parse_input(armor_input)
armor["None"] = { "Cost": 0, "Damage": 0, "Armor": 0 }
rings = parse_input(rings_input)
rings["None left"] = { "Cost": 0, "Damage": 0, "Armor": 0 }
rings["None right"] = { "Cost": 0, "Damage": 0, "Armor": 0 }


def simulate_battle(player, boss):
    while True:
        boss["Hit Points"] -= max(player["Damage"] - boss["Armor"], 1)
        if boss["Hit Points"] <= 0:
            return True

        player["Hit Points"] -= max(boss["Damage"] - player["Armor"], 1)
        if player["Hit Points"] <= 0:
            return False


equipment_costs = {
    "win": set(),
    "lose": set()
}

for w, a, r in product(weapons, armor, combinations(rings, 2)):
    equipment = [weapons[w], armor[a], rings[r[0]], rings[r[1]]]

    equipment_cost = sum(x["Cost"] for x in equipment)

    player = {
        "Hit Points": 100,
        "Damage": sum(x["Damage"] for x in equipment),
        "Armor": sum(x["Armor"] for x in equipment)
    }

    boss = {
        "Hit Points": 103,
        "Damage": 9,
        "Armor": 2
    }

    if simulate_battle(player, boss):
        equipment_costs["win"].add(equipment_cost)
    else:
        equipment_costs["lose"].add(equipment_cost)

print min(equipment_costs["win"])
print max(equipment_costs["lose"])
