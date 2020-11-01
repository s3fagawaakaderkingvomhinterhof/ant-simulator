#############
# ant class #
#############
"""
Idee für das zufällige bewegen: Ameise bekommt von welt Richtungsvektor.
D.h. mögliche Bewegungsoptionen, Ameise entscheidet sich dan zufällig für einen Weg.
"""
from random import randrange
import threading


def build_empty_world_part_from_neighbor_list(neighbors):
    neighbors.sort()  # sort e.g.:[[0,0],[0,1],[1,0],[1,1]]
    row_count = neighbors[len(neighbors) - 1][0] - neighbors[0][0]  # diff between firt and last row
    column_count = neighbors[len(neighbors) - 1][1] - neighbors[0][1]  # diff between first and last col
    empty_world_part = [[0] * (row_count + 1) for i in range(column_count + 1)]  # + 1 to get real dimension
    return empty_world_part


def copy_world_to_world_part(empty_world_part, world):
    print('empty:', empty_world_part)
    print('world:', world)

class Ant:
    def __init__(self, pos, home, radius):
        self.pos = pos
        self.next_pos = pos
        self.is_in_pack = False     # change to Pack object
        self.my_home_pos = home
        self.my_sugar_pos = [-1, -1]
        self.exploration_radius = radius
        self.neighbors_in_exp_radius = None
        self.old_neighbors = []
        self.direct_neighbors = None
        self.world = [-1,-1]
        """
        t = threading.Thread(target=self.work)
        t.daemon = True
        t.start()
        """

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def clear_pos(self):
        self.world[self.pos[1]][self.pos[0]] = 0

    def set_next_pos(self, pos):
        self.next_pos = pos

    def get_next_pos(self):
        return self.next_pos

    def set_is_in_pack(self, bool):
        self.is_in_pack = bool

    def get_is_in_pack(self):
        return self.is_in_pack

    def set_my_sugar(self, pos):
        self.my_sugar_pos = pos

    def get_my_sugar(self):
        return self.my_sugar_pos

    def set_exploration_radius(self, radius):
        self.exploration_radius = radius

    def get_exploration_radius(self):
        return self.exploration_radius

    def set_neighbors_in_exp_radius(self, part_of_world):
        self.neighbors_in_exp_radius = part_of_world

    def get_neighbors_in_exp_radius(self):
        return self.neighbors_in_exp_radius

    def clear_neighbors_in_exp_radius(self):
        self.neighbors_in_exp_radius = []

    def set_old_neighbors(self, neighbors):
        self.old_neighbors = neighbors

    def get_old_neighbors(self):
        return self.old_neighbors

    def clear_old_neighbors(self):
        for i in range(len(self.old_neighbors)):
            self.world[self.old_neighbors[i][1]][self.old_neighbors[i][0]] = 0

    def set_direct_neighbors(self, direct_neighbors):
        self.direct_neighbors = direct_neighbors

    def get_direct_neighbors(self):
        return self.direct_neighbors

    def set_world(self, world):
        self.world = world

    def get_world(self):
        return self.world

    def clear_world(self):
        print('todo')

    def set_radius_in_world(self):
        for i in range(len(self.neighbors_in_exp_radius)):
            if self.world[self.neighbors_in_exp_radius[i][1]][self.neighbors_in_exp_radius[i][0]] == -1 and self.world[self.neighbors_in_exp_radius[i][1]][self.neighbors_in_exp_radius[i][0]] != self.pos:
                self.world[self.neighbors_in_exp_radius[i][1]][self.neighbors_in_exp_radius[i][0]] = -1
            else:
                self.world[self.neighbors_in_exp_radius[i][1]][self.neighbors_in_exp_radius[i][0]] = -2

    def set_pos_in_world(self):
        self.world[self.pos[1]][self.pos[0]] = -1

    def find_direct_neigbors(self):
        res = []

        all_neighbors = self.get_neighbors_in_exp_radius()
        print('all_neighbors:', all_neighbors)
        row_pos = self.pos[0]
        col_pos = self.pos[1]

        up = [row_pos - 1, col_pos]
        down = [row_pos + 1, col_pos]
        left = [row_pos, col_pos - 1]
        right = [row_pos, col_pos + 1]

        if up in all_neighbors:
            res.append([row_pos - 1, col_pos])

        if down in all_neighbors:
            res.append([row_pos + 1, col_pos])

        if left in all_neighbors:
            res.append([row_pos, col_pos - 1])

        if right in all_neighbors:
            res.append([row_pos, col_pos + 1])

        return res

    def work(self):
        print('i am at', self.get_pos())
        print('world value', self.world[self.pos[1]][self.pos[0]])
        # print(self.world)
        if self.world[self.pos[1]][self.pos[0]] >= 3:
            print('found sugar')
            self.set_my_sugar(self.get_pos())
            print('my_sugar:', self.get_my_sugar())

        if self.get_my_sugar() != [-1, -1]:
            self.call_company()
            # look for field with other ant that is not self.pos ==> look for field with -1
        else:
            self.search_sugar()

        self.clear_neighbors_in_exp_radius()
        self.set_pos(self.next_pos)

    def move_randomly(self):
        self.set_old_neighbors(self.get_neighbors_in_exp_radius())
        self.clear_pos()
        self.clear_old_neighbors()

        walkable_neighbors = self.find_direct_neigbors()  # e.g.:[[0,0],[1,1],[2,0]]
        random_neighbor = randrange(len(walkable_neighbors))
        self.set_next_pos(walkable_neighbors[random_neighbor])

        self.set_radius_in_world()
        self.set_pos_in_world()

        # moved to work method

    def search_sugar(self):
        self.move_randomly()

    def call_company(self):
        self.move_randomly()
        print('call other ants in radius:', self.neighbors_in_exp_radius)

    def communicate(self, ant):
        ant.set_my_sugar(self.get_my_sugar())
