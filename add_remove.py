

inventory = []
def add_item(item):
	inventory.append(item)
	print(f"{item} has been added to your inventory.")


def remove_item(item):
	if item in inventory:
		inventory.remove(item)
		print(f"{item} has been removed from your inventory.")
	else:
		print(f"{item} is not in your inventory.")




