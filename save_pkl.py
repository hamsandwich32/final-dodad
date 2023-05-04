import pickle
items = ["potion bag","snail food","broomstick","wand","potion","leash","key","crystal"]
with open ('save_pkl.py', 'wb') as f:
	pickle.dump(save_pkl.py, f)
	f.close()
with open('save_pkl.py', 'rb') as f:

	items_name_loaded = pickle.load(f) # deserialize using load()
	print(items_name_loaded)