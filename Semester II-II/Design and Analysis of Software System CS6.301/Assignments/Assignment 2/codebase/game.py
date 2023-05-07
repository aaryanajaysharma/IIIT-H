import colorama


from colorama import Fore, Back, Style


from src.input_starter import input_to
from src.input_starter import Get
from src.person import Person
from src.building import Building

getch = Get()
n = 50
m = 50

status = 1

rows, cols = (n, m)

checkstart = 0
z_start = 0
x_start = 0
c_start = 0

k_r = 1
k_c = 10

bz_r = 5
bz_c = 20

bx_r = 20
bx_c = 5

arr = [['' for i in range(cols)] for j in range(rows)]


bc_r = 30
bc_c = 30

t_r = 5
t_c = 5

h_r = [15, 35, 40, 40, 30]
h_c = [15, 35, 20, 10, 20]


w_r = 10
w_c = 10

c1_r = 10
c1_c = 10

c2_r = 40
c2_c = 40

bull_1_r = c1_r
bull_1_c = c1_c

bull_2_r = c2_r
bull_2_c = c2_c


# class definitons


# class King:

#     health = 100
#     beg_health = 100
#     damage = 2
#     movement_speed = 1
#     alive = 1

#     # A sample method
#     def fun(self):
#         if k_man.alive == 1:
#             global k_c
#             global k_r
#             input = input_to(getch)
#             if (k_c) > m-3:
#                 arr[k_r][k_c] = ''
#                 k_c = 0
#             if input == "d":
#                 arr[k_r][k_c] = ''
#                 k_c = k_c+k_man.movement_speed
#                 arr[k_r][k_c] = Fore.WHITE+'K'

#             if input == "a":
#                 arr[k_r][k_c] = ''
#                 k_c = k_c-k_man.movement_speed
#                 arr[k_r][k_c] = Fore.WHITE+'K'

#             if input == "s":
#                 arr[k_r][k_c] = ''
#                 k_r = k_r+k_man.movement_speed
#                 arr[k_r][k_c] = Fore.WHITE+'K'

#             if input == "w":
#                 arr[k_r][k_c] = ''
#                 k_r = k_r-k_man.movement_speed
#                 arr[k_r][k_c] = Fore.WHITE+'K'

#             if input == "k":

#                 for t in range(5):
#                     if abs(h_r[t]-k_r) <= 4 and abs(h_c[t]-k_c) <= 4:
#                         hut_list[t].health = hut_list[t].health-k_man.damage

#                 if abs(t_r-k_r) <= 4 and abs(t-k_c) <= 4:
#                     hall.health = hall.health-k_man.damage

#             if k_man.health <= 0:
#                 arr[k_r][k_c] = ''
#                 k_man.alive = 0

                # if goal_zh==6:
                # hall.health=hall.health-1
                # else:
                #  hut_list[goal_zh].health=hut_list[goal_zh].health-1

class King:
    def __init__(self):
        self.health = 100
        self.beg_health = 100
        self.damage = 2
        self.movement_speed = 1
        self.alive = 1

    def move(self):
        global k_c
        global k_r
        input_key = input_to(getch)
        if k_man.alive == 1:
            if k_c > m - 3:
                k_man.remove_from_board()
                k_c = 0
            if input_key == "d":
                k_man.remove_from_board()
                k_c += k_man.movement_speed
                k_man.add_to_board()
            if input_key == "a":
                k_man.remove_from_board()
                k_c -= k_man.movement_speed
                k_man.add_to_board()
            if input_key == "s":
                k_man.remove_from_board()
                k_r += k_man.movement_speed
                k_man.add_to_board()
            if input_key == "w":
                k_man.remove_from_board()
                k_r -= k_man.movement_speed
                k_man.add_to_board()
            if input_key == "k":
                k_man.attack()
            if k_man.health <= 0:
                k_man.die()

    def remove_from_board(self):
        arr[k_r][k_c] = ''

    def add_to_board(self):
        arr[k_r][k_c] = Fore.WHITE + 'K'

    def attack(self):
        for t in range(5):
            if abs(h_r[t]-k_r) <= 4 and abs(h_c[t]-k_c) <= 4:
                hut_list[t].health = hut_list[t].health-k_man.damage

        if abs(t_r-k_r) <= 4 and abs(t-k_c) <= 4:
            hall.health = hall.health-k_man.damage

    def die(self):
        k_man.remove_from_board()
        k_man.alive = 0


