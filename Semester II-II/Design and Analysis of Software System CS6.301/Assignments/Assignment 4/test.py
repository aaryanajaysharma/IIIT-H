import unittest

import king
import village as v
import copy
# import points as pt
# unit test to test the King.move() function

V = v.createVillage(1)
class TestKingMove(unittest.TestCase):
    def setUp(self):
        self.king = king.getHero(0)
        self.village = v.createVillage(1)
        self.king.alive = True
    def test_move_up(self):
        # self.king.move('up', self.village)
       
        artributes = [self.king.max_health, self.king.attack, self.king.AoE, self.king.attack_radius]
        for i in range(35):
            for j in range(17):
                if(V.map[j][i] == '0'):
                    self.king.position = [j, i]
                    # print(self.king.position)

                    # up = copy.deepcopy(self.king.position)
                    self.king.move('up', self.village)
                    # Checking if face is right
                    self.assertEqual(self.king.facing, 'up', "incorrect face")
                    # print(j, i)
                    # print(self.king.position)
                    if j == 0:
                        self.assertEqual(self.king.position, [j, i], "incorrect position")
                    else:
                        if(V.map[j-1][i] == '0' or V.map[j-1][i] == '2'):
                            # up[0]-=1
                            self.assertEqual(self.king.position, [j-1, i], "incorrect position")
                        else:
                            self.assertEqual(self.king.position, [j, i], "incorrect position")
                    # checking if other attributes are changed
                    self.assertEqual(self.king.max_health, artributes[0], "incorrect max_health")
                    self.assertEqual(self.king.attack, artributes[1], "incorrect attack")
                    self.assertEqual(self.king.AoE, artributes[2], "incorrect AoE")
                    self.assertEqual(self.king.attack_radius, artributes[3], "incorrect attack_radius")
        # self.assertEqual(self.king.position, [16, 35], "incorrect position")

    def test_move_down(self):
        artributes = [self.king.max_health, self.king.attack, self.king.AoE, self.king.attack_radius]
        for i in range(35):
            for j in range(17):
                if(V.map[j][i] == '0'):
                    self.king.position = [j, i]
                    # print(self.king.position)

                    # up = copy.deepcopy(self.king.position)
                    self.king.move('down', self.village)
                    # Checking if face is right
                    self.assertEqual(self.king.facing, 'down', "incorrect face")
                    # print(j, i)
                    # print(self.king.position)
                    if j == 17:
                        self.assertEqual(self.king.position, [j, i], "incorrect position")
                    else:
                        if(V.map[j+1][i] == '0' or V.map[j+1][i] == '2'):
                            # up[0]-=1
                            self.assertEqual(self.king.position, [j+1, i], "incorrect position")
                        else:
                            self.assertEqual(self.king.position, [j, i], "incorrect position")
                    # checking if other attributes are changed
                    self.assertEqual(self.king.max_health, artributes[0], "incorrect max_health")
                    self.assertEqual(self.king.attack, artributes[1], "incorrect attack")
                    self.assertEqual(self.king.AoE, artributes[2], "incorrect AoE")
                    self.assertEqual(self.king.attack_radius, artributes[3], "incorrect attack_radius")

    def test_move_left(self):
        artributes = [self.king.max_health, self.king.attack, self.king.AoE, self.king.attack_radius]
        for i in range(35):
            for j in range(17):
                if(V.map[j][i] == '0'):
                    self.king.position = [j, i]
                    # print(self.king.position)

                    # up = copy.deepcopy(self.king.position)
                    self.king.move('left', self.village)
                    # Checking if face is right
                    self.assertEqual(self.king.facing, 'left', "incorrect face")
                    # print(j, i)
                    # print(self.king.position)
                    if i == 0:
                        self.assertEqual(self.king.position, [j, i], "incorrect position")
                    else:
                        if(V.map[j][i-1] == '0' or V.map[j][i-1] == '2'):
                            # up[0]-=1
                            self.assertEqual(self.king.position, [j, i-1], "incorrect position")
                        else:
                            self.assertEqual(self.king.position, [j, i], "incorrect position")
                    self.assertEqual(self.king.max_health, artributes[0], "incorrect max_health")
                    self.assertEqual(self.king.attack, artributes[1], "incorrect attack")
                    self.assertEqual(self.king.AoE, artributes[2], "incorrect AoE")
                    self.assertEqual(self.king.attack_radius, artributes[3], "incorrect attack_radius")

    def test_move_right(self):
        artributes = [self.king.max_health, self.king.attack, self.king.AoE, self.king.attack_radius]
        for i in range(35):
            for j in range(17):
                if(V.map[j][i] == '0'):
                    self.king.position = [j, i]
                    # print(self.king.position)

                    # up = copy.deepcopy(self.king.position)
                    self.king.move('right', self.village)
                    # Checking if face is right
                    self.assertEqual(self.king.facing, 'right', "incorrect face")
                    # print(j, i)
                    # print(self.king.position)
                    if i == 35:
                        self.assertEqual(self.king.position, [j, i], "incorrect position")
                    else:
                        if(V.map[j][i+1] == '0' or V.map[j][i+1] == '2'):
                            # up[0]-=1
                            self.assertEqual(self.king.position, [j, i+1], "incorrect position")
                        else:
                            self.assertEqual(self.king.position, [j, i], "incorrect position")
                    self.assertEqual(self.king.max_health, artributes[0], "incorrect max_health")
                    self.assertEqual(self.king.attack, artributes[1], "incorrect attack")
                    self.assertEqual(self.king.AoE, artributes[2], "incorrect AoE")
                    self.assertEqual(self.king.attack_radius, artributes[3], "incorrect attack_radius")
                    self.assertGreater(self.king.speed, 0, "speed is negative")
    def test_king_dead(self):
        self.king.alive = False
        previous_position = copy.deepcopy(self.king.position)
        self.king.move('up', self.village)
        self.assertEqual(self.king.position, previous_position, "incorrect position")

    def main(self):
            runner = unittest.TextTestRunner()
            final_answer = runner.run(unittest.makeSuite(TestKingMove))
            with open("output.txt", "w") as file:
                file.write(str(final_answer.wasSuccessful()) + "\n")
                file.close()
    
if __name__ == '__main__':
    TestKingMove_object = TestKingMove()
    TestKingMove_object.main()
    # run the test
        