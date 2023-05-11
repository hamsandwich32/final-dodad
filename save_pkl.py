import pickle
SAVE_FILE = "saved_game.dat"

# Function to save the game data
def save_game(player_data):
	with open(SAVE_FILE, "wb") as file:
		pickle.dump(player_data, file)
	print("Game saved successfully.")

# Function to load the game data
def load_game():
	try:
		with open(SAVE_FILE, "rb") as file:
			player_data = pickle.load(file)
		print("Game loaded successfully.")
		return player_data
	except FileNotFoundError:
		print("Save file not found.")
		return None






#items = ["potion bag","snail food","broomstick","wand","potion","leash","key","crystal"]
#with open ('save_pkl.py', 'wb') as f:
	#pickle.dump(save_pkl.py, f)
	#f.close()
#with open('save_pkl.py', 'rb') as f:

	#items_name_loaded = pickle.load(f) # deserialize using load()
	#print(items_name_loaded)