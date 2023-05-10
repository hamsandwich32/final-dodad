
	# Initialize an empty list to store items
inventory = []
# Function to add an item to the inventory
def add_item(item):
	inventory.append(item)
	print(f"{item} has been added to your inventory.")

# Function to remove an item from the inventory
def remove_item(item):
	if item in inventory:
		inventory.remove(item)
		print(f"{item} has been removed from your inventory.")
	else:
		print(f"{item} is not in your inventory.")
#to add / remove item in inventory
#add_item("key")
#remove_item("book")



