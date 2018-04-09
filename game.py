from hero import Hero
from dungeon import Dungeon


done = False

#objects
hero = Hero("null")
dungeon = Dungeon()

#functions
def intro():
    print("Welcome to Dungeon Adventure")
    print()
    print("What is your name")
    name = input()
    hero.name = name

#introduction
intro()

#dungeon
dungeon.room_one()


    
