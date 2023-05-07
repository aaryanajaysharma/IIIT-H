import numpy as np
import points as pt
import buildings as bd
import collections
from characters import barbarians, dragons,balloons, archers


class Village:
    def __init__(self, config, level):
        self.level = level
        self.dimensions = config['dimensions']     # dimesions of the village
        # coords spawn points of the village
        self.spawn_points = config['spawn_points']
        # coords of top left corner of town hall of the village
        self.town_hall = config['town_hall']
        # coords of top left corner of huts of the village
        self.huts = config['huts']
        # coords of walls of the village
        self.walls_top = config['walls_top']
        self.walls_bottom = config['walls_bottom']
        self.walls_left = config['walls_left']
        self.walls_right = config['walls_right']
        self.walls_topright = config['walls_topright']
        self.walls_topleft = config['walls_topleft']
        self.walls_bottomright = config['walls_bottomright']
        self.walls_bottomleft = config['walls_bottomleft']
        # coords of top left corner of cannons of the village
        self.cannons = config['cannons']
        self.wizard_towers = config['wizard_towers']
        self.hut_objs = {}
        self.cannon_objs = {}
        self.wizard_tower_objs = {}
        self.wall_objs = {}
        self.town_hall_obj = bd.TownHall(self.town_hall, self)
        self.map = self.generate_map()             # map of the village

    def generate_map(self):
        map = np.empty(self.dimensions, dtype="<U10")
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                map[i][j] = pt.BLANK
        for spawn_point in self.spawn_points:
            map[spawn_point[0]][spawn_point[1]] = pt.SPAWN
        for hut in self.huts:                                           # hut is 2x2
            hut_obj = bd.Hut(hut, self)
            self.hut_objs[hut] = hut_obj
            map[hut[0]][hut[1]] = pt.HUT + ":" + \
                str(hut[0]) + ":" + str(hut[1])
            map[hut[0]+1][hut[1]] = pt.HUT + ":" + \
                str(hut[0]) + ":" + str(hut[1])
            map[hut[0]][hut[1]+1] = pt.HUT + ":" + \
                str(hut[0]) + ":" + str(hut[1])
            map[hut[0]+1][hut[1]+1] = pt.HUT + \
                ":" + str(hut[0]) + ":" + str(hut[1])
        for wall in self.walls_top:                                     # wall is 1x1
            wall_obj = bd.Wall(wall, self)
            self.wall_objs[wall] = wall_obj
            map[wall[0]][wall[1]] = pt.WALL_TOP
        for wall in self.walls_bottom:
            wall_obj = bd.Wall(wall, self)
            self.wall_objs[wall] = wall_obj
            map[wall[0]][wall[1]] = pt.WALL_BOTTOM
        for wall in self.walls_left:
            wall_obj = bd.Wall(wall, self)
            self.wall_objs[wall] = wall_obj
            map[wall[0]][wall[1]] = pt.WALL_LEFT
        for wall in self.walls_right:
            wall_obj = bd.Wall(wall, self)
            self.wall_objs[wall] = wall_obj
            map[wall[0]][wall[1]] = pt.WALL_RIGHT
        for wall in self.walls_topright:
            wall_obj = bd.Wall(wall, self)
            self.wall_objs[wall] = wall_obj
            map[wall[0]][wall[1]] = pt.WALL_TOPRIGHT
        for wall in self.walls_topleft:
            wall_obj = bd.Wall(wall, self)
            self.wall_objs[wall] = wall_obj
            map[wall[0]][wall[1]] = pt.WALL_TOPLEFT
        for wall in self.walls_bottomright:
            wall_obj = bd.Wall(wall, self)
            self.wall_objs[wall] = wall_obj
            map[wall[0]][wall[1]] = pt.WALL_BOTTOMRIGHT
        for wall in self.walls_bottomleft:
            wall_obj = bd.Wall(wall, self)
            self.wall_objs[wall] = wall_obj
            map[wall[0]][wall[1]] = pt.WALL_BOTTOMLEFT
        for cannon in self.cannons:                                     # cannon is 2x2
            cannon_obj = bd.Cannon(cannon, self)
            self.cannon_objs[cannon] = cannon_obj
            map[cannon[0]][cannon[1]] = pt.CANNON + ":" + \
                str(cannon[0]) + ":" + str(cannon[1])
            map[cannon[0]+1][cannon[1]] = pt.CANNON + \
                ":" + str(cannon[0]) + ":" + str(cannon[1])
            map[cannon[0]][cannon[1]+1] = pt.CANNON + \
                ":" + str(cannon[0]) + ":" + str(cannon[1])
            map[cannon[0]+1][cannon[1]+1] = pt.CANNON + \
                ":" + str(cannon[0]) + ":" + str(cannon[1])
        for wizard_tower in self.wizard_towers:                          # wizard tower is 1X1
            wizard_tower_obj = bd.WizardTower(wizard_tower, self)
            self.wizard_tower_objs[wizard_tower] = wizard_tower_obj
            map[wizard_tower[0]][wizard_tower[1]] = pt.WIZARD_TOWER + \
                ":" + str(wizard_tower[0]) + ":" + str(wizard_tower[1])

        # town hall is 4x3
        for i in range(self.town_hall[0], self.town_hall[0]+4):
            for j in range(self.town_hall[1], self.town_hall[1]+3):
                map[i][j] = pt.TOWNHALL

        return map

    def update_map(self, map):
        self.map = map

    def remove_hut(self, hut_obj):
        self.hut_objs.pop(hut_obj.position)
        hut_coords = hut_obj.position
        for i in range(hut_coords[0], hut_coords[0]+2):
            for j in range(hut_coords[1], hut_coords[1]+2):
                self.map[i][j] = pt.BLANK

    def remove_cannon(self, cannon_obj):
        self.cannon_objs.pop(cannon_obj.position)
        cannon_coords = cannon_obj.position
        for i in range(cannon_coords[0], cannon_coords[0]+2):
            for j in range(cannon_coords[1], cannon_coords[1]+2):
                self.map[i][j] = pt.BLANK

    def remove_wizard_tower(self, wizard_tower_obj):
        self.wizard_tower_objs.pop(wizard_tower_obj.position)
        wizard_tower_coords = wizard_tower_obj.position
        self.map[wizard_tower_coords[0]][wizard_tower_coords[1]] = pt.BLANK

    def remove_wall(self, wall_obj):
        self.wall_objs.pop(wall_obj.position)
        self.map[wall_obj.position[0]][wall_obj.position[1]] = pt.BLANK

    def remove_town_hall(self, town_hall_obj):
        self.town_hall_obj = None
        town_coords = town_hall_obj.position
        for i in range(town_coords[0], town_coords[0]+4):
            for j in range(town_coords[1], town_coords[1]+3):
                self.map[i][j] = pt.BLANK

    def get_attack_options(self, position, radius):
        attack_options = {}
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                if (position[0]-i)**2 + (position[1]-j)**2 <= radius**2:
                    if self.map[i][j].split(':')[0] == pt.HUT:
                        a = int(self.map[i][j].split(':')[1])
                        b = int(self.map[i][j].split(':')[2])
                        hut_obj = self.hut_objs[(a, b)]
                        if hut_obj.destroyed == False:
                            attack_options[(a, b)] = hut_obj
                    elif self.map[i][j].split(':')[0] == pt.CANNON:
                        a = int(self.map[i][j].split(':')[1])
                        b = int(self.map[i][j].split(':')[2])
                        cannon_obj = self.cannon_objs[(a, b)]
                        if cannon_obj.destroyed == False:
                            attack_options[(a, b)] = cannon_obj
                    elif self.map[i][j].split(':')[0] == pt.WIZARD_TOWER:
                        a = int(self.map[i][j].split(':')[1])
                        b = int(self.map[i][j].split(':')[2])
                        wizard_tower_obj = self.wizard_tower_objs[(a, b)]
                        if wizard_tower_obj.destroyed == False:
                            attack_options[(a, b)] = wizard_tower_obj
                    elif self.map[i][j] == pt.WALL:
                        wall_obj = self.wall_objs[(i, j)]
                        if wall_obj.destroyed == False:
                            attack_options[(i, j)] = wall_obj
                    elif self.map[i][j] == pt.TOWNHALL:
                        town_hall_obj = self.town_hall_obj
                        if town_hall_obj.destroyed == False:
                            attack_options[(i, j)] = town_hall_obj
        return attack_options

    def get_target(self, a, b):
        target = None
        if self.map[a][b].split(':')[0] == pt.HUT:
            x = int(self.map[a][b].split(':')[1])
            y = int(self.map[a][b].split(':')[2])
            target = self.hut_objs[(x, y)]
        elif self.map[a][b].split(':')[0] == pt.CANNON:
            x = int(self.map[a][b].split(':')[1])
            y = int(self.map[a][b].split(':')[2])
            target = self.cannon_objs[(x, y)]
        elif self.map[a][b].split(':')[0] == pt.WIZARD_TOWER:
            x = int(self.map[a][b].split(':')[1])
            y = int(self.map[a][b].split(':')[2])
            target = self.wizard_tower_objs[(x, y)]
        elif self.map[a][b] == pt.WALL:
            target = self.wall_objs[(a, b)]
        elif self.map[a][b] == pt.TOWNHALL:
            target = self.town_hall_obj
        return target

    def check_if_game_over(self, King):
        all_buildings = collections.ChainMap(
            self.hut_objs, self.cannon_objs, self.wizard_tower_objs)
        if len(all_buildings) == 0 and self.town_hall_obj == None:
            if self.level != 3:
                return 1
            else:
                return 2
        elif King.alive == False and len(barbarians) == 0 and len(dragons) == 0 and len(balloons) == 0 and len(archers) == 0:
            return 3
        else:
            return 0


def createVillage(level):
    village = Village(getConfig(level), level)
    return village


def getConfig(level):
    if(level == 1):
        return pt.config_level_1
    elif(level == 2):
        return pt.config_level_2
    elif(level == 3):
        return pt.config_level_3
