import pickle
def save_object(bag, Intro):
    with open(Intro, 'wb') as f:
        pickle.dump(bag, f)
        print(f"Object saved to {Intro}")

def load_object(main):
    with open(main, 'rb') as f:
        bag = pickle.load(f)
        print(f"Object loaded from {main}")
        return obj

my_object = ['potion bag','snail food','broomstick','wand','potion','leash','key','crystal']
filename = 'my_object.pickle'
save_object(my_object, main)
loaded_obj = load_object(main)
print(loaded_obj)






#items = ["potion bag","snail food","broomstick","wand","potion","leash","key","crystal"]
#with open ('save_pkl.py', 'wb') as f:
	#pickle.dump(save_pkl.py, f)
	#f.close()
#with open('save_pkl.py', 'rb') as f:

	#items_name_loaded = pickle.load(f) # deserialize using load()
	#print(items_name_loaded)