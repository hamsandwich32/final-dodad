import sys
from add_remove import add_item
def bee():
		#include classes within the program
		#Include inventory
	print("You forgot to walk your bee around, he might be a bit angry at you this morning.\n")
	print("You look around the wall and your eyes stop at a clock floating throughout the room. You check the time, you're almost forty minutes late.\n")
	print("Your teacher is going to be so mad. You need to get out of here.\n")
	print("You make eye contact with your bee. Yup, he's mad. What do you do now?\n")
	MENU = '''
	1 - try to get past your bee
	2 - try to find the rest of your things '''
	print(MENU)
	attempt_1 = 'a'
	while attempt_1 == 1 or 2:
		attempt_1 = input("\nWhat's your choice?\n")
		if attempt_1 == '1':
			print("Your bee comes and stings you. You are put into a deep sleep and must start again. I'm sorry.\n")
			print("Goodbye.")
			sys.exit()
		elif attempt_1 == '2':
			MENU = '''
			1 - go towards the weird bubbling noise
			2 - go back to the angry bee'''
			print("You walk around your room trying to avoid your angry bee. Geez you need to take him on a walk soon.\n")
			print("As you awkwardly shuffle along the wall you feel yourself fall backwards. You find yourself in a a room you've never seen before.\n")
			print("As you lay on the ground you hear a bubbiling coming from behind you. You get up to investigate.\n")
			print(MENU)
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
					print("You continue to look around the room and realize it goes back further. What do you want to do?\n")
