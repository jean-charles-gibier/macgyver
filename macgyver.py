#! /usr/bin/env python3
# coding: utf-8

"""This script starts mc Guyver labyrinth parameter is :  file_name (discribing map)."""
from mapgame import MapGame
from perso import Perso
from item import Item
import utils
import constant
import random
import logging as lg

logger = lg.getLogger(__name__)


def dispatch_items(map):
    """" dispatch the different items in the play area taking care
    that the layout does not block the player """
    # set McGyver personage
    mcGyver = Perso(map.xy_start_point[0], map.xy_start_point[1], constant.IMG_MCGYVER)
    # how many boxes are accessible
    nb_pos = len(map.possible_path)
    p1 = random.choice(range(int(nb_pos / 2), nb_pos))
    guard = Perso((map.possible_path[p1])[0], (map.possible_path[p1])[1], constant.IMG_GARDIEN)
    p2 = random.choice(range(4, p1))
    needle = Item((map.possible_path[p2])[0], (map.possible_path[p2])[1], constant.IMG_AIGUILLE)
    p3 = random.choice(range(3, p2))
    ether = Item((map.possible_path[p3])[0], (map.possible_path[p3])[1], constant.IMG_ETHER)
    p4 = random.choice(range(2, p3))
    tube = Item((map.possible_path[p4])[0], (map.possible_path[p4])[1], constant.IMG_TUBE)

    return mcGyver, guard, needle, ether, tube


def main():
    """Main entry no parameter."""
    args = utils.parse_arguments()
    # prepare les logs
    utils.set_logger()
    # lit le fichier map
    map_game = MapGame(args.datafile)
    lg.info('Map description loaded: %s', map_game.path_name)
    interface_type = args.interface
    lg.info('Display interface : %s', args.interface)

    # implementation Text or Graphic
    class_name = "Dal"+interface_type
    module_display = class_name.lower()
    lg.info('Implementation : %s', module_display)
    module = __import__(module_display)
    class_ = getattr(module, class_name)
    display = class_()

    fenetre = display.init(map_game)
    lg.info('%s env set : %s', args.interface, map_game.path_name)

    (mcGyver, guard, needle, ether, tube) = dispatch_items(map_game)
    lg.info('Dispatch items set')

    # collected items
    collected_items = []

    # main loop
    continuer = 1

    while continuer:
        display.draw_map(fenetre, map_game.map_content)
        display.draw_footer(fenetre)
        mcGyver.display(fenetre)
        guard.display(fenetre)
        needle.display(fenetre)
        ether.display(fenetre)
        tube.display(fenetre)
        display.flip()
        display.clock()

        for event in display.event_get():

            # Boucle event
            if display.event_quit(event) == True:
                continuer = 0
            elif display.event_keydown_escape(event) == True :
                continuer = 0
            elif display.event_keydown_right(event) == True:
                mcGyver.deplacer('droite', map_game.path_course)
            elif display.event_keydown_left(event) == True:
                mcGyver.deplacer('gauche', map_game.path_course)
            elif display.event_keydown_up(event) == True:
                mcGyver.deplacer('haut', map_game.path_course)
            elif display.event_keydown_down(event) == True:
                mcGyver.deplacer('bas', map_game.path_course)

            # check items
            if mcGyver.compare_pos(guard):
                lg.info('On rencontre le garde ')
                if len(collected_items) == 3:
                    lg.info('Ok Garde endormi ')
                    guard.value_y = constant.UNIT_SIZE * constant.UNITS_PER_ROW
                    guard.value_x = ((constant.UNIT_SIZE * constant.UNITS_PER_ROW) // 2) +\
                                    ((constant.UNIT_SIZE + 10) * 4)
                else:
                    lg.info('You loose !')

            elif mcGyver.compare_pos(needle):
                lg.info('On rencontre l''aiguille ')
                collected_items.append(needle)
                needle.value_y = constant.UNIT_SIZE * constant.UNITS_PER_ROW
                needle.value_x = (constant.UNIT_SIZE * constant.UNITS_PER_ROW) // 2

            elif mcGyver.compare_pos(ether):
                collected_items.append(ether)
                lg.info('On rencontre la bouteille d''ether ')
                ether.value_y = constant.UNIT_SIZE * constant.UNITS_PER_ROW
                ether.value_x = ((constant.UNIT_SIZE * constant.UNITS_PER_ROW) // 2) +\
                                (constant.UNIT_SIZE + 10)

            elif mcGyver.compare_pos(tube):
                collected_items.append(tube)
                lg.info('On rencontre le tube ')
                tube.value_y = constant.UNIT_SIZE * constant.UNITS_PER_ROW
                tube.value_x = ((constant.UNIT_SIZE * constant.UNITS_PER_ROW) // 2) +\
                               ((constant.UNIT_SIZE + 10) * 2)

            elif mcGyver.compare_pos((map_game.xy_end_point[0], map_game.xy_end_point[1])):
                if len(collected_items) == 3:
                    lg.info('You win !')


if __name__ == "__main__":
    main()
