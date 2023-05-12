import add_remove
add_remove.add_item('item')
add_remove.remove_item('item')
from Intro import intro_part
intro_part()
from bedroom_hallway import hallway1
hallway1()
from potion_room_2 import potion_weirdness
potion_weirdness()
from Bee_room import bee
bee()
import save_pkl
save_pkl.save_game('player_data')
save_pkl.load_game()

locations = ["bed","table","culdron","bookcase", "toadstool",""] 
my_object = ["potion bag","snail food","broomstick","wand","potion","sacrifice","key","crystal", "leash"]
