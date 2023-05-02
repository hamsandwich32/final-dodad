def intro_part():
	print("You wake up to your alarm blaring, you realize that it's been going off for the last five minutes.\n")
	print("You hit the alarm expecting it to turn off. It yells at you to get up.\n")
	print("You get up and start to look around. You feel disoriented. You're in your bedroom, you look at the clock closer, you're 15 minutes late to your magic training class!\n")
	print("You start to frantically run around your room and look for your things. You can't find your potion bag, your wand, or the food to feed your snail.\n")
	print("You look around once more and see your bag on your nightstand, you grab it.\n")
	print("You're still missing a lot of your stuff, where do you look?\n")
	print("1 - check under your bed")
	print("2 - check in the drawers of the nightstand")
	while True:
		bn = input()
		try:
			if int(bn) == 1:
				print("You look under the bed, you feel something pointy. You reach for it and pull it from under the bed. It's a unicorn horn. What does this do?")
			elif int(bn) == 2:
				print("You open the top drawer of your nightstand you find a brown leather bag of salt. What could this possibly be used for?")
				break 
			else:
				print("Pick an option to chose from.")
		except:
			print("Value must be a whole number between 1 and 2.")

	print("You're still missing most of your things. You need to check elsewhere!")

