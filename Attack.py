import Dice as dice
class Attack:
    def __init__(self, name, attack_bonus, advantage, disadvantage, bonus, penalty, number_of_attacks, damage_dice):
        self.name = name
        self.attack_bonus = attack_bonus
        self.advantage = advantage
        self.disadvantage = disadvantage
        self.bonus = bonus
        self.penalty = penalty
        self.number_of_attacks = number_of_attacks
        self.damage_dice = damage_dice
        #self.additional_damage  #this should be a list that can be appended to to account for extra damage types like sneak attack or flaming

"""
A1 = Attack("shortsword", 5, False, False, 0, 0, 2, [1,8,"slashing"])
D1 = dice.Dice(A1.damage_dice[0], A1.damage_dice[1], A1.damage_dice[2])

for i in range(A1.number_of_attacks):
    D1.roll(1,20, "to attack") #Attack
    D1.roll(A1.damage_dice[0], A1.damage_dice[1], A1.damage_dice[2]) #damage
"""



