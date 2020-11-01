class Field:
    def __init__(self):
        self.coordinate = [-1, -1]
        self.sugar = None # wenn nicht als obj dann bool, dann noch zuckereinheiten
        self.home = None
        self.ant = None

    def get_coordinate(self):
        return self.coordinate

    def get_sugar(self):
        return self.sugar

    def get_home(self):
        return self.home

    def get_ant(self):
        return self.ant

    def is_free(self):
        return  # combination of ...
