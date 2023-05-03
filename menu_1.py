#use 19p for a menu and a good way of displaying it aesthetically 
# 19p menu options with print aspects
while choice != '0':
		print(MENU)
		choice = input("What's your choice?\n")
		if choice == '1':
			print(table(atts))
		elif choice == '2':
			atts = roll_pool(atts)
			print("Attribute pool has been rolled.")
		elif choice == '3':
			attr = input("Assign a value to which attribute?\n").title()
			amt = int(input("Which value do you wish to assign?\n"))
			print(add(attr, amt, atts))
		elif choice == '4':
			attr = input("Remove value from which attribute?\n").title()
			print(remove(attr, atts))
		elif choice == '5':
			atts = reset()
			print("All attributes have been reset.")
		elif choice == '0':
			print("Goodbye.")
		else:
			print(f"'{choice}' is not a valid menu option.")