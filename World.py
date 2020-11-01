######################
# playground of ants #
######################
from random import randrange
from Ant import *
from Field import *


class World:
    def __init__(self, rows, columns, radius):
        self.default_radius = radius
        self.columns = columns
        self.rows = rows
        self.start_column = 0
        self.end_column = self.columns - 1
        self.start_row = 0
        self.end_row = self.rows - 1
        self.playground = None
        self.create_playground()
        self.ant_home_coord = [-1,-1]
        self.sugar_coord = [-1,-1]
        self.ant_population = []
        self.prepare_world()

    def get_start_column(self):
        return self.start_column

    def get_end_column(self):
        return self.end_column

    def get_start_row(self):
        return self.start_row

    def get_end_row(self):
        return self.end_row

    def create_playground(self):
        self.playground = [[Field for column in range(0, self.rows)] for row in range(self.columns)]

    def get_playground(self):
        return self.playground

    def clear_playground(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.get_playground_field([row, col]) == -2:
                    self.set_playground_field([row, col], 0)
        self.set_playground_field(self.get_sugar_coord(), 9)

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
        self.ant_home_coord = pos

    def get_ant_home_coord(self):  # return pos of home
        return self.ant_home_coord

    def set_sugar_coord(self, pos):
        self.sugar_coord = pos

    def get_sugar_coord(self):
        return self.sugar_coord

    def is_field_free(self, pos):
        return self.get_playground_field(pos) == 0

    def create_random_sugar(self, size):
        sugar_pos = [randrange(self.rows), randrange(self.columns)]
        self.set_sugar_coord(sugar_pos)
        self.set_playground_field(sugar_pos, size)

    def create_random_home(self):
        rand_row = randrange(self.rows)
        rand_col = randrange(self.columns)
        while [rand_row, rand_col] == self.get_sugar_coord():
            rand_row = randrange(self.rows)
            rand_col = randrange(self.columns)
        self.ant_home_coord = [rand_row, rand_col]

    def add_ant_to_ant_population(self, ant):
        self.ant_population.append(ant)

    def get_ant_population(self):
        return self.ant_population

    def get_ant_from_population_by_index(self, ant_index):
        return self.ant_population[ant_index]

    def prepare_world(self):
        rand_sugar_units = randrange(3, 10)
        self.create_random_sugar(rand_sugar_units)
        self.create_random_home()

    def increase_population(self, pos):
        new_ant = Ant(pos, self.get_ant_home_coord(), self.default_radius)
        self.set_playground_field(pos, -1)
        self.add_ant_to_ant_population(new_ant)
        print('population_size:', len(self.ant_population))

    """
    Hier müssen Nachbarfelder der Ameisen bestimmt werden und Konflikte erkannt werden.
    Also ob Nachfolgerposition noch im Spielfeld ist etc., 
    """

    def is_coord_in_playground(self, coord):  # arg: [row, col]
        if self.get_start_row() <= coord[0] <= self.get_end_row() and self.get_start_column() <= coord[
            1] <= self.get_end_column():
            return True
        else:
            return False

    def get_upper_coordinates(self, coord, radius, neighbors):
        for field_upper in range(1, radius + 1):
            row_coord = coord[0] - field_upper
            col_coord = coord[1]
            if self.is_coord_in_playground([row_coord, col_coord]):
                neighbors.append([row_coord, col_coord])

    def get_lower_coordinates(self, coord, radius, neighbors):
        for field_lower in range(1, radius + 1):
            row_coord = coord[0] + field_lower
            col_coord = coord[1]
            if self.is_coord_in_playground([row_coord, col_coord]):
                neighbors.append([row_coord, col_coord])

    def get_left_coordinates(self, coord, radius, neighbors):
        for field_left in range(1, radius + 1):
            row_coord = coord[0]
            col_coord = coord[1] - field_left
            if self.is_coord_in_playground([row_coord, col_coord]):
                neighbors.append([row_coord, col_coord])

    def get_right_coordinates(self, coord, radius, neighbors):
        for field_right in range(1, radius + 1):
            row_coord = coord[0]
            col_coord = coord[1] + field_right
            if self.is_coord_in_playground([row_coord, col_coord]):
                neighbors.append([row_coord, col_coord])

    def get_world_part_of_ant(self, coord, exp_radius):
        neighbors = [coord]
        self.get_upper_coordinates(coord, exp_radius, neighbors)
        self.get_lower_coordinates(coord, exp_radius, neighbors)

        for coord_iter in range(0, len(neighbors)):
            temp_coord = neighbors[coord_iter]
            self.get_left_coordinates(temp_coord, exp_radius, neighbors)
            self.get_right_coordinates(temp_coord, exp_radius, neighbors)

        neighbors.sort()
        return neighbors

    def get_neighbors_in_radius_of_ant(self, ant):
        radius = ant.get_exploration_radius()
        current_ant_position = ant.get_pos()

        list_of_neighbors = self.get_world_part_of_ant(current_ant_position, radius)
        return list_of_neighbors

    def work_population(self):
        for ant_i in range(0, len(self.ant_population)):
            ant = self.get_ant_from_population_by_index(ant_i)

            neighbor_list = self.get_neighbors_in_radius_of_ant(ant)  # change that arg is ant obj
            ant.set_neighbors_in_exp_radius(neighbor_list)
            ant.set_world(self.get_playground())

            ant.work()
