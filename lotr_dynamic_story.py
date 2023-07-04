from random import choice

name = input("What is the adventureer's name?...")
age = input("How old are you?")

if int(age) > 1000:
    description = " an elder "
else:
    description = " a younger one "

# Game Intro
print("Welcome to Middle Earth," + name)
print("")
print(f"So you are {description} , {name}")
print("")

# Items
things = ["goblins", "mines", "chocolate", "rocks", "trees", "pipe"]
friends = ["Bilbo", "Gandalf", "Aragorn", "Galadriel", "Gimli", "Haldir", "Arwen", "Thranduil ", "Legolas", "celeborn", "Glorfindel", "Elrond"]
actions = ["slay", "kiss", "save", "marry", "rescue", "eat", "study", "talk with"]
places = ["Old Forrest", "Lothlórien", "Fangorn", "Beleriand", "Valinor"]

# Story
thing = choice(things)
friend = choice(friends)
action = choice(actions)
place = choice(places)

story = "Once upon a time, there was an Elf called " + name + ". The Elf was " + description + " in Middle Earth." + " It liked nothing better than to " +  action + " " + thing + ". Sadly, the Elf was so great at this that it ran out of " + thing + " to " + action + " in " + place + ". The Elf became very bored. Luckily the Elf had a friend called " + friend + ". " + friend + " knew where the Elf could find lots of " + thing + " and the two of them travelled far away from " + place + " and found a land filled with lots of lovely " + thing + " to " + action + ". " + name + " and " + friend + " lived happily ever, with all the " + thing + " they wanted."
print(story)