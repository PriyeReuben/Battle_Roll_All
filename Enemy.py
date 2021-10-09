import Creature
import Attack
import Dice

class Enemy:
    def __init__(self, Creature, Attack, Dice):
        self.Creature = Creature()
        self.Attack = Attack()

Bandit = Enemy(Creature("Bandit", 2, 2, 3, 0, 14), Attack("shortsword", 5, False, False, 0, 0, 1, [1,8,"slashing"]))
Bandit.Dice.roll(Bandit.Attack.damage_dice)
