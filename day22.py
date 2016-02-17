import copy

spell_costs = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229
}

def spend_mana(spell, player):
    player["Mana"] -= spell_costs[spell]
    return player["Mana"] >= 0

def cast_spell(stats, spell):
    player = stats["Player"]
    boss = stats["Boss"]
    effects = stats["Effects"]

    if not spend_mana(spell, player):
        return False

    # print "Player casts {}.".format(spell)

    if spell == "Magic Missile":
        boss["Hit Points"] -= 4
    elif spell == "Drain":
        boss["Hit Points"] -= 2
        player["Hit Points"] += 2
    elif spell == "Shield":
        if len(effects["Shield"]) > 0:
            return False
        effects["Shield"] = [7 for i in xrange(6)]
    elif spell == "Poison":
        if len(effects["Poison"]) > 0:
            return False
        effects["Poison"] = [3 for i in xrange(6)]
    elif spell == "Recharge":
        if len(effects["Recharge"]) > 0:
            return False
        effects["Recharge"] = [101 for i in xrange(5)]

    return True

def get_armor(stats):
    effects = stats["Effects"]
    try:
        return effects["Shield"].pop()
    except IndexError:
        return 0

def recharge(stats):
    effects = stats["Effects"]
    player = stats["Player"]
    try:
        mana = effects["Recharge"].pop()
        # print "Recharge provides {} mana.".format(mana)
        player["Mana"] += mana
    except IndexError:
        # print "Recharge wears off"
        pass

def poison(stats):
    effects = stats["Effects"]
    boss = stats["Boss"]
    try:
        damage = effects["Poison"].pop()
        boss["Hit Points"] -= damage
        # print "Poison deals {} damage.".format(damage)
    except IndexError:
        # print "Poison wears off"
        pass

def take_turn(stats, player_name, spell = None):
    player = stats["Player"]
    boss = stats["Boss"]

    if player_name == "Player":
        player["Hit Points"] -= 1
        if player["Hit Points"] <= 0:
            return False

    armor = get_armor(stats)

    # print
    # print "-- {} turn --".format(player_name)
    # print "- Player has {} hit points, {} armor, {} mana".format(player["Hit Points"], armor, player["Mana"])
    # print "- Boss has {} hit points".format(boss["Hit Points"])

    recharge(stats)
    poison(stats)

    if boss["Hit Points"] <= 0:
        return True

    if player_name == "Player":
        if not cast_spell(stats, spell):
            return False
    else:
        damage = boss["Damage"] - armor
        # print "Boss attacks for {} damage.".format(damage)
        player["Hit Points"] -= damage

    return player["Hit Points"] > 0

def full_turn(stats, spell, mana_spent):
    if not take_turn(stats, "Player", spell):
        return
    mana_spent += spell_costs[spell]

    if len(mana_costs) > 0 and mana_spent > min(mana_costs):
        return

    if not take_turn(stats, "Boss"):
        return

    if stats["Boss"]["Hit Points"] <= 0:
        # print "Boss died"
        mana_costs.add(mana_spent)
        return

    simulate_battle(stats, mana_spent)

stats = {
    "Player": {
        "Hit Points": 50,
        "Mana": 500
    },
    "Boss": {
        "Hit Points": 71,
        "Damage": 10
    },
    "Effects": {
        "Shield": [],
        "Poison": [],
        "Recharge": []
    }
}

mana_costs = set()

def simulate_battle(stats, mana_spent = 0):
    for spell in spell_costs.iterkeys():
        full_turn(copy.deepcopy(stats), spell, mana_spent)

simulate_battle(stats)

print min(mana_costs)