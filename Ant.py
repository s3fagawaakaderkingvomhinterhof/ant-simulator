#############
# ant class #
#############
"""
Idee für das zufällige bewegen: Ameise bekommt von welt Richtungsvektor.
D.h. mögliche Bewegungsoptionen, Ameise entscheidet sich dan zufällig für einen Weg.
"""


class Ant:
    def __init__(self, pos, home, radius):
        self.pos = pos
        self.next_pos = None
        self.is_in_pack = False
        self.my_home_pos = home
        self.my_sugar_pos = [-1, -1]
        self.exploration_radius = radius  # have to be changed when sugar found
        self.part_of_world = None  # array as small partition from the world (current_pos + 8 neighbors)

    def set_next_pos(self, pos):
        self.next_pos = pos

    def get_next_pos(self):
        return self.next_pos

    def set_is_in_pack(self, bool):
        self.is_in_pack = bool

    def get_is_in_pack(self):
        return self.is_in_pack

    def set_my_sugar(self, pos):
        self.my_home_pos = pos

    def get_my_sugar(self):
        return self.my_sugar_pos

    def set_exploration_radius(self, radius):
        self.exploration_radius = radius

    def get_exploration_radius(self):
        return self.exploration_radius

    def set_part_of_world(self, part):
        self.part_of_world = part

    def get_part_of_world(self):
        return self.part_of_world

    def work(self):
        if self.my_sugar_pos == [-1, -1]:
            self.search_sugar()
        else:
            self.call_company()

    def search_sugar(self):
        print('looking for sugar in:', self.part_of_world)

    def call_company(self):
        print('call other ants in:', self.part_of_world)
