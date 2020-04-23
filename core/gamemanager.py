from core import constant
from core.item.item import Item
from core.item.perso import Perso
import random
import logging as lg
logger = lg.getLogger(__name__)


class DisplayManager:

    # item list to display
    map_dict = {}
    collected_items = []

    def __init__(self, display, fenetre, map_game):
        self.display = display
        self.fenetre = fenetre
        self.map_game = map_game

    def draw(self):
        """ display all elements in the game"""
        self.display.draw_map(self.fenetre, self.map_game.map_content)
        self.display.draw_footer(self.fenetre)

        # diplay  all items / perso
        for key in sorted(self.map_dict.keys()):
            self.display.draw_item(self.fenetre, self.map_dict[key])
        self.display.clock()
        self.display.flip()

    def dispatch_items(self):
        """" dispatch the different items in the play area taking care
        that the layout does not block the player """
        # how many boxes are accessible
        nb_pos = len(self.map_game.possible_path)

        # set McGyver personage
        self.map_dict[constant.ID_MCGYVER] = Perso(
            self.map_game.xy_start_point[0],
            self.map_game.xy_start_point[1],
            constant.IMG_MCGYVER)

        p1 = random.choice(range(int(nb_pos / 2), nb_pos))
        self.map_dict[constant.ID_GARDIEN] = Perso(
            (self.map_game.possible_path[p1])[0],
            (self.map_game.possible_path[p1])[1],
            constant.IMG_GARDIEN)

        p2 = random.choice(range(4, p1))
        self.map_dict[constant.ID_AIGUILLE] = Item(
            (self.map_game.possible_path[p2])[0],
            (self.map_game.possible_path[p2])[1],
            constant.IMG_AIGUILLE)

        p3 = random.choice(range(3, p2))
        self.map_dict[constant.ID_ETHER] = Item(
            (self.map_game.possible_path[p3])[0],
            (self.map_game.possible_path[p3])[1],
            constant.IMG_ETHER)

        p4 = random.choice(range(2, p3))
        self.map_dict[constant.ID_TUBE] = Item(
            (self.map_game.possible_path[p4])[0],
            (self.map_game.possible_path[p4])[1],
            constant.IMG_TUBE)

        # final load img for all items / persos
        for key in sorted(self.map_dict.keys()):
            self.display.load_item(self.fenetre, self.map_dict[key])

    def move_items(self, id_item, direction):
        """" move an item or perso in indicated direction """
        self.map_dict[id_item].move(direction, self.map_game.path_course)

    def compare_pos(self, id_item1, id_item2):
        """" compare positions of 2 items => return true if they matches """
        return (self.map_dict[id_item1]).compare_pos(self.map_dict[id_item2])

    def is_exit(self, id_item):
        """" compare positions of item with exit
        => return true if they matches """
        return (self.map_dict[id_item]).compare_pos(
            (self.map_game.xy_end_point[0],
                self.map_game.xy_end_point[1]))

    def collect_item(self, id_item):
        """" add items in hero's bag """
        self.collected_items.append(self.map_dict[id_item])

    def exclude_item(self, id_item, no_place):
        """" exclude items from game """
        self.map_dict[id_item].exclude(no_place)

    def is_completed(self):
        """" returns true if all items are collected """
        return len(self.collected_items) == 3
