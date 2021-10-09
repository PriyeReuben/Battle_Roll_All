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
    [4] Modify the Creatures table.
    [8] Quit
    [9] Add encounter.
    """))

    if option == 1:
        confirm = str(input("Are you sure?  This will delete all tables permanently. Y/N: "))
        if confirm == 'y' or confirm == 'Y':
            bra.drop_tables()
            print("Tables deleted.")
        else:
            print("Tables not deleted.")
    elif option == 2:
        bra.create_tables()
    elif option == 3:
        bra.display_creature_table()
    elif option == 4:
        bra.fill_creature_table()
    elif option == 8:
        sys.exit()
    elif option == 9:
        bra.create_enconter()
    else:
        continue

#test edit366

