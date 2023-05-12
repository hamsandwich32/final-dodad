import pickle
SAVE_FILE = "saved_game.dat"


def save_game(player_data):
	with open(SAVE_FILE, "wb") as file:
		pickle.dump(player_data, file)
	print("Game saved successfully.")


def load_game():
	try:
		with open(SAVE_FILE, "rb") as file:
			player_data = pickle.load(file)
		print("Game loaded successfully.")
		return player_data
	except FileNotFoundError:
		print("Save file not found.")
		return None


loaded_data = load_game()
if loaded_data is not None:
	player_data = loaded_data
	print("Welcome back to the game!")
else:
	print("Starting new game...")