class barbarian(Person):
    health = 15
    beg_health = 15
    damage = 1
    movement_speed = 1
    alive = 1

    def fun(self):
        stat_check()

        global bz_c
        global bz_r
        global bx_c
        global bx_r
        global bc_c
        global bc_r

        global z_start
        global x_start
        global c_start

        global status

        global hut_list
        global hall

        input = input_to(getch)
        if input == "z":
            z_start = 1
            arr[bz_r][bz_c] = Fore.WHITE+'B'
        if input == "x":
            x_start = 1
            arr[bx_r][bx_c] = Fore.WHITE+'B'
        if input == "c":
            c_start = 1
            arr[bc_r][bc_c] = Fore.WHITE+'B'

        if (z_start == 1):
            arr[bz_r][bz_c] = Fore.WHITE+'B'
            zx_diff = 10000
            zy_diff = 10000
            min = zx_diff+zy_diff
            for i in range(5):
                curr_dist = abs(h_r[i]-bz_r)+abs(h_c[i]-bz_c)
                if curr_dist < min and hut_list[i].alive == 1:
                    min = curr_dist
                    goal_zr = h_r[i]
                    goal_zc = h_c[i]
                    goal_zh = i

            town_dist = abs(t_r-bz_r)+abs(t_c-bz_c)
            if town_dist < min and hall.alive == 1:
                min = town_dist
                goal_zh = 6
                goal_zr = t_r
                goal_zc = t_c

            if goal_zr > bz_r:
                arr[bz_r][bz_c] = ''
                bz_r = bz_r+1
                arr[bz_r][bz_c] = Fore.WHITE+'B'
                # arr[bz_r-1][bz_c] = ''

            else:
                arr[bz_r][bz_c] = ''
                bz_r = bz_r-1
                arr[bz_r][bz_c] = Fore.WHITE+'B'
                # arr[bz_r+1][bz_c] = ''

            if goal_zc > bz_c:
                arr[bz_r][bz_c] = ''
                bz_c = bz_c+1
                arr[bz_r][bz_c] = Fore.WHITE+'B'
                # arr[bz_r][bz_c-1] = ''

            else:
                arr[bz_r][bz_c] = ''
                bz_c = bz_c-1
                arr[bz_r][bz_c] = Fore.WHITE+'B'
                # arr[bz_r][bz_c+1] = ''

            if abs(goal_zr-bz_r) <= 1 and abs(goal_zc-bz_c) <= 1:
                if goal_zh == 6:
                    hall.health = hall.health-1
                else:
                    hut_list[goal_zh].health = hut_list[goal_zh].health-1

            if b_list[0].health <= 0:
                z_start = 0
                arr[bz_r][bz_c] = ''
                b_list[0].alive = 0

        if (x_start == 1):
            arr[bx_r][bx_c] = Fore.WHITE+'B'
            xx_diff = 10000
            xy_diff = 10000
            min = xx_diff+xy_diff
            for i in range(5):
                curr_dist = abs(h_r[i]-bx_r)+abs(h_c[i]-bx_c)
                if curr_dist < min and hut_list[i].alive == 1:
                    min = curr_dist
                    goal_xr = h_r[i]
                    goal_xc = h_c[i]
                    goal_xh = i

            town_dist = abs(t_r-bx_r)+abs(t_c-bx_c)
            if town_dist < min and hall.alive == 1:
                min = town_dist
                goal_xh = 6
                goal_xr = t_r
                goal_xc = t_c

            if goal_xr > bx_r:
                arr[bx_r][bx_c] = ''
                bx_r = bx_r+1
                arr[bx_r][bx_c] = Fore.WHITE+'B'

            else:
                arr[bx_r][bx_c] = ''
                bx_r = bx_r-1
                arr[bx_r][bx_c] = Fore.WHITE+'B'

            if goal_xc > bx_c:
                arr[bx_r][bx_c] = ''
                bx_c = bx_c+1
                arr[bx_r][bx_c] = Fore.WHITE+'B'

            else:
                arr[bx_r][bx_c] = ''
                bx_c = bx_c-1
                arr[bx_r][bx_c] = Fore.WHITE+'B'

            if abs(goal_xr-bx_r) <= 1 and abs(goal_xc-bx_c) <= 1:
                if goal_xh == 6:
                    hall.health = hall.health-1
                else:
                    hut_list[goal_xh].health = hut_list[goal_xh].health-1

            if b_list[1].health <= 0:
                x_start = 0
                arr[bx_r][bx_c] = ''
                b_list[1].alive = 0

        if (c_start == 1):
            arr[bc_r][bc_c] = Fore.WHITE+'B'
            cx_diff = 10000
            cy_diff = 10000
            min = cx_diff+cy_diff
            for i in range(5):
                curr_dist = abs(h_r[i]-bc_r)+abs(h_c[i]-bc_c)
                if curr_dist < min and hut_list[i].alive == 1:
                    min = curr_dist
                    goal_cr = h_r[i]
                    goal_cc = h_c[i]
                    goal_ch = i

            town_dist = abs(t_r-bc_r)+abs(t_c-bc_c)
            if town_dist < min and hall.alive == 1:
                min = town_dist
                goal_ch = 6
                goal_cr = t_r
                goal_cc = t_c

            if goal_cr > bc_r:
                arr[bc_r][bc_c] = ''
                bc_r = bc_r+1
                arr[bc_r][bc_c] = Fore.WHITE+'B'

            else:
                arr[bc_r][bc_c] = ''
                bc_r = bc_r-1
                arr[bc_r][bc_c] = Fore.WHITE+'B'

            if goal_cc > bc_c:
                arr[bc_r][bc_c] = ''
                bc_c = bc_c+1
                arr[bc_r][bc_c] = Fore.WHITE+'B'

            else:
                arr[bc_r][bc_c] = ''
                bc_c = bc_c-1
                arr[bc_r][bc_c] = Fore.WHITE+'B'
                # arr[bz_r][bz_c+1] = ''

            if abs(goal_cr-bc_r) <= 1 and abs(goal_cc-bc_c) <= 1:
                if goal_ch == 6:
                    hall.health = hall.health-1
                else:
                    hut_list[goal_ch].health = hut_list[goal_ch].health-1

            if b_list[2].health <= 0:
                c_start = 0
                arr[bc_r][bc_c] = ''
                b_list[2].alive = 0

    # put colour functions


