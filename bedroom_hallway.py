def hallway1():
	print("You reach towards the door leading out of your bedroom, you grab the doorknob and twist it.")
	print("You open the door and look out into the narrow hallway.")
	print("The hallway is dimly lit from the floating candles that span the entire hallway.")
	print("You see a door and realize that's the etrance to your potion room, you remember that you left a potion you need by the culdron.")
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
		elif attempt_1 == '2':
			MENU = '''
	1 - go to the hallway to the right
	2 - go to the hallway to the left
	3 - stay in the distorting hallway'''
			print("The hallway keeps spinning around you, you finally reach the door and try to open it. It's locked.\n")
			print("You walk around the hallway trying to find the key. You realize you probably shouldn't have a distorting hallway anymore.\n")
			print("As you look around for the key, you see that the hallway diverges to the right and the left.\n")
			while attempt_1 == 1 or 2 or 3:
				if attempt_1 == '1':
					print("The hallway's a dead end.") 
				if attempt_1 == '2':
					print("The hallway turns pitch black. You pull out your potion bag and use an enlightener potion to illuminate the hallway. At the end of the hallway sits a table. You walk over, the key is sitting ontop of the table.")
				if attempt_1 == '3':
					print("The hallway spins and makes you discombobulated. This probably isn't it.")
					
					print("")
		else:
			print("Try again.")
			#False
		


	#attempt_2 = input()
	#while attempt_2 == 1 or 2 or 3

	


