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
        self.my_home = home
        self.my_sugar = None
        self.exploration_radius = radius

    def work(self):
        print('i stay at:', self.pos)
        # 1st determine exp_radius and go to random neighbor
        # 2nd look for sugar in radius if
        # 2.1 found sugar ==> call_bros in radius

    """
    Der exploration_radius gibt alle möglicherweise erreichbaren Felder/Nachbarn an.
    Validierung findet weiter oben statt, ob etwa Spielfeldende oder ähnliches.
    Idee nimmt einfach aktuelle Position und geht in Abhängikeit des Radius die 
    Nachbarn und Nachbars Nachbarn durch. Alle diese Positionen werden dann zurück gegeben.
    Die Rückgabe erfolgt als Liste von Koordinaten. Befindet sich der Zucker im Radius wird die Koordinate gesetzt.
    """
    def get_exploration_radius(self):
        print('get all elements that could be reached or detected')

    def search_sugar(self):
        print('no sugar at:', self.pos)

    """
    Im exploration_radius werden nach finden des Zuckers, die Nachbarn benachrichtigt.
    """
    def call_bros(self):
        print('call other ants in radius')