class Town_hall(Building):
    height = 4
    width = 3
    health = 20
    beg_health = 20
    alive = 1


class hut(Building):
    height = 2
    width = 2
    health = 10
    beg_health = 10
    alive = 1


class wall(Building):
    height = 1
    width = 1
    health = 100
    beg_health = 100


class cannon(Building):
    height = 1
    width = 1
    health = 100
    beg_health = 100

    def fun(self):

        global bz_c
        global bz_r
        global bx_c
        global bx_r
        global bc_c
        global bc_r

        global c1_r
        global c1_c
        global c2_r
        global c2_c

        global z_start
        global x_start
        global c_start

        global bull_1_r
        global bull_1_c
        global bull_2_r
        global bull_2_c

        global k_man

        min_target_1 = 10000
        target_1 = 0

        min_target_2 = 10000
        target_2 = 0

        if abs(c1_r-bz_r)+abs(c1_c-bz_c) < min_target_1 and z_start == 1:
            min_target_1 = abs(c1_r-bz_r)+abs(c1_c-bz_c)
            target_1 = 1

        if abs(c1_r-bx_r)+abs(c1_c-bx_c) < min_target_1 and x_start == 1:
            min_target_1 = abs(c1_r-bx_r)+abs(c1_c-bx_c)
            target_1 = 2

        if abs(c1_r-bc_r)+abs(c1_c-bc_c) < min_target_1 and c_start == 1:
            min_target_1 = abs(c1_r-bc_r)+abs(c1_c-bc_c)
            target_1 = 3

        if abs(c1_r-k_r)+abs(c1_c-k_c) < min_target_1 and k_man.alive == 1:
            min_target_1 = abs(c1_r-k_r)+abs(c1_c-k_c)
            target_1 = 4

        if target_1 == 1:
            if bull_1_r < bz_r-1:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_r = bull_1_r+1
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_r = bull_1_r-1
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < bz_c-1:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_c = bull_1_c+1
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_c = bull_1_c-1
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-bz_r) <= 2 and abs(bull_1_c-bz_c) <= 2:
                b_list[target_1-1].health = b_list[target_1-1].health-1

        if target_1 == 2:
            if bull_1_r < bx_r-1:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_r = bull_1_r+2
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_r = bull_1_r-2
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < bx_c-1:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_c = bull_1_c+2
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_c = bull_1_c-2
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-bx_r) <= 2 and abs(bull_1_c-bx_c) <= 2:
                b_list[target_1-1].health = b_list[target_1-1].health-1

        if target_1 == 3:
            if bull_1_r < bc_r-1:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_r = bull_1_r+3
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_r = bull_1_r-3
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < bc_c-1:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_c = bull_1_c+3
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_c = bull_1_c-3
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-bc_r) <= 2 and abs(bull_1_c-bc_c) <= 2:
                b_list[target_1-1].health = b_list[target_1-1].health-1

        if target_1 == 4:
            if bull_1_r < k_r-1:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_r = bull_1_r+1
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_r = bull_1_r-1
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < k_c-1:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_c = bull_1_c+1
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                arr[bull_1_r][bull_1_c] = ''
                bull_1_c = bull_1_c-1
                arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-k_r) <= 2 and abs(bull_1_c-k_c) <= 2:
                k_man.health = k_man.health-1

        # cannon 2

        if abs(c2_r-bz_r)+abs(c2_c-bz_c) < min_target_2 and z_start == 1:
            min_target_2 = abs(c2_r-bz_r)+abs(c2_c-bz_c)
            target_2 = 1

        if abs(c2_r-bx_r)+abs(c2_c-bx_c) < min_target_2 and x_start == 1:
            min_target_2 = abs(c2_r-bx_r)+abs(c2_c-bx_c)
            target_2 = 2

        if abs(c2_r-bc_r)+abs(c2_c-bc_c) < min_target_2 and c_start == 1:
            min_target_2 = abs(c2_r-bc_r)+abs(c2_c-bc_c)
            target_2 = 3

        if abs(c2_r-k_r)+abs(c2_c-k_c) < min_target_2 and k_man.alive == 1:
            min_target_2 = abs(c2_r-k_r)+abs(c2_c-k_c)
            target_2 = 4

        if target_2 == 1:
            if bull_2_r < bz_r-1:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_r = bull_2_r+1
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_r = bull_2_r-1
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < bz_c-1:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_c = bull_2_c+1
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_c = bull_2_c-1
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-bz_r) <= 2 and abs(bull_2_c-bz_c) <= 2:
                b_list[target_2-1].health = b_list[target_2-1].health-1

        if target_2 == 2:
            if bull_2_r < bx_r-1:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_r = bull_2_r+2
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_r = bull_2_r-2
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < bx_c-1:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_c = bull_2_c+2
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_c = bull_2_c-2
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-bx_r) <= 2 and abs(bull_2_c-bx_c) <= 2:
                b_list[target_2-1].health = b_list[target_2-1].health-1

        if target_2 == 3:
            if bull_2_r < bc_r-1:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_r = bull_2_r+3
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_r = bull_2_r-3
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < bc_c-1:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_c = bull_2_c+3
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_c = bull_2_c-3
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-bc_r) <= 2 and abs(bull_2_c-bc_c) <= 2:
                b_list[target_2-1].health = b_list[target_2-1].health-1

        if target_2 == 4:
            if bull_2_r < k_r-1:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_r = bull_2_r+1
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_r = bull_2_r-1
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < k_c-1:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_c = bull_2_c+1
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ''
                bull_2_c = bull_2_c-1
                arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-k_r) <= 2 and abs(bull_2_c-k_c) <= 2:
                k_man.health = k_man.health-1

        #############


