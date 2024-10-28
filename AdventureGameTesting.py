print(""" 
Controls:

[w] Goes north.
[a] Goes west.
[s] Goes south.
[d] Goes east.
[q] Drop the item.
[e] Pick up the item.
[r] Swap the item in your hand with the one in the current room.
[u] Use the item in my inventory.
[f] Check my inventory.
[z] Look around.
[c] Show controls.

***Type "quit" to quit the game.***
""")

Desc = list(range(81))
Objects = list(range(81))
North = list(range(81))
South = list(range(81))
East = list(range(81))
West = list(range(81))

#room data
Desc[1] = "Starting Room"
Objects[1] = ["a starter pack"] 
North[1] = 0
South[1] = 2
East[1] = 0
West[1] = 0

Desc[2] = "Main Hall Section 1"
Objects[2] = ["a starting room teleporter"]
North[2] = 1
South[2] = 3
East[2] = 11
West[2] = 9

Desc[3] = "Main Hall Section 2"
Objects[3] = ["nothing"]
North[3] = 2
South[3] = 4
East[3] = 0
West[3] = 0

Desc[4] = "Fountain"
Objects[4] = ["nothing"]
North[4] = 3
South[4] = 5
East[4] = 0
West[4] = 0

Desc[5] = "Main Hall Section 3"
Objects[5] = ["nothing"]
North[5] = 4
South[5] = 6
East[5] = 0
West[5] = 0

Desc[6] = "Main Hall Section 4"
Objects[6] = ["nothing"]
North[6] = 5
South[6] = 7
East[6] = 0
West[6] = 0

Desc[7] = "Main Hall Section 5"
Objects[7] = ["nothing"]
North[7] = 6
South[7] = 8
East[7] = 0
West[7] = 0

Desc[8] = "End Of The Main Hall"
Objects[8] = ["nothing"]
North[8] = 7
South[8] = 0
East[8] = 0
West[8] = 0

Desc[9] = "Bedroom 1"
Objects[9] = ["a pillow"]
North[9] = 0
South[9] = 10
East[9] = 2
West[9] = 0

Desc[10] = "Bathroom Of Bedroom 1"
Objects[10] = ["nothing"]
North[10] = 9
South[10] = 0  #wall between main hall & bathroom
East[10] = 0
West[10] = 0

Desc[11] = "Bedroom 2"
Objects[11] = ["a pillow"]
North[11] = 0
South[11] = 12
East[11] = 0
West[11] = 2

Desc[12] = "Bathroom Of Bedroom 2"
Objects[12] = ["nothing"]
North[12] = 11
South[12] = 0  #wall between main hall & bathroom
East[12] = 0
West[12] = 0


#game mechanics
current_room = 1
inventory = []  
interacted_with_armor = False
grabbed_sword = False
first_time_toilet = False
first_time_starting_room = False
death = False

#items----------
def use_item(item):
    if item == "a starter pack":
            print("You opened the starter pack and see another smaller pack inside of it.")
            inventory.append("a smaller starter pack")
            inventory.remove("a starter pack")
    elif item == "a smaller starter pack":
            print("You opened the smaller starter pack and see another even smaller pack inside of it.")
            inventory.append("an even smaller starter pack")
            inventory.remove("a smaller starter pack")
    elif item == "an even smaller starter pack":
            print("You opened the even smaller starter pack and see another even much smaller pack inside of it.")
            inventory.append("an even much smaller starter pack")
            inventory.remove("an even smaller starter pack")
    elif item == "an even much smaller starter pack":
            print("You opened the even much smaller starter pack and see another even much much smaller pack inside of it... just kidding, you see a teleporter to the starting room, will a red button on it.")
            inventory.append("a starting room teleporter")
            inventory.remove("an even much smaller starter pack")
    elif item ==  "a starting room teleporter":
        global current_room
        current_room = 1
        print("You press on the red button on the teleporter, you are suddenly back to the starting room again.")
        
    elif item == "a stone":
        print("You throw the stone. It makes a satisfying thud as it hits the wall.")
    elif item == "a pillow":
        print("You hug the pillow tightly. It feels soft and comforting.")
    else:
        print("You can't use that item.")
