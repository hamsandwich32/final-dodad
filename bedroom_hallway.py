from add_remove import add_item, inventory, remove_item
from save_pkl import save_game
def hallway1():
	import sys
	print("You reach towards the door leading out of your bedroom, you grab the doorknob and twist it.")
	print("You open the door and look out into the narrow hallway.")
	print("The hallway is dimly lit from the floating candles that span the entire hallway.")
	print("You see a door and realize that's the entrance to your potion room, you remember that you left a potion you need by the culdron.")
	print("You make your way down the hallway. The hallway seems to twist and turn as you start to go down it.")
	print("Doors start to appear around you, which one are you supposed to go down?\n")

	MENU = '''
	1 - open the door next to you
	2 - keep walking down the hall until the end'''
	attempt_1 = 'a'
	while attempt_1 == 1 or 2:
		print(MENU)
		attempt_1 = input("What's your choice?\n")
		if attempt_1 == '1':
			print("You reach for the door ahead of you, your arm goes through the door. It's not this one.\n")
			print("Try again.")
		if attempt_1 == '2':
			print("The hallway keeps spinning around you, you finally reach the door and try to open it. It's locked.\n")
			print("You walk around the hallway trying to find the key. You realize you probably shouldn't have a distorting hallway anymore.\n")
			print("As you look around for the key in the middle of the hallway, you see that the hallway diverges to the right and the left.\n")
			break
	MENU = '''
	1 - go to the hallway to the right
	2 - go to the hallway to the left
	3 - stay in the distorting hallway
	4 - sit and cry
	5 - go back to bedroom'''
	print(MENU)
	attempt_2 = 'a'
	while attempt_2 == 1 or 2 or 3:
		attempt_2 = input("\nWhat's your choice?\n")
		if attempt_2 == '1':
			print("The hallway's a dead end.\n")
			print("Try again.")
			print(MENU)
		elif attempt_2 == '2':
			print("The hallway turns pitch black. You pull out your potion bag and use an enlightener potion to illuminate the hallway. At the end of the hallway sits a table. You walk over, the key is sitting ontop of the table.\n")
			add_item('key')
			break
		elif attempt_2 == '3':
			print("The hallway spins and makes you discombobulated. This probably isn't it.\n")
			print("Try again.")
			print(MENU)
		elif attempt_2 == '4':
			print("You're doing great. Just keep trying. You're already so late.")
			print("Try again.")
			print(MENU)
		elif attempt_2 == '5':
			print("You walk back to your room. You feel defeated and like you want to plop on your bed and just quit magic training.\n")
			print("What do you do now?\n")
			MENU = '''
			1 - quit magic training
			2 - go back to hallway'''
			print(MENU)
			attempt_0 = 'a'
			while attempt_0 != '1':
				attempt_0 = input("\nWhat's your choice?\n")
				if attempt_0 == '2':
					MENU = '''
					1 - go to the hallway to the right
					2 - go to the hallway to the left
					3 - stay in the distorting hallway
					4 - sit and cry
					5 - go back to bedroom'''
					print("Good job sticking with it. You walk back to the bedroom door and open it. You walk down the hallway and are met with a door. It's locked.")
					print("Try again.")
					print(MENU)
					break
				if attempt_0 == '1':
					print("Goodbye.")
					sys.exit()

		else:
			print("Try again.")
	print("You need to head back to the locked door. Which direction do you go?\n")
	MENU = '''
	1 - go right
	2 - go left'''
	print(MENU)
	attempt_3 = 'a'
	while attempt_3 == 1 or 2:
		attempt_3 = input("What's your choice?\n")
		if attempt_3 == '1':
			print("You made it back to the middle of the hallway, you start walking towards the door and unlock the door.\n")
			print(f"Items collected:{inventory}\n")
			remove_item("key")
			break
		elif attempt_3 == '2':
			print("You made the wrong decision. Shame on you.\n")
			print("Try again.")
			print(MENU)
		else:
			print("Try again.")
player_data = {"level": 2, "inventory": ["bag", "snail food",]}
save_game(player_data)

