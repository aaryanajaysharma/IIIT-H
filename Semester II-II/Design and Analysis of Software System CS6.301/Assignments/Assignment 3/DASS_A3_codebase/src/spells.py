from characters import barbarians, dragons, balloons, archers, healers


def rage_spell(King):
    if King.alive == True:
        King.rage_effect()
    for barb in barbarians:
        if barb.alive == True:
            barb.rage_effect()
    for arch in archers:
        if arch.alive == True:
            arch.rage_effect()
    for dr in dragons:
        if dr.alive == True:
            dr.rage_effect()
    for bl in balloons:
        if bl.alive == True:
            bl.rage_effect()
    for hl in healers:
        if hl.alive == True:
            hl.rage_effect()

def heal_spell(King):
    if King.alive == True:
        King.heal_effect()
    for barb in barbarians:
        if barb.alive == True:
            barb.heal_effect()
    for arch in archers:
        if arch.alive == True:
            arch.heal_effect()
    for dr in dragons:
        if dr.alive == True:
            dr.heal_effect()
    for bl in balloons:
        if bl.alive == True:
            bl.heal_effect()