from add_remove import add_item, inventory, remove_item
from save_pkl import save_game, load_game
def intro_part():
	print("Do you have a saved game?\n")
	MENU0= '''
	1 - yes
	2 - no'''
	print(MENU0)
	attempt = input()
	if attempt == 1:
		print(load_game)
	if attempt == 2:
		print("You wake up to your alarm blaring, you realize that it's been going off for the last five minutes.\n")
		print("You hit the alarm expecting it to turn off. It yells at you to get up.\n")
		print("You get up and start to look around. You feel disoriented. You're in your bedroom, you look at the clock closer, you're 15 minutes late to your magic training class!\n")
		print("You start to frantically run around your room and look for your things. You can't find your potion bag, your wand, or the food to feed your snail.\n")
		print("You look around once more and see your potion bag on your table, you grab it.\n")
		add_item('potion bag')

		print("You're still missing a lot of your stuff, where do you look?\n")
		MENU='''
	1 - check under your bed
	2 - check the top of the table'''
		attempt_1 = 'a'
		print(MENU)
		while attempt_1 == 1 or 2:
			attempt_1 = input("What's your choice?\n")
			if attempt_1 == '1':
				print("Under the bed, you see something. You can't grab it.\n")
				print("You check your table as well and find your broomstick. You realize that you can use it to grab what's underneath your bed.")
				add_item('broomstick')
				print(MENU)
			elif attempt_1 == '2':
				print("You check back under your bed and use your broomstick to grab the thing under your bed. You pull it out and realize its the bag of snail food!")
				remove_item('broomstick')
				add_item('snail food')
				break 
			else:
				print("Pick an option to chose from.")
		print("")
		print("You realize that you need to feed your snail before you leave, you have to find him first. Maybe he's in the crystal room?\n")
		print("You look around your room and head towards your door.\n")
		print(f"Items collected:{inventory}\n")
		player_data = {"level": 1, "inventory": ["snail food", "bag",]}
		save_game(player_data)

