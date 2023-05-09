def potion_weirdness():
	print("After unlocking the door you walk into the potion room.")
	print("Now you need to find that potion you were missing.")
	print("You have no idea where to start, potions line the entire room with only a narrow passage through them. Ugh. You are so gonna get in trouble with your teacher.")
	MENU = '''
	1 - go forward
	2 - go back'''
	attempt_1 = 'a'
	while attempt_1 == 1 or 2:
		print(MENU)
		attempt_1 = input("\nWhat's your choice?\n")
		if attempt_1 == '1':
			print("You walk forward and the path diverges into. Where do you three paths where do you go from here?\n")
			MENU = '''
			1 - go right
			2 - go left
			3 - go straight'''
			print(MENU)

			attempt_2 = 'a'
			while attempt_2 == 1 or 2:
				attempt_2 = input("\nWhat's your choice?\n")
				if attempt_2 == '1':
					print("You're greeted with a profoundly large door. Why do you have this? You try the knob and it licks you. You need to find a sacrifice to feed it.\n")
					print(MENU)
                    #MIGHT NEED BREAK STATEMENT
                elif attempt_2 == '2':
				#menu not right 2 should be go back not left, or seperate option
					MENU = '''
					1 - go right
					2 - go left'''
					print("You walk to the end of the hallway and it diverges to the left and the right.\n")
					print("You've been fooled once again by your own home. You really need to stop making things hard on yourself.\n")
					print(MENU)
				#between dots not working
					attempt_3 = 'a'
					while attempt_3 == 1 or 2 :
						attempt_3 = input("\nWhat's your choice?\n")
						if attempt_3 == '1':
							MENU = '''
							1 - go left
							2 - go back to potion room hallway'''
					#add in as item save to inventory
							print("You walk to the end of the hallway. You find a large bookcase. You start to look around and you find a small sacrifice for the doorknob.\n")
							print(MENU)
							break
						    if attempt_3 == '1':
				                MENU = '''
							    1 - go right
							    2 - go back to potion room hallway'''
                                print("You walk to the end of the hallway. You find the potion sitting on toadstool by the culdron, it smells weird. What is this again?\n")
                                print(MENU)
					            break
                        if attempt_3 == '2':
                            #GO BACK TO ATTEMPT 1
        if attempt_1 == '2':
            print("You go back.")
            print("Try again.")
            print(MENU)

							
					#add in as item save to inventory
									