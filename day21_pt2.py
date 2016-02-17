def cast_shield():
    for i in xrange(6):
        yield 7

def cast_poison():
    for i in xrange(6):
        yield 3

def cast_recharge():
    for i in xrange(5):
        yield 101

spell_costs = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229
}

effects = {
    "Shield": None,
    "Poison": None,
    "Recharge": None
}

def spend_mana(spell, player):
    player["Mana"] -= spell_costs[spell]
    return player["Mana"] >= 0

def cast_spell(spell, player, boss):
    if not spend_mana(spell, player):
        return False

    print "Player casts {}.".format(spell)

    if spell == "Magic Missile":
        boss["Hit Points"] -= 4
    elif spell == "Drain":
        boss["Hit Points"] -= 2
        player["Hit Points"] += 2
    elif spell == "Shield":
        if effects["Shield"] is not None:
            return False
        effects["Shield"] = cast_shield()
    elif spell == "Poison":
        if effects["Poison"] is not None:
            return False
        effects["Poison"] = cast_poison()
    elif spell == "Recharge":
        if effects["Recharge"] is not None:
            return False
        effects["Poison"] = cast_recharge()

    return True

players = {
    "Player": {
        "Hit Points": 50,
        "Mana": 500
    },
    "Boss": {
        "Hit Points": 71,
        "Damage": 10
    }
}

def get_armor():
    if effects["Shield"] is not None:
        try:
            return effects["Shield"].next()
        except StopIteration:
            effects["Shield"] = None
    return 0

def recharge(player):
    if effects["Recharge"] is not None:
        try:
            player["Mana"] += effects["Recharge"].next()
        except StopIteration:
            effects["Recharge"] = None

def poison(boss):
    if effects["Poison"] is not None:
        try:
            boss["Hit Points"] -= effects["Poison"].next()
        except StopIteration:
            effects["Poison"] = None

def take_turn(player_name, spell = None):
    player = players["Player"]
    boss = players["Boss"]

    armor = get_armor()
    recharge(player)
    poison(boss)

    print "-- {} turn --".format(player_name)
    print "- Player has {} hit points, {} armor, {} mana".format(player["Hit Points"], player["Armor"], player["Mana"])
    print "- Boss has {} hit points".format(boss["Hit Points"])
    if player_name == "Player" and not cast_spell(spell, player, boss):
        return False
    else:
        damage = boss["Damage"] - armor
        print "Boss attacks for {} damage.".format(damage)
        player["Hit Points"] -= damage

    return player["Hit Points"] > 0

mana_costs = set()
def simulate_battle(spell_sequence):
    mana_spent = 0
    for spell in spell_sequence:
        if not take_turn("Player", spell):
            return
        mana_spent += spell_costs[spell]
        if len(mana_costs) > 0 and mana_spent > min(mana_costs):
            return
        if not take_turn("Boss"):
            return

        if players["Boss"]["Hit Points"] <= 0:
            mana_costs.add(mana_spent)
            return

simulate_battle(["Poison", "Magic Missile"])
raise

from itertools import product

for spell_sequence in product(spell_costs.iterkeys(), repeat=len(10)):
    simulate_battle(spell_sequence)

print min(mana_costs)