
from add_remove import add_item, inventory, remove_item
from save_pkl import save_game
def potion_weirdness():
	print("After unlocking the door you walk into the potion room.\n")
	print("Now you need to find that potion you were missing.\n")
	print("You have no idea where to start, potions line the entire room with only a narrow passage through them. Ugh. You are so gonna get in trouble with your teacher.\n")
	MENU1 = '''
	1 - go forward
	2 - go back'''
	attempt_1 = '1'
	while attempt_1 == 1 or 2:
		print(MENU1)
		attempt_1 = input("\nWhat's your choice?\n")
		if attempt_1 == '2':
			print("You are back at the funky hallway from alice and wonderland. Don't go back.")
		elif attempt_1 == '1':
			MENU2 = '''
	1 - go right
	2 - go left
	3 - go straight'''
			print("You walk forward and the path diverges into. Where do you three paths where do you go from here?\n")
			print(MENU2)
			break
			
	sacrifice = False
	attempt_2 = 'a'
	while attempt_2 == 1 or 2 or 3 or sacrifice:
		attempt_2 = input("\nWhat's your choice?\n")
		if attempt_2 == '1' and sacrifice:
			print("You're greeted with a profoundly large door. Why do you have this? You try the knob and it licks you. It's hungry. You use your sacrifice to feed it and it opens.\n")
			print("You look around and see your snail sitting in the corner. He looks hungry. You remember the snail food in your bag. You feed your snail, now you have to leave. Seriously. You're so late.\n")
			remove_item('sacrifice')
			print(MENU2)
		elif attempt_2 == '1':
			print("Find a sacrifice.")
			print(MENU2)
		elif attempt_2 == '2':
			MENU3 = '''
	1 - go right
	2 - go to potion hallway'''
			print("You've been fooled once again by your own home. You really need to stop making things hard on yourself.\n")
			print(MENU3)
			
			attempt_3 = 'a'
			while attempt_3 == 1 or 2 :
				attempt_3 = input("\nWhat's your choice?\n")
				if attempt_3 == '1':
					MENU4 = '''
	2 - go back to potion room hallway'''
					
					print("You walk to the end of the hallway. You find a large bookcase. You start to look around and you find a small sacrifice for the doorknob.\n")
					print(MENU4)
					sacrifice = True
					add_item('sacrifice')
					vn = input()

					if vn == '2':
						print(MENU2)
						break
					else:
						vn = input()
					

				elif attempt_3 == '2':
					print("You walk forward and the path diverges into. Where do you three paths where do you go from here?\n")
					MENU5 = '''
	1 - go right
	2 - go left
	3 - go straight'''
					print(MENU5)
					
		elif attempt_2 == '3':
			print("You walk down the hallway. Pictures of the witches who have owned the house before you hang. Why can't you be like them? Why must you be late to all of your training classes\n")
			print("You slowly walk past all of the portraits, you just want to make them proud.\n")
			print("You reach the door end of the hallway, you reach out and twist the handle. It opens for you, you walk through and are greeted with your giant bee.\n")
			print(f"Items collected:{inventory}\n")
		
			break
player_data = {"level": 3, "inventory": ["bag"]}
save_game(player_data)
