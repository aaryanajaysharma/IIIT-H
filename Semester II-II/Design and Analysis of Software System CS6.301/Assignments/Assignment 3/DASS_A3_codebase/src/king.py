import points as pt
from threading import Timer

hero = []

class King:
    def __init__(self, pos):
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.AoE = 10
        self.facing = ''
        self.attack_radius = 3
        self.position = pos
        self.alive = True


    def move(self, direction, V):
        if(self.alive == False):
            return
        vmap = V.map
        if direction == 'up':
            self.facing = 'up'
            for i in range(self.speed):
                r = self.position[0] - 1
                c = self.position[1]
                if(r < 0):
                    continue
                if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[0] -= 1
        elif direction == 'down':
            self.facing = 'down'
            for i in range(self.speed):
                r = self.position[0] + 1
                c = self.position[1]
                if(r >= len(vmap)):
                    continue
                if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[0] += 1
        elif direction == 'left':
            self.facing = 'left'
            for i in range(self.speed):
                r = self.position[0]
                c = self.position[1] - 1
                if(c < 0):
                    continue
                if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[1] -= 1
        elif direction == 'right':
            self.facing = 'right'
            for i in range(self.speed):
                r = self.position[0]
                c = self.position[1] + 1
                if(c >= len(vmap[0])):
                    continue
                if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[1] += 1
        pt.HERO_POS = self.position


    # def move(self, direction,V):
    #     if(self.alive == False):
    #         return
    #     vmap = V.map
    #     if direction == 'up':
    #         temp = self.position[0]
    #         self.position[0] -= self.speed
    #         if self.position[0] < 0:
    #             self.position[0] = 0
    #         if vmap[self.position[0]][self.position[1]] != pt.BLANK and vmap[self.position[0]][self.position[1]] != pt.SPAWN:
    #             self.position[0] = temp
    #     elif direction == 'down':
    #         temp = self.position[0]
    #         self.position[0] += self.speed
    #         if self.position[0] >= pt.config['dimensions'][0]:
    #             self.position[0] = pt.config['dimensions'][0] - 1
    #         if vmap[self.position[0]][self.position[1]] != pt.BLANK and vmap[self.position[0]][self.position[1]] != pt.SPAWN:
    #             self.position[0] = temp
    #     elif direction == 'left':
    #         temp = self.position[1]
    #         self.position[1] -= self.speed
    #         if self.position[1] < 0:
    #             self.position[1] = 0
    #         if vmap[self.position[0]][self.position[1]] != pt.BLANK and vmap[self.position[0]][self.position[1]] != pt.SPAWN:
    #             self.position[1] = temp
    #     elif direction == 'right':
    #         temp = self.position[1]
    #         self.position[1] += self.speed
    #         if self.position[1] >= pt.config['dimensions'][1]:
    #             self.position[1] = pt.config['dimensions'][1] - 1
    #         if vmap[self.position[0]][self.position[1]] != pt.BLANK and vmap[self.position[0]][self.position[1]] != pt.SPAWN:
    #             self.position[1] = temp
    #     pt.HERO_POS = self.position

    
    
    def attack_target(self, target,attack):
        if(self.alive == False):
            return
        target.health -= attack
        if target.health <= 0:
            target.health = 0
            target.destroy()

    def specialAttack(self,V):
        if(self.alive == False):
            return
        options = V.get_attack_options(self.position,self.attack_radius)
        for pos in options:
            self.attack_target(options[pos],self.AoE)

    def normalAttack(self,V):
        if(self.alive == False):
            return
        a = self.position[0]
        b = self.position[1]
        if self.facing == 'up':
            a -= 1
        elif self.facing == 'down':
            a += 1
        elif self.facing == 'left':
            b -= 1
        elif self.facing == 'right':
            b += 1
        if a < 0 or a >= pt.config['dimensions'][0] or b < 0 or b >= pt.config['dimensions'][1]:
            return
        if V.map[a][b] != pt.BLANK and V.map[a][b] != pt.SPAWN:
            target = V.get_target(a,b)
            self.attack_target(target,self.attack)
        
    
    def deal_damage(self,hit):
        if(self.alive == False):
            return
        self.health -= hit
        if self.health <= 0:
            self.health = 0
            self.kill()
    
    def kill(self):
        self.alive = False
        pt.HERO_POS = -1

    def rage_effect(self):
        self.speed = self.speed*2
        self.attack = self.attack*2
        self.AoE = self.AoE*2

    def heal_effect(self):
        self.health = self.health*1.5
        if self.health > self.max_health:
            self.health = self.max_health

