def hallway1():
	print("You reach towards the door leading out of your bedroom, you grab the doorknob and twist it.")
	print("You open the door and look out into the narrow hallway.")
	print("The hallway is dimly lit from the floating candles that span the entire hallway.")
	print("You see a door and realize that's the etrance to your potion room, you remember that you left a potion you need by the culdron.")
	print("You make your way down the hallway. The hallway seems to twist and turn as you start to go down it.")
	print("Doors start to appear around you, which one are you supposed to go down?\n")
	print("1 - open the door next to you")
	print("2 - keep walking down the hall until the end")
	attempt_1 = input()
	while attempt_1 == 1 or 2:
		try:
			
			if int(attempt_1) == 1:
				print("You reach for the door ahead of you, your arm goes through the door. It's not this one.")
				print("Try again.")
				break
			if int(attempt_1) == 2:
				print("The hallway keeps spinning around you, you finally reach the door and try to open it. It's locked.")
		except:
			print("Try again.")
	


