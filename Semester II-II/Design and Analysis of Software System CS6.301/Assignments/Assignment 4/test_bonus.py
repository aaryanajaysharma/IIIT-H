import unittest

import king
import village as v
import copy
# import points as pt
# unit test to test the King.move() function

V = v.createVillage(1)
class TestAttackTarget(unittest.TestCase):
    def setUp(self):
        self.king = king.getHero(0)
        self.village = v.createVillage(1)

    def test_isAlive(self):
        for i in self.village.cannon_objs.values():
            artributes = [self.king.max_health, self.king.attack, self.king.AoE, self.king.attack_radius]
            attack = self.king.attack
            previous_health = i.health
            self.king.attack_target(i,attack)
            self.assertTrue(self.king.alive)
            # checking if health of target is reduced
            new_health = previous_health - attack
            self.assertGreater(i.health, 0, "incorrect health")
            if(new_health == 0):
                self.assertEqual(i.destroyed, True, "incorrect destroyed")
            self.assertEqual(i.health, new_health, "incorrect health")
            # checking if other attributes are changed
            self.assertEqual(self.king.max_health, artributes[0], "incorrect max_health")
            self.assertEqual(self.king.attack, artributes[1], "incorrect attack")
            self.assertEqual(self.king.AoE, artributes[2], "incorrect AoE")
            self.assertEqual(self.king.attack_radius, artributes[3], "incorrect attack_radius")
    def main(self):
        runner = unittest.TextTestRunner()
        final_answer = runner.run(unittest.makeSuite(TestAttackTarget))
        with open("output_bonus.txt", "w") as file:
            file.write(str(final_answer.wasSuccessful()) + "\n")
            file.close()
    
if __name__ == '__main__':
    TestAttackTarget_object = TestAttackTarget()
    TestAttackTarget_object.main()
            
        