# end class definitions


# function definitions

def end_check():
    input = input_to(getch)
    if input == "t":
        quit()


def stat_check():
    global status
    if hut_list[0].alive == 0 and hut_list[1].alive == 0 and hut_list[2].alive == 0 and hut_list[3].alive == 0 and hut_list[4].alive == 0 and hall.alive == 0:
        status = 0
        print("victory to the attacking team")
        exit()

    if b_list[0].alive == 0 and b_list[1].alive == 0 and b_list[2].alive == 0 and k_man.alive == 0:
        status = 0
        print("victory to the defending team")
        exit()


def spell():
    input = input_to(getch)
    if input == "r":
        k_man.movement_speed = 2
        k_man.damage = k_man.damage*2
    if input == "h":
        k_man.health = k_man.health*1.5


def render():

    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    global checkstart
    if checkstart == 1:
        for i in range(n):
            print(CURSOR_UP_ONE+ERASE_LINE+CURSOR_UP_ONE)

    for row in arr:
        print(*row)

    checkstart = 1


b_list = []
b_list.append(barbarian(initial_health=15))
b_list.append(barbarian(initial_health=15))
b_list.append(barbarian(initial_health=15))


k_man = King()


arr[k_r][k_c] = 'K'

arr[bz_r][bz_c] = 'B'
arr[bx_r][bx_c] = 'B'
arr[bc_r][bc_c] = 'B'