class Queen:
    def __init__(self, pos):
        self.speed = 1
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.AoE = 10
        self.facing = ''
        self.attack_radius = 5
        self.attack_distance = 8
        self.position = pos
        self.alive = True
        self.specialAttackDelay = 1.0

    def move(self, direction, V):
        if(self.alive == False):
            return
        vmap = V.map
        if direction == 'up':
            self.facing = 'up'
            for i in range(self.speed):
                r = self.position[0] - 1
                c = self.position[1]
                if(r < 0):
                    continue
                if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[0] -= 1
        elif direction == 'down':
            self.facing = 'down'
            for i in range(self.speed):
                r = self.position[0] + 1
                c = self.position[1]
                if(r >= len(vmap)):
                    continue
                if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[0] += 1
        elif direction == 'left':
            self.facing = 'left'
            for i in range(self.speed):
                r = self.position[0]
                c = self.position[1] - 1
                if(c < 0):
                    continue
                if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[1] -= 1
        elif direction == 'right':
            self.facing = 'right'
            for i in range(self.speed):
                r = self.position[0]
                c = self.position[1] + 1
                if(c >= len(vmap[0])):
                    continue
                if(vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[1] += 1
        pt.HERO_POS = self.position
    
    
    def attack_target(self, target,attack):
        if(self.alive == False):
            return
        target.health -= attack
        if target.health <= 0:
            target.health = 0
            target.destroy()

    def specialAttack(self,V):
        if(self.alive == False):
            return
        r = Timer(self.specialAttackDelay,self.specialAttackfn,(V,))
        try:
            r.start()
        except:
            exit()
        
    def specialAttackfn(self,V):
        a = self.position[0]
        b = self.position[1]
        if self.facing == 'up':
            a -= 16
        elif self.facing == 'down':
            a += 16
        elif self.facing == 'left':
            b -= 16
        elif self.facing == 'right':
            b += 16
        
        a = a-4
        b = b-4

        for i in range(a,a+9):
            for j in range(b,b+9):
                if i < 0 or i >= pt.config['dimensions'][0] or j < 0 or j >= pt.config['dimensions'][1]:
                    continue
                if V.map[i][j] != pt.BLANK and V.map[i][j] != pt.SPAWN:
                    target = V.get_target(i,j)
                    self.attack_target(target,self.AoE)

    def normalAttack(self,V):
        if(self.alive == False):
            return
        a = self.position[0]
        b = self.position[1]
        if self.facing == 'up':
            a -= 8
        elif self.facing == 'down':
            a += 8
        elif self.facing == 'left':
            b -= 8
        elif self.facing == 'right':
            b += 8
        
        a = a-2
        b = b-2

        for i in range(a,a+5):
            for j in range(b,b+5):
                if i < 0 or i >= pt.config['dimensions'][0] or j < 0 or j >= pt.config['dimensions'][1]:
                    continue
                if V.map[i][j] != pt.BLANK and V.map[i][j] != pt.SPAWN:
                    target = V.get_target(i,j)
                    self.attack_target(target,self.attack)
        
    
    def deal_damage(self,hit):
        if(self.alive == False):
            return
        self.health -= hit
        if self.health <= 0:
            self.health = 0
            self.kill()
    
    def kill(self):
        self.alive = False
        pt.HERO_POS = -1

    def rage_effect(self):
        self.speed = self.speed*2
        self.attack = self.attack*2
        self.AoE = self.AoE*2

    def heal_effect(self):
        self.health = self.health*1.5
        if self.health > self.max_health:
            self.health = self.max_health
    


def spawnKing(pos):
    # convert tuple to list
    pos = list(pos)
    pt.HERO_POS = pos
    x=King(pos)
    hero.append(x)
    return x

def spawnQueen(pos):
    # convert tuple to list
    pos = list(pos)
    pt.HERO_POS = pos
    x=Queen(pos)
    hero.append(x)
    return x

def getHero(hero):
    if(hero == 0):
        return spawnKing(pt.config['hero_pos'])
    elif(hero == 1):
        return spawnQueen(pt.config['hero_pos'])