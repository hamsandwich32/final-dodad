def add_rem_bag():
	# Initialize an empty list to store items
inventory = []

# Function to add an item to the inventory
def add_item(bag):
	inventory.append(bag)
	print(f"{bag} has been added to your inventory.")

# Function to remove an item from the inventory
def remove_item(bag):
	if bag in inventory:
		inventory.remove(bag)
		print(f"{bag} has been removed from your inventory.")
	else:
		print(f"{bag} is not in your inventory.")
#to add / remove item in inventory
add_item("key")
remove_item("book")