def place():
    # arr[k_r][k_c] = Fore.WHITE+'K'
    # arr[b_r][b_c] = Fore.WHITE+'B'

    hall.find_colour()
    if hall.colour == 'G':
        for i in range(t_r, t_r+hall.height):
            for j in range(t_c, t_c+hall.width):
                arr[i][j] = Fore.GREEN+'T'
    elif hall.colour == 'Y':
        for i in range(t_r, t_r+hall.height):
            for j in range(t_c, t_c+hall.width):
                arr[i][j] = Fore.YELLOW+'T'
    elif hall.colour == 'R':
        for i in range(t_r, t_r+hall.height):
            for j in range(t_c, t_c+hall.width):
                arr[i][j] = Fore.RED+'T'
    else:
        for i in range(t_r, t_r+hall.height):
            for j in range(t_c, t_c+hall.width):
                arr[i][j] = ''

    hut_list[0].find_colour()
    hut_list[1].find_colour()
    hut_list[2].find_colour()
    hut_list[3].find_colour()
    hut_list[4].find_colour()

    for a in range(5):
        if hut_list[a].colour == 'G':
            for i in range(h_r[a], h_r[a]+hut_list[a].height):
                for j in range(h_c[a], h_c[a]+hut_list[a].width):
                    arr[i][j] = Fore.GREEN+'H'
        elif hut_list[a].colour == 'Y':
            for i in range(h_r[a], h_r[a]+hut_list[a].height):
                for j in range(h_c[a], h_c[a]+hut_list[a].width):
                    arr[i][j] = Fore.YELLOW+'H'
        elif hut_list[a].colour == 'R':
            for i in range(h_r[a], h_r[a]+hut_list[a].height):
                for j in range(h_c[a], h_c[a]+hut_list[a].width):
                    arr[i][j] = Fore.RED+'H'
        else:
            for i in range(h_r[a], h_r[a]+hut_list[a].height):
                for j in range(h_c[a], h_c[a]+hut_list[a].width):
                    arr[i][j] = ''

    wall_obj = wall(initial_health=100)
    wall_obj.find_colour()
    if wall_obj.colour == 'G':
        for i in range(w_r, w_r+wall_obj.height):
            for j in range(w_c, w_c+wall_obj.width):
                arr[i][j] = Fore.GREEN+'W'
    elif wall_obj.colour == 'Y':
        for i in range(w_r, w_r+wall_obj.height):
            for j in range(w_c, w_c+wall_obj.width):
                arr[i][j] = Fore.YELLOW+'W'
    elif wall_obj.colour == 'R':
        for i in range(w_r, w_r+wall_obj.height):
            for j in range(w_c, w_c+wall_obj.width):
                arr[i][j] = Fore.RED+'W'
    else:
        for i in range(w_r, w_r+wall_obj.height):
            for j in range(w_c, w_c+wall_obj.width):
                arr[i][j] = Fore.BLUE+'W'

    cannon_obj_1 = cannon(initial_health=100)
    cannon_obj_2 = cannon(initial_health=100)
    cannon_obj_1.find_colour()
    if cannon_obj_1.colour == 'G':
        for i in range(c1_r, c1_r+cannon_obj_1.height):
            for j in range(c1_c, c1_c+cannon_obj_1.width):
                arr[i][j] = Fore.GREEN+'C'
    elif cannon_obj_1.colour == 'Y':
        for i in range(c1_r, c1_r+cannon_obj_1.height):
            for j in range(c1_c, c1_c+cannon_obj_1.width):
                arr[i][j] = Fore.YELLOW+'C'
    elif cannon_obj_1.colour == 'R':
        for i in range(c1_r, c1_r+cannon_obj_1.height):
            for j in range(c1_c, c1_c+cannon_obj_1.width):
                arr[i][j] = Fore.RED+'C'
    else:
        for i in range(c1_r, c1_r+cannon_obj_1.height):
            for j in range(c1_c, c1_c+cannon_obj_1.width):
                arr[i][j] = Fore.BLUE+'C'

    cannon_obj_2.find_colour()
    if cannon_obj_2.colour == 'G':
        for i in range(c2_r, c2_r+cannon_obj_2.height):
            for j in range(c2_c, c2_c+cannon_obj_2.width):
                arr[i][j] = Fore.GREEN+'C'
    elif cannon_obj_2.colour == 'Y':
        for i in range(c2_r, c2_r+cannon_obj_2.height):
            for j in range(c2_c, c2_c+cannon_obj_2.width):
                arr[i][j] = Fore.YELLOW+'C'
    elif cannon_obj_2.colour == 'R':
        for i in range(c2_r, c2_r+cannon_obj_2.height):
            for j in range(c2_c, c2_c+cannon_obj_2.width):
                arr[i][j] = Fore.RED+'C'
    else:
        for i in range(c2_r, c2_r+cannon_obj_2.height):
            for j in range(c2_c, c2_c+cannon_obj_2.width):
                arr[i][j] = Fore.BLUE+'C'


def revise():
    Rodger = King()
    Rodger.move()
    Barb = barbarian(initial_health=15)
    Barb.fun()
    Cann = cannon(initial_health=100)
    Cann.fun()


# end function definitions


hut_list = []
hut_list.append(hut(initial_health=10))
hut_list.append(hut(initial_health=10))
hut_list.append(hut(initial_health=10))
hut_list.append(hut(initial_health=10))
hut_list.append(hut(initial_health=10))

hall = Town_hall(initial_health=20)


# putting things on the grid


while status == 1:
    place()
    render()
    revise()
    spell()
    end_check()
    stat_check()

    # break
