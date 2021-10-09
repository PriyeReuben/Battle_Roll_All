import sqlite3
#test commit

conn = sqlite3.connect('BRA.db')
cur = conn.cursor()

def create_tables():
    conn = sqlite3.connect('BRA.db')
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE Creatures(
            name text UNIQUE,
            proficiency_bonus integer,
            strength_mod integer,
            dexterity_mod integer,
            casting_mod integer,
            armor_class integer    
        )
    """)
    #this needs to change.  this should be a weapon table, that combines with creature to make an attack.
    cur.execute("""
        CREATE TABLE Attacks(
            name text,
            advantage integer,
            disadvantage integer,
            static_bonus integer,
            number_of_attacks integer,
            base_damage_dice1 integer,
            base_damage_dice2 integer,
            base_damage_type1 text,
            bonus1_damage_dice1 integer,
            bonus1_damage_dice2 integer,
            bonus1_damage_type1 text,
            bonus2_damage_dice1 integer,
            bonus2_damage_dice2 integer,
            bonus2_damage_type1 text
        )
    """)

    conn.commit()
    conn.close()

def drop_tables():
    conn = sqlite3.connect('BRA.db')
    cur = conn.cursor()

    cur.execute("""
        DROP TABLE Creatures
    """)

    cur.execute("""
            DROP TABLE Attacks
        """)

    conn.commit()
    conn.close()

def add_creature():
    conn = sqlite3.connect('BRA.db')
    cur = conn.cursor()

    #code to add creature #statu variabilis
    name = str(input("Creature Name:"))
    proficiency_bonus = int(input("Proficiency Bonus"))
    strength_mod = int(input("Strength Modifier"))
    dexterity_mod = int(input("Dexterity Modifier"))
    casting_mod = int(input("Casting Modifier"))
    armor_class = int(input("Armor Class"))
    #hitpoints = input()

    creature_list = [name, proficiency_bonus, strength_mod, dexterity_mod, casting_mod, armor_class]

    cur.execute("""INSERT INTO Creatures VALUES(?,?,?,?,?,?)""", creature_list)

    conn.commit()
    conn.close()

def delete_creature():
    conn = sqlite3.connect('BRA.db')
    cur = conn.cursor()
    name = str(input("Name of creature to delete:"))

    find_matching_creature(name)

    id = int(input("ID of creature to delete:"))
    cur.execute("DELETE FROM Creatures WHERE rowid = {}".format(id))

    conn.commit()
    conn.close()

def find_matching_creature(creature_name):
    conn = sqlite3.connect('BRA.db')
    cur = conn.cursor()

    cur.execute("SELECT rowid, * FROM Creatures WHERE name LIKE '%{}%'".format(creature_name))
    results = cur.fetchall()
    print("Matching creatures\nID:\tName:\tStats")
    for result in results:
        print(result)

    conn.commit()
    conn.close()

def copy_creature():
    conn = sqlite3.connect('BRA.db')
    cur = conn.cursor()
    name = str(input("Name of creature to copy:"))

    find_matching_creature(name)

    id = int(input("ID of creature to copy:"))
    cur.execute("SELECT * FROM Creatures WHERE rowid = {}".format(id))
    copy_result = cur.fetchall()

    name = str(input("New Creature Name:"))
    proficiency_bonus = copy_result[0][1]
    strength_mod = copy_result[0][2]
    dexterity_mod = copy_result[0][3]
    casting_mod = copy_result[0][4]
    armor_class = copy_result[0][5]

    creature_list = [name, proficiency_bonus, strength_mod, dexterity_mod, casting_mod, armor_class]

    cur.execute("""INSERT INTO Creatures VALUES(?,?,?,?,?,?)""", creature_list)

    conn.commit()
    conn.close()

def create_enconter():

    #this creates a table, which has rowid, creature name, and weapon name
    conn = sqlite3.connect('BRA.db')
    cur = conn.cursor()

    encounter_name = str(input("What is the name of this encounter? "))
    encounter_name = encounter_name.replace(' ', '_')

    cur.execute("""
        CREATE TABLE {}(
            creature_name text UNIQUE
        )
    """.format(encounter_name))


    conn.commit()
    conn.close()

def populate_encounter():
    #find matching encounter
    #find matching creatures
    #find matching weapons
    #add creature and weapon to encounter
    pass

def fill_creature_table():
    conn = sqlite3.connect('BRA.db')
    cur = conn.cursor()

    #add_creature() #check if the table is empty before doing this
    while True:
        x = str(input("""
            Press A to add a new creature.\n
            Press C to copy an existing creature.\n
            Press D to delete an existing creature. \n
            Press S to show the Creature table. \n
            Press Q to quit.\n
            """))
        if x == 'a' or x == 'A':
            add_creature()
        elif x == 'c' or x == 'C':
            copy_creature()
        elif x == 'd' or x == 'D':
            delete_creature()
        elif x == 's' or x == 'S':
            display_creature_table()
        elif x == 'q' or x == 'Q':
            break
        else:
            print("Invalid response.")
            continue

    conn.commit()
    conn.close()

def display_creature_table():
    conn = sqlite3.connect('BRA.db')
    cur = conn.cursor()

    cur.execute("SELECT rowid, * FROM Creatures")
    results = cur.fetchall()
    for row in results:
        print(row)

    conn.commit()
    conn.close()

#create_tables()
#drop_tables()