#---------------

#starting-------
while True:
    print(f"\nYou are in: {Desc[current_room]}")
    print(f"You see {', '.join(Objects[current_room])} at the first look." if Objects[current_room] else "There's nothing here.")
    #print(current_room)
    
    command = input("What do you want to do? ").lower()

    if command == 'w':
        next_room = North[current_room]
        if next_room != 0:
            current_room = next_room
        else:
            print("You can't go that way!")
    elif command == 's':
        next_room = South[current_room]
        if next_room != 0:
            current_room = next_room
        else:
            print("You can't go that way!")
    elif command == 'a':
        next_room = West[current_room]
        if next_room != 0:
            current_room = next_room
        else:
            print("You can't go that way!")
    elif command == 'd':
        next_room = East[current_room]
        if next_room != 0:
            current_room = next_room
        else:
            print("You can't go that way!")

    #pick up-----
    elif command == 'e':
        if Objects[current_room]:
            #prevent picking up "nothing"
            Objects[current_room] = [item for item in Objects[current_room] if item != "nothing"]
            if len(Objects[current_room]) == 1:
            #if only 1 item in room, directly pick it up
                item_to_pick = Objects[current_room][0]
                if len(inventory) < 2:
                    inventory.append(item_to_pick)
                    Objects[current_room].remove(item_to_pick)
                    print(f"You picked up {item_to_pick}.")
                else:
                    print("You can only carry 2 items at a time.")
            elif len(Objects[current_room]) > 1:
                print("Which item do you want to pick up? Options:", ', '.join(Objects[current_room]))
                item_to_pick = input("Enter item name: ").strip()
                if item_to_pick in Objects[current_room]:
                    if len(inventory) < 2:
                        inventory.append(item_to_pick)
                        Objects[current_room].remove(item_to_pick)
                        print(f"You picked up {item_to_pick}.")
                    else:
                        print("You can only carry 2 items at a time.")
                else:
                    print("You can't pick that up.")
        else:
            print("There's nothing to pick up here.")
    #drop-----
    elif command == 'q':
        if inventory:
            if len(inventory) == 1:
            #if only 1 item in inventory, directly pick it up
                item_to_drop = inventory[0]
                inventory.remove(item_to_drop)
                Objects[current_room].append(item_to_drop)
                print(f"You dropped {item_to_drop}.")
            elif len(inventory) > 1:
                print("Which item do you want to drop? Options:", ', '.join(inventory))
                item_to_drop = input("Enter item name: ").strip()
                if item_to_drop in inventory:
                    inventory.remove(item_to_drop)
                    Objects[current_room].append(item_to_drop)
                    print(f"You dropped {item_to_drop}.")
                else:
                    print("You don't have that item.")
        else:
            print("Your inventory is empty.")
    #check inventory-----
    elif command == 'f':
        print("Your inventory:", inventory)
    #swap-----
    elif command == 'r':
        if inventory:
            #prevent swapping nothing
            Objects[current_room] = [item for item in Objects[current_room] if item != "nothing"]

            if Objects[current_room]:
                #if >1 items in the room
                if len(Objects[current_room]) > 1:
                    print("Which item do you want to swap from the room? Options:", ', '.join(Objects[current_room]))
                    item_in_room = input("Enter the name of the item in the room: ").strip()
                    if item_in_room not in Objects[current_room]:
                        print("That item is not in the room.")
                        continue
                else:
                    item_in_room = Objects[current_room][0]  #one item in room

                #if >1 items in the inventory
                if len(inventory) > 1:
                    print("Which item do you want to swap from your inventory? Options:", ', '.join(inventory))
                    item_to_swap = input("Enter the name of the item in your inventory: ").strip()
                    if item_to_swap not in inventory:
                        print("That item is not in your inventory.")
                        continue
                else:
                    item_to_swap = inventory[0]  #one item in inventory

                
                Objects[current_room][Objects[current_room].index(item_in_room)] = item_to_swap
                inventory[inventory.index(item_to_swap)] = item_in_room
                print(f"You swapped {item_to_swap} with {item_in_room}.")
            else:
                print("There's nothing in the room to swap with.")
        else:
            print("You don't have anything to swap.")

    
    #look around-----
    elif command == 'z':
            
        if current_room == 10 and first_time_toilet == False:
            print("As you look around, your eyes are drawn to the mesmerizing sight of the glowing pure gold toilet. It sparkles under the soft ambient light, casting a warm, ethereal glow that feels almost otherworldly. The lavishness of its design evokes a sense of whimsy and indulgence, transforming an ordinary moment into a fantastical dream. In that moment, its not just a toilet; its a gilded throne, inviting you to revel in a touch of luxurious surrealism. But sadly, you don't feel like to excrete right now. You unwillingly declined the kindness of the pure gold toilet. ")
            first_time_toilet = True
        elif current_room == 10 and first_time_toilet == True:
            print("You see the toilet again, it still looks as gorgeous as it was. You hope one day that you will be the person sitting on it.")
        elif current_room == 1 and first_time_starting_room == False:
            print("You are in the starting room, you see a huge sign in front of you telling you it's the starting room.")
            first_time_starting_room = True
        elif current_room == 1 and first_time_starting_room == True:
            print("You somehow come back to the starting room again and decided to look around, you see the huge sign telling that you're in the starting room just like the first time you did.")
            
        elif current_room == 8 and interacted_with_armor == False and len(inventory) >= 2 and grabbed_sword == False:
            print("You see an armor standing in front of you but nothing too special, maybe you should comeback later..??(Tips: Leave atleast 1 blank in your invenmtroy.)")
        elif current_room == 8 and interacted_with_armor == False and grabbed_sword == False:
            print("You look around and see an iron armor standing nearby. Striking a pose while it seems to be holding something, coincidentally you see a sword laying on the floor nearby.")
            armorsword = input("Do you want to put the sword back? (y/n) ")
            if armorsword == "y":
                print("You decide to put the sword back. The armor bows to you and send you the sword as a gift, grateful for your kindness.")
                inventory.append("a sword")  
                interacted_with_armor = True  
            
            elif armorsword == "n":
                print("You chose to grab the sword because it looks cool.")
                inventory.append("a sword")
                grabbed_sword = True

            else:
                print("""Please only inter "y" or "n".""")

        elif current_room == 8 and interacted_with_armor == True:
            print("The armor noticed you are here again, waving it's hand friendly.")
        elif current_room == 8 and interacted_with_armor == False and grabbed_sword == True:
            print("You look around and see an iron armor standing nearby. Striking a pose while it seems to be holding something.")
            armorsword = input("Do you want to put the sword back? (y/n) ")
            if armorsword == "y":
                print("You decide to put the sword back. The armor bows to you and send you the sword, grateful for your kindness.")  
                interacted_with_armor = True  
            
            elif armorsword == "n":
                print("You chose to keep the sword because it looks cool.")
            else:
                print("""Please only inter "y" or "n".""")

        elif current_room == 4:
            print("You see a huge fountain in the middle of the room, you expect there will be some coins in the fountain so you can pick them up, but sadly there isn't any.")

        else:
            print("You look around but see nothing of interest.")
            pass
    #use item-----
    elif command == 'u':
        if inventory:
            print("Which item do you want to use? Options:", ', '.join(inventory))
            item_to_use = input("Enter item name: ").strip()
            if item_to_use in inventory:
                use_item(item_to_use)
            else:
                print("You don't have that item.")
        else:
            print("Your inventory is empty.")

    #check controls
    elif command == 'c':
        print("""Controls:

[w] Goes north.
[a] Goes west.
[s] Goes south.
[d] Goes east.
[q] Drop the item.
[e] Pick up the item.
[r] Swap the item in your hand with the one in the current room.
[u] Use the item in my inventory.
[f] Check my inventory.
[z] Look around.
[c] Show controls.

***Type "quit" to quit the game.***
""")
    #quit-----
    elif command == 'quit':
        print("Thanks for playing~!!")
        break
    else:
        print("Unknown command.")
