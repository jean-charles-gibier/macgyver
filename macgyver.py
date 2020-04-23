#! /usr/bin/env python3
# coding: utf-8

"""This script starts mc Guyver labyrinth
parameter is :
  file_name (discribing map)."""
from core.gamemanager import DisplayManager
from core.mapgame import MapGame
from core import utils
from core import constant
from tkinter import messagebox, Tk
import logging as lg

logger = lg.getLogger(__name__)

MODULE_DAL_PATH = 'core/dal'


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
    display = utils.build_display(MODULE_DAL_PATH, interface_type)

    # get Pygame windows
    fenetre = display.init(map_game)
    lg.info('%s env set : %s', args.interface, map_game.path_name)

    # set display manager : intialize items and persos
    game_manager = DisplayManager(display, fenetre, map_game)

    # dispatch item and perso (mcGyver, guard, needle, ether, tube)
    game_manager.dispatch_items()
    lg.info('Dispatch items set')

    # main loop
    continuer = 1

    while continuer:

        game_manager.draw()

        for event in display.event_get():
            # Boucle event
            if event is None:
                continue

            if display.event_quit(event) is True:
                continuer = 0
            elif display.event_keydown_escape(event) is True:
                continuer = 0
            elif display.event_keydown_right(event) is True:
                game_manager.move_items(constant.ID_MCGYVER, 'droite')
            elif display.event_keydown_left(event) is True:
                game_manager.move_items(constant.ID_MCGYVER, 'gauche')
            elif display.event_keydown_up(event) is True:
                game_manager.move_items(constant.ID_MCGYVER, 'haut')
            elif display.event_keydown_down(event) is True:
                game_manager.move_items(constant.ID_MCGYVER, 'bas')

            # check items
            if game_manager.compare_pos(constant.ID_MCGYVER,
                                        constant.ID_GARDIEN):
                lg.info('On rencontre le garde ')
                if game_manager.is_completed():
                    game_manager.exclude_item(constant.ID_GARDIEN, 4)
                    lg.info('Ok Garde endormi ')
                else:
                    lg.info('You loose !')
                    Tk().wm_withdraw()
                    messagebox.showinfo('Oups', 'You loose !')
                    continuer = 0

            elif game_manager.compare_pos(constant.ID_MCGYVER,
                                          constant.ID_AIGUILLE):
                lg.info('On rencontre l\'aiguille ')
                game_manager.collect_item(constant.ID_AIGUILLE)
                game_manager.exclude_item(constant.ID_AIGUILLE, 0)

            elif game_manager.compare_pos(constant.ID_MCGYVER,
                                          constant.ID_ETHER):
                lg.info('On rencontre la bouteille d\'ether ')
                game_manager.collect_item(constant.ID_ETHER)
                game_manager.exclude_item(constant.ID_ETHER, 1)

            elif game_manager.compare_pos(constant.ID_MCGYVER,
                                          constant.ID_TUBE):
                lg.info('On rencontre le tube ')
                game_manager.collect_item(constant.ID_TUBE)
                game_manager.exclude_item(constant.ID_TUBE, 2)

            elif game_manager.is_exit(constant.ID_MCGYVER):
                if game_manager.is_completed():
                    lg.info('You win !')
                    # on redessine une derniere fois la fenetre du jeu
                    game_manager.draw()
                    Tk().wm_withdraw()
                    messagebox.showinfo('Congratulations', 'You win !')
                    continuer = 0


if __name__ == "__main__":
    main()
