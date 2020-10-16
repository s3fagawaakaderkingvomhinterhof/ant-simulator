from World import *
from random import randrange

ant_world = World(4, 3)         # when creating world 1st give rows = y-dimension, 2nd cols = x-dimension
#ant_world.print_playground()

ant_world.create_random_sugar(10)
ant_world.print_playground()

print('sugar is at:', ant_world.get_sugar_coord())
print('sugar amount is:', ant_world.get_playground_field(ant_world.get_sugar_coord()))
ant_world.create_random_home()

print('ant home is:', ant_world.get_ant_home_coord())
