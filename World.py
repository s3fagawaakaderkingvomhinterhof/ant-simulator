######################
# playground of ants #
######################
from random import randrange
from Ant import *


class World:
    def __init__(self, rows, columns):
        self.columns = columns
        self.rows = rows
        self.playground = None
        self.create_playground()
        self.home = None
        self.sugar = None
        self.population = []
        self.prepare_world()

    def create_playground(self):
        self.playground = [[0 for column in range(0, self.rows)] for row in range(self.columns)]

    def get_playground(self):
        return self.playground

    def set_playground_field(self, pos, val):  # args: pos = [y-coord, x-coord], val = int
        self.playground[pos[1]][pos[0]] = val

    def get_playground_field(self, pos):  # arg: pos = [y, x]
        return self.playground[pos[1]][pos[0]]

    def print_playground(self):
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                print(self.playground[col][row], end='|')
            print()

    def set_ant_home_coord(self, pos):  # pos is [x, y] coord
        self.home = pos

    def get_ant_home_coord(self):  # return pos of home
        return self.home

    def set_sugar_coord(self, pos):
        self.sugar = pos

    def get_sugar_coord(self):
        return self.sugar

    def is_field_free(self, pos):
        return self.get_playground_field(pos) == 0

    def create_random_sugar(self, size):
        rand_row = randrange(self.rows)
        rand_col = randrange(self.columns)
        sugar_pos = [rand_row, rand_col]
        self.sugar = sugar_pos
        self.set_playground_field(sugar_pos, size)

    def create_random_home(self):
        rand_row = randrange(self.rows)
        rand_col = randrange(self.columns)
        while [rand_row, rand_col] == self.get_sugar_coord():
            rand_row = randrange(self.rows)
            rand_col = randrange(self.columns)
        self.home = [rand_row, rand_col]

    def prepare_world(self):
        rand_sugar_units = randrange(3, 10)
        self.create_random_sugar(rand_sugar_units)
        self.create_random_home()

    def increase_population(self, pos):
        new_ant = Ant(pos, self.get_ant_home_coord(), 3)
        self.set_playground_field(pos, 1)
        self.population.append(new_ant)

    """
    Hier müssen Nachbarfelder der Ameisen bestimmt werden und Konflikte erkannt werden.
    Also ob Nachfolgerposition noch im Spielfeld ist etc., 
    """
    def work_population(self):
        for ant in range(0, len(self.population)):
            self.population[ant].work()
