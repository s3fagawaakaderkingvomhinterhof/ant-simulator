from World import *
from random import randrange
from Ant import *

ant_world = World(4, 4)  # when creating world 1st give rows = y-dimension, 2nd cols = x-dimension
"""
important: constructor calls prepare world method 
"""

ant_world.print_playground()

print('sugar is at:', ant_world.get_sugar_coord())
print('sugar amount is:', ant_world.get_playground_field(ant_world.get_sugar_coord()))
print('ant home is:', ant_world.get_ant_home_coord())

print(ant_world.is_coord_in_playground([39, 39]))

neighbors = ant_world.get_world_part_of_ant([0, 0], 2)

#print('neighbors:', neighbors)

print('playground unformatted:', ant_world.playground)

print(build_empty_world_part_from_neighbor_list(neighbors))

list = [[0,0],[0,1],[1,0]]
a = [0,0]

print()
print('list:', list)
print('a:', a)

print(a in list)
print(randrange(3))

found = []