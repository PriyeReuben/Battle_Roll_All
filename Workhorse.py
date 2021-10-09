from Creature import Creature
from Attack import Attack
from Dice import Dice

target_AC = 15
hitpoints = 500

bandit = Creature("Bandit", 2, 3, 2, 0, 14)  #name, proficiency_bonus, strength_mod, dexterity_mod, casting_mod, armor_class
shortsword_attack = Attack("shortsword", 5, False, False, 0, 0, 1, [1,8,"slashing"])  #name, attack_bonus, advantage, disadvantage, bonus, penalty, number_of_attacks, damage_dice


#attack_roll = Dice(1,20,"")
#damage_roll = Dice(2, 6, "slashing")
#attack_roll.attack_roll()

attack_mod = input("What ability score is used in the attack? [s]trength, [d]exterity, or [c]asting")
if attack_mod == 's':
    attack_mod = bandit.strength_mod
elif attack_mod == 'd':
    attack_mod = bandit.dexterity_mod
elif attack_mod == 'c':
    attack_mod = bandit.casting_mod
else: #this code runs on the assumption that the correct input will be given.  Foolish.
    print("You get nothing!  choose better next time.")
    attack_mod = 0



attack_bonus = bandit.proficiency_bonus + attack_mod

while hitpoints>0:
    attack_roll = Dice(1, 20, attack_bonus, "to hit")
    attack_result = attack_roll.roll()
    #attack_roll.roll() #remember this for the future.
    if attack_result < target_AC or attack_result - attack_bonus == 1:
        print("You missed!\n___________")
        #done?
    elif attack_result == 20:
        print("Critical hit!")
        damage_roll = Dice(4, 6, attack_mod, "slashing")
        damage_result = damage_roll.roll()
        print("You did " + str(damage_result) + " points of " + damage_roll.damage_type + " damage.\n___________")
        hitpoints = hitpoints - damage_result
    else:
        print("You hit with a " + str(attack_result) + "!")
        damage_roll = Dice(2, 6, attack_mod, "slashing")
        damage_result = damage_roll.roll()
        print("You did " + str(damage_result) + " points of " + damage_roll.damage_type + " damage.\n___________")
        hitpoints = hitpoints - damage_result

print("This isn't brave, it's murder.")
    #damage_roll = Dice(2, 6, "slashing")
    #attack_roll.roll()
    #damage_roll.roll()
    #print("You rolled "+ str(attack_roll.roll()))
