import random as rand
class Dice:
    def __init__(self, number_of_dice, type_of_dice, flat_bonus, damage_type):
        self.number_of_dice = number_of_dice
        self.type_of_dice = type_of_dice
        self.damage_type = damage_type
        self.flat_bonus = flat_bonus
        #self.dice_log = dice_log

    def roll(self):

        total = 0
        dice_log = []

        for i in range(self.number_of_dice):
            current = rand.randint(1, self.type_of_dice)
            total = total + current
            dice_log.append(current)
        total = total + self.flat_bonus


        return(total)

    def return_damage_type(self):
        return self.damage_type

#SaniSensei: rolling with advantage could be as simple as: result = max(d20.roll(2))
#D1 = Dice(20,8,"")
#D1.roll()

