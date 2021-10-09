import BRA_database as bra
import sys

#bra.drop_tables()
#bra.create_tables()
#bra.fill_creature_table()
#bra.delete_creature()
#bra.copy_creature()
#bra.add_creature()
#test commit

while True:
    option = int(input("""
    What do you want to do?
    [1] Delete the tables.
    [2] Create the tables.
    [3] Display Creature table.
    [4] Fill the Creatures table.
    [5] Add a Creature.
    [6] Delete a Creature.
    [7] Copy a Creature.
    [8] Quit
    [9] Add encounter.
    """))

    if option == 1:
        bra.drop_tables()
    elif option == 2:
        bra.create_tables()
    elif option == 3:
        bra.display_creature_table()
    elif option == 4:
        bra.fill_creature_table()
    elif option == 5:
        bra.add_creature()
    elif option == 6:
        bra.delete_creature()
    elif option == 7:
        bra.copy_creature()
    elif option == 8:
        sys.exit()
    elif option == 9:
        bra.create_enconter()
    else:
        continue

#test edit366

