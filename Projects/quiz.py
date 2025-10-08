roblox_points = 0
minecraft_points = 0
block = input("blocks or studs ")
if block == "blocks":
    minecraft_points += 1
elif block == "studs":
    roblox_points += 1
print (f"roblox = {roblox_points}")
print (f"minecraft{ minecraft_points}")
animal = input("cats or dogs")
if animal == "dogs" or animal == "puppy":
    minecraft_points += 1
elif animal == "cats":
    roblox_points += 1
print (f"roblox = {roblox_points}")
print (f"minecraft{ minecraft_points}")
mental = input("do you like to create or to explore ")
if mental == "explore":
    roblox_points += 1
elif mental == "create":
    minecraft_points += 1
print (f"roblox = {roblox_points}")
print (f"minecraft{ minecraft_points}")
animal = input("crafting or taking")
if animal == "crafting":
    minecraft_points += 1
elif animal == "taking":
    roblox_points += 1
print (f"roblox = {roblox_points}")
print (f"minecraft{ minecraft_points}")
animal = input("r or m ")
if animal == "m":
    minecraft_points += 1
elif animal == "r ":
    roblox_points += 1
print (f"roblox = {roblox_points}")
print (f"minecraft{ minecraft_points}")
if roblox_points > minecraft_points:
    print ("you like roblox better.")
elif roblox_points < minecraft_points:
    print ("you like minecraft better")
elif roblox_points and 1 == 2 print("wow")