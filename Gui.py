############################
# graphical user interface #
############################

import wx
import wx.grid as gridlib

import sys
import time
import threading

from World import *

cols = 7
rows = 9

edge_length = 40
default_radius = 1

class GridFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title='ant-simulator')
        self.columns = cols
        self.rows = rows
        self.edge_length = edge_length

        self.grid = gridlib.Grid(self, -1)
        self.grid.CreateGrid(self.rows, self.columns)
        self.grid.SetColLabelSize(0)
        self.grid.SetRowLabelSize(0)

        self.set_dimensions_of_grid_field()
        self.coloring_grid_fields()
        self.grid.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.single_left_click)

        #####################
        # other gui objects #
        #####################
        self.ant_world = World(self.rows, self.columns, default_radius)  # 1st arg is rows(y-dimension), 2nd cols(x-dimension)

        t = threading.Thread(target=self.game_loop)
        t.daemon = True
        t.start()

        self.SetSize(self.columns * self.edge_length + 16, self.rows * self.edge_length + 39)
        self.Center()
        self.Show()

    #################
    # gui functions #
    #################

    def set_dimensions_of_grid_field(self):
        for i_1 in range(0, self.rows):
            self.grid.SetRowSize(i_1, self.edge_length)
        for i_2 in range(0, self.columns):
            self.grid.SetColSize(i_2, self.edge_length)

    def coloring_grid_fields(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.grid.SetCellBackgroundColour(row, col, (33, 145, 63, 255))  # RGB color

    def single_left_click(self, event):
        pos = [event.GetRow(), event.GetCol()]  # pos [y-coord, x-coord]
        print("current-x: %s, current-y: %s" % (event.GetCol(), event.GetRow()))
        self.ant_world.increase_population(pos)
        # print(self.ant_world.get_ant_from_population_by_index(0).pos)

    def game_loop(self):
        i = 0
        while True:
            i += 1
            time.sleep(1)
            self.update_view()
            self.ant_world.print_playground()
            self.ant_world.work_population()
            print('step:', i)

    def update_view(self):
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                pos = [row, col]
                self.grid.SetCellBackgroundColour(pos[0], pos[1], (255, 255, 255, 255))

        for row in range(0, self.rows):
            for col in range(0, self.columns):
                pos = [row, col]
                if self.ant_world.get_playground_field(
                        pos) == 0 and pos != self.ant_world.get_ant_home_coord() and pos != self.ant_world.get_sugar_coord():
                    self.grid.SetCellBackgroundColour(pos[0], pos[1], (33, 145, 63, 255))
                else:
                    if pos == self.ant_world.get_sugar_coord():
                        self.grid.SetCellBackgroundColour(pos[0], pos[1], (255, 255, 255, 255))
                    elif pos == self.ant_world.get_ant_home_coord():
                        self.grid.SetCellBackgroundColour(pos[0], pos[1], (50, 40, 12, 255))
                    elif pos != self.ant_world.get_ant_home_coord() and pos != self.ant_world.get_sugar_coord() and \
                            self.ant_world.playground[pos[1]][pos[0]] == -1:
                        self.grid.SetCellBackgroundColour(pos[0], pos[1], (255, 42, 0, 255))
                    else:
                        self.grid.SetCellBackgroundColour(pos[0], pos[1], (52, 146, 235, 255))

        self.ant_world.clear_playground()
        self.grid.ForceRefresh()


#################
# main function #
#################

if __name__ == '__main__':

    if len(sys.argv) < 4:
        print('len', len(sys.argv))
        cols = int(sys.argv[1])
        rows = int(sys.argv[2])
    else:
        print('len', sys.argv)
        cols = int(sys.argv[1])
        rows = int(sys.argv[2])
        radius = int(sys.argv[3])

    if cols > 20 and rows > 20:
        edge_length = 20
        default_radius = radius

    if cols >= 2 and rows >= 2:
        app = wx.App(0)
        frame = GridFrame(None)
        app.MainLoop()
    else:
        if cols < 2 or rows < 2:
            print('2 cols x 2 rows minimum')
