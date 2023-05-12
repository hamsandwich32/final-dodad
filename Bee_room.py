import sys
from add_remove import add_item, inventory, remove_item
from save_pkl import save_game
def bee():
		
	print(f"Items collected:{inventory}\n")
	print("You forgot to walk your bee around, he might be a bit angry at you this morning.\n")
	print("You look around the wall and your eyes stop at a clock floating throughout the room. You check the time, you're almost forty minutes late.\n")
	print("Your teacher is going to be so mad. You need to get out of here.\n")
	print("You make eye contact with your bee. Yup, he's mad. What do you do now?\n")
	MENU1 = '''
	1 - try to get past your bee
	2 - try to find the rest of your things '''
	print(MENU1)
	attempt_1 = 'a'
	while attempt_1 == 1 or 2:
		attempt_1 = input("\nWhat's your choice?\n")
		if attempt_1 == '1':
			print("Your bee comes and stings you. You are put into a deep sleep and must start again. I'm sorry.\n")
			print("Goodbye.")
			sys.exit()
		elif attempt_1 == '2':
			MENU2 = '''
			1 - go towards the weird bubbling noise
			2 - go back to the angry bee'''
			print("You walk around your room trying to avoid your angry bee. Geez you need to take him on a walk soon.\n")
			print("As you awkwardly shuffle along the wall you feel yourself fall backwards. You find yourself in a a room you've never seen before.\n")
			print("As you lay on the ground you hear a bubbiling coming from behind you. You get up to investigate.\n")
			print(MENU2)
			attempt_2 = 'a'
			while attempt_2 == 1 or 2:
				attempt_2 = input("\nWhat's your choice?\n")
				if attempt_2 == '2':
					print("You turn around and you and your bee come face to face. You stare into it's cold black eyes. It stings you. You are put into a deep sleep and must start again. I'm sorry.\n")
					print("Goodbye.")
					sys.exit()
				elif attempt_2 == '1':
					print("You walk towards the weird bubbiling noise and realize it's your culdron. You walk around it and on a toadstool you find the poition. You swear you've never been in this room before.\n")
					print("You pick up the potion.\n")
					add_item("potion")
					print("You continue to look around the room and realize it goes back further. Your curiosity gets the best of you.\n")
					print("As you go further back to the room, you see shelves lined with spell books. You walk closer to investigate. As you walk along the books you find a leash.\n")
					print("It's the leash to your bee! Now you can take him on a walk!\n")
					add_item("leash")
					print("You walk back towards where you fell into the room from, you need to get your bee on the leash. What do you do?")
					MENU3 = '''
					1 - run towards him and put the leash on
					2 - lasso him like a bull'''
					print(MENU3)
					attempt_3 = 'a'
					while attempt_3 == 1 or 2:
						attempt_3 = input("\nWhat's your choice?\n")
						if attempt_3 == '1':
							print("He got scared and stung you.\n")
							print("Try again.")
							print(MENU3)
						elif attempt_3 == '2':
							print("You lasso him like a bull and he's very happy. He knows it's time for a walk.\n")
							print("You look around and walk towards the door to leave.\n")
							print("You open the door and you take your bee outside. You see your teacher angerly waiting outside.\n")
							print("You give the potion to your teacher and she smiles.\n")
							remove_item("potion")
							print("You completed the day. Good job!")
							break
					break
			break
	