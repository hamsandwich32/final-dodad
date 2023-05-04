def intro_part():
	print("You wake up to your alarm blaring, you realize that it's been going off for the last five minutes.\n")
	print("You hit the alarm expecting it to turn off. It yells at you to get up.\n")
	print("You get up and start to look around. You feel disoriented. You're in your bedroom, you look at the clock closer, you're 15 minutes late to your magic training class!\n")
	print("You start to frantically run around your room and look for your things. You can't find your potion bag, your wand, or the food to feed your snail.\n")
	print("You look around once more and see your potion bag on your table, you grab it.\n")
	print("You're still missing a lot of your stuff, where do you look?\n")
	print("\t1 - check under your bed")
	print("\t2 - check the top of the table")
	while True:
		bn = input()
		if int(bn) == 1:
			print("Under the bed, you see something. You can't grab it.\n")
			print("You check your table as well and find your broomstick. You realize that you can use it to grab what's underneath your bed.")
			break
		elif int(bn) == 2:
			print("You check your table as well and find your broomstick. You realize that you can use it to grab what's underneath your bed.\n")
			#add in as item save to inventory
			print("You check back under your bed and use your broomstick to grab the thing under your bag. You pull it out and realize its the bag of snail food!")
			break 
		else:
			print("Pick an option to chose from.")
		#except:
			#print("Value must be a whole number between 1 and 2.")
	print("")
	print("You realize that you need to feed your snail before you leave, you have to find him first. Maybe he's in the crystal room?\n")
	print("You look around your room and head towards your door.\n")


