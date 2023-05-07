import sys
import os
import time

sys.path.append('./src')

import get_input
import village
import king
from map import printMap, showKingHealth, update_map
from characters import move_healers, spawnBarbarian, move_barbarians, spawnArcher, move_archers, spawnDragon, move_dragons, spawnBalloon, move_balloons, clearTroops, spawnHealer
from buildings import shoot_cannons, shoot_wizard_towers
from spells import rage_spell, heal_spell
import points as pt

getch = get_input.Get()

cnt = 0


level = 1

V = village.createVillage(level)


# For printing health of King/Queen
def Phealth(health_bar):
    if(King.health > 0):
        print()
        character = ""
        if(pt.hero == 0):
            character = "King's"
        elif(pt.hero == 1):
            character = "Queen's"
        print(character+ ' Health: ', end='')
        for i in range(len(health_bar)):
            print(health_bar[i], end='')
        print('')
        # For printing village map layout
        # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in V.map]))
        # exit()




os.system('clear')
print("Choose your Movement:\n1. Break walls\n2. Don't break walls if possible")
ch = int(input("Enter Choice: "))
if ch == 1:
    pt.movement = 2
elif ch == 2:
    pt.movement = 1
else:
    print("Invalid Choice")
    exit()
os.system('clear')
print("Choose your Hero:\n1. Barbarian King\n2. Archer Queen")
ch = int(input("Enter Choice: "))
if ch == 1:
    pt.hero = 0
elif ch == 2:
    pt.hero = 1
else:
    print("Invalid Choice")
    exit()
King = king.getHero(pt.hero)
os.system('clear')
printMap(V)
Phealth(showKingHealth(King.health))


def init_level(level):
    
    global V,King,cnt
    cnt = 0
    V = village.createVillage(level)
    os.system('clear')
    print("Choose your Hero:\n1. Barbarian King\n2. Archer Queen")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        pt.hero = 0
    elif ch == 2:
        pt.hero = 1
    King = king.getHero(pt.hero)
    os.system('clear')
    clearTroops()
    printMap(V)
    Phealth(showKingHealth(King.health))

# clear terminal

# #reposition cursor to top left
# print("\033[%d;%dH" % (0, 0), end='')

# while True:
#     pass




while(True):
    cnt += 1
    ch = get_input.input_to(getch)
    if ch == 'w':
        King.move('up', V)
    elif ch == 's':
        King.move('down', V)
    elif ch == 'a':
        King.move('left', V)
    elif ch == 'd':
        King.move('right', V)
    elif ch == '1':
        King.specialAttack(V)
    elif ch == ' ':
        King.normalAttack(V)
    elif ch == 'r':
        rage_spell(King)
    elif ch == 'h':
        heal_spell(King)
    elif ch == 'z':
        spawnBarbarian(V.spawn_points[0])
    elif ch == 'x':
        spawnBarbarian(V.spawn_points[1])
    elif ch == 'c':
        spawnBarbarian(V.spawn_points[2])
    elif ch == 'v':
        spawnDragon(V.spawn_points[0])
    elif ch == 'b':
        spawnDragon(V.spawn_points[1])
    elif ch == 'n':
        spawnDragon(V.spawn_points[2])
    elif ch == 'j':
        spawnBalloon(V.spawn_points[0])
    elif ch == 'k':
        spawnBalloon(V.spawn_points[1])
    elif ch == 'l':
        spawnBalloon(V.spawn_points[2])
    elif ch == 'e':
        spawnHealer(V.spawn_points[0])
    elif ch == 'f':
        spawnHealer(V.spawn_points[1])
    elif ch == 'g':
        spawnHealer(V.spawn_points[2])
    elif ch == 'i':
        spawnArcher(V.spawn_points[0], -1)
    elif ch == 'o':
        spawnArcher(V.spawn_points[1], -1)
    elif ch == 'p':
        spawnArcher(V.spawn_points[2], -1)
    elif ch == 'u':
        spawnArcher(V.spawn_points[0], time.time())
    elif ch == 't':
        spawnArcher(V.spawn_points[1], time.time())
    elif ch == 'm':
        spawnArcher(V.spawn_points[2], time.time())
    elif ch == 'q':
        print('quit')
        exit()
    # os.system('clear')
    move_barbarians(V, pt.movement)
    move_archers(V, pt.movement)
    move_dragons(V)
    move_balloons(V)
    move_healers(V)
    shoot_cannons(King, V)
    shoot_wizard_towers(King, V)
    if(cnt % 20 == 0):
        os.system('clear')
    print("\033[%d;%dH" % (0, 0), end='')
    printMap(V)
    Phealth(showKingHealth(King.health))
    # print('Status: ', V.check_if_game_over(King)) # Done to test why game is not ending
    if(V.check_if_game_over(King) == 1):  # next level
        level += 1
        init_level(level)
    elif(V.check_if_game_over(King) == 2):  # Victory
        os.system('clear')
        print('Victory')
        exit()
    elif(V.check_if_game_over(King) == 3):
        os.system('clear')
        print('Defeat')
        